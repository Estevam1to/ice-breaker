from config.settings import settings
from tavily import TavilyClient


def get_profile_url_tavily(query: str) -> dict:
    """
    Busca a URL do perfil do LinkedIn correspondente a uma consulta usando o TavilyClient.

    Args:
        query (str): A consulta de pesquisa para encontrar o perfil do LinkedIn.
    Returns:
        str: A URL do perfil do LinkedIn correspondente à consulta fornecida.
    Raises:
        KeyError: Se a chave "url" não estiver presente no resultado retornado pelo TavilyClient.
        TavilyClientError: Se ocorrer um erro ao realizar a busca com o TavilyClient.
    """

    client = TavilyClient(api_key=settings.TAVILY_API_KEY)

    result = client.search(query=query, max_results=1)

    return result
