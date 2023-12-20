# используется aiohttp для асинхронного скачивания страниц и asyncio для организации
# асинхронного выполнения кода.

import aiohttp
import asyncio

urls = ['http://ya.ru', 'http://lenta.ru', 'http://gb.ru']


async def download_url(url, file_name):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            with open(file_name, 'wb') as f:
                f.write(await resp.read())


async def main():
    tasks = []
    for i, url in enumerate(urls):
        file_name = f'file_{i}.html'
        tasks.append(download_url(url, file_name))
    await asyncio.gather(*tasks)


asyncio.run(main())
