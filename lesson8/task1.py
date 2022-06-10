import asyncio
import re

import aiohttp

BASE_URL = 'http://127.0.0.1:8000'
CATEGORY_URL = f'{BASE_URL}/category/'

urls = ['http://127.0.0.1:8000/category/', ]

LINK_PATTERN = re.compile(r'<a[^href]+href="([^"]*)" class="card col-md-4 m-2"')
TEXT_PATTERN = re.compile(r'card-title\s*"\s*>\s*([^<]+)')


async def get_url(url):
    print(f'Starting {url}')
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.text()
            data_len = len(data)
            print(f'Received {data_len}')
            links = LINK_PATTERN.findall(data, re.DOTALL)
            texts = TEXT_PATTERN.findall(data, re.DOTALL)
            for text, link in zip(texts, links):
                print(f'{text}: {BASE_URL}{link}')


futures = [get_url(url) for url in urls]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait([get_url(CATEGORY_URL)]))
