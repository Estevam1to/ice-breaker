from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama


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

    # llm = ChatAnthropic(
    #     api_key=settings.ANTROPIC_API_KEY,
    #     model_name="claude-3-opus-20240229",
    #     temperature=0,
    # )

    llm = ChatOllama(
        model="llama3",
        temperature=0,
    )

    # Chain é uma classe que combina um prompt com um modelo de linguagem para gerar uma resposta.
    chain = summary_prompt_template | llm | StrOutputParser()

    output = await chain.ainvoke(
        input={
            "information": "Eu sou uma pessoa muito criativa e gosto de pensar fora da caixa. Além disso, sou apaixonado por música e toco violão desde os 10 anos. Também sou um grande fã de esportes radicais e já pratiquei escalada em rocha."
        }
    )

    print(output)


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
