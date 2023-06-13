import asyncio
import time
import aiohttp

async def download_site(session, url):
    async with session.get(url) as response:
        print("Read {0} from {1}" .format(response.content_length, url))

