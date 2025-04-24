import json

import aiohttp
from config.settings import settings


async def scrape_linkedin_profile(url: str) -> dict:
    """
    Raspagem de informações de perfis do LinkedIn.
    A função busca dados de uma URL especificada que contém os dados mockados em formato JSON.

    Args:
        url (str): A URL do perfil do LinkedIn.
    Returns:
        dict: Um dicionário contendo as informações raspadas.
    Raises:
        Exception: Se a resposta da API não for bem-sucedida (código de status diferente de 200).
    """

    headers = {"Authorization": "Bearer " + settings.PROXY_CURL_API_KEY}
    params = {"url": url}
    async with aiohttp.ClientSession() as session:
        async with session.get(
            settings.PROXY_CURL_API_URL, headers=headers, params=params
        ) as response:
            if response.status == 200:
                text_data = await response.text()
                data = json.loads(text_data)
                return data
            else:
                raise Exception(f"Erro: {response.status}")
