from config.settings import settings
from langchain_anthropic import ChatAnthropic
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

# from config.logs import logger
from utils.likedin import scrape_linkedin_profile
from agents.linkedin_lookup_agent import LinkedinLookupAgent


async def ice_break_with(name: str) -> str:
    """
    Executa o agente de busca para encontrar o perfil do LinkedIn de uma pessoa com base no nome completo fornecido.
    Args:
        name (str): O nome completo da pessoa cujo perfil do LinkedIn deve ser localizado.
    Returns:
        str: A URL direta para o perfil do LinkedIn da pessoa.
    """
    agent = LinkedinLookupAgent()
    linkedin_profile_url = await agent.execute(name=name)
    linkedin_profile_data = await scrape_linkedin_profile(url=linkedin_profile_url)

    summary_prompt = """Dadas as informações abaixo sobre uma pessoa, elabore um resumo que contenha:
        1. Um breve resumo de sua personalidade;
        2. Dois fatos interessantes e distintos sobre ela.
        Dados: {information}
        Responda sempre em PT-BR e não use formatação de código.
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_prompt
    )

    llm = ChatAnthropic(
        api_key=settings.ANTROPIC_API_KEY,
        model_name=settings.ANTROPIC_MODEL_NAME,
        temperature=0,
    )

    chain = summary_prompt_template | llm | StrOutputParser()

    output = await chain.ainvoke(
        input={
            "information": linkedin_profile_data,
        }
    )

    print(output)


async def main():
    """
    Função principal que executa a função de quebra-gelo com um nome específico.
    """
    name = "Luís Estevam MlOPs"
    await ice_break_with(name=name)


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
