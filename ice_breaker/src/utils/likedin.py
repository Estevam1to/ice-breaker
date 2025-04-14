import json

import aiohttp
from config.settings import settings


async def scrape_linkedin_profile(url: str, mock: bool = False) -> dict:
    """
    Scrape information from a LinkedIn profiles.
    The function fetches data from a specified URL that contains the mock data in JSON format.

    Args:
        url (str): The LinkedIn profile URL.

    Returns:
        dict: A dictionary containing the scraped information.
    """

    if mock:
        url = "https://gist.githubusercontent.com/emarco177/859ec7d786b45d8e3e3f688c6c9139d8/raw/5eaf8e46dc29a98612c8fe0c774123a7a2ac4575/eden-marco-scrapin.json"

        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                text_data = await response.text()
                data = json.loads(text_data)
                return data
    else:
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
                    raise Exception(f"Error: {response.status}")
