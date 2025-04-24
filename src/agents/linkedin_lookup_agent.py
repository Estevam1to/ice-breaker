from langchain import hub
from langchain.agents import AgentExecutor, create_react_agent
from langchain.prompts import PromptTemplate
from langchain.tools import Tool
from langchain_anthropic import ChatAnthropic
from config.settings import settings
from tools.search_tool import get_profile_url_tavily


class LinkedinLookupAgent:
    async def execute(self, name: str) -> str:
        """
        Executa o agente de busca para encontrar o perfil do LinkedIn de uma pessoa com base no nome completo fornecido.

        Args:
            name (str): O nome completo da pessoa cujo perfil do LinkedIn deve ser localizado.

        Returns:
            str: A URL direta para o perfil do LinkedIn da pessoa.

        Comportamento:
            - Utiliza um modelo de linguagem (LLM) configurado com a API da Anthropic para processar o prompt.
            - Define um template de prompt que solicita apenas a URL do perfil do LinkedIn.
            - Usa uma ferramenta personalizada para buscar o link do perfil no LinkedIn através do Google.
            - Cria um agente reativo (react agent) para executar a tarefa.
            - Retorna a URL do perfil do LinkedIn como resultado.
        """

        llm = ChatAnthropic(
            api_key=settings.ANTROPIC_API_KEY,
            model=settings.ANTROPIC_MODEL_NAME,
            temperature=0,
        )

        template = """Dado o nome completo de uma pessoa {name_of_person}, quero que você me envie o link direto para o perfil dela no LinkedIn. 
        Sua resposta deve conter apenas a URL, sem nenhum texto adicional."""

        prompt_template = PromptTemplate(
            input_variables=["name_of_person"],
            template=template,
        )

        tools_for_agent = [
            Tool(
                name="Crawl Google 4 LinkedIn Profile Page",
                func=get_profile_url_tavily,
                description="Use this tool to get the LinkedIn profile link of a person.",
            ),
        ]

        react_prompt = hub.pull("hwchase17/react")

        agent = create_react_agent(
            llm=llm,
            tools=tools_for_agent,
            prompt=react_prompt,
        )

        agent_executor = AgentExecutor(
            agent=agent,
            tools=tools_for_agent,
            verbose=True,
            handle_parsing_errors=True,
        )

        result = await agent_executor.ainvoke(
            input={"input": prompt_template.format_prompt(name_of_person=name)}
        )

        linkedin_profile_url = result["output"]

        return linkedin_profile_url
