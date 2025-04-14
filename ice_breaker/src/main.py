from config.settings import settings
from langchain_anthropic import ChatAnthropic
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

# from langchain_ollama import ChatOllama
# from config.logs import logger
from utils.likedin import scrape_linkedin_profile


async def main():
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
        model_name="claude-3-opus-20240229",
        temperature=0,
    )

    # llm = ChatOllama(
    #     model="llama3",
    #     temperature=0,
    # )

    # Chain é uma classe que combina um prompt com um modelo de linguagem para gerar uma resposta.
    chain = summary_prompt_template | llm | StrOutputParser()

    data = await scrape_linkedin_profile(url="https://www.linkedin.com/in/estevamluis/")

    output = await chain.ainvoke(
        input={
            "information": data,
        }
    )

    print(output)


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
