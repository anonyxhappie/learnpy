import aiohttp
import asyncio
import sys

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    async with aiohttp.ClientSession() as session:
        try:
            url = sys.argv[1]
        except IndexError:
            url = 'http://python.org'

        try:
            html = await fetch(session, url)
            print(html)
        except Exception as e:
            print(e)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())