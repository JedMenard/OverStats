import asyncio
import aiohttp

from overwatch_api.core import AsyncOWAPI
from overwatch_api.constants import *


async def testing(loop, battletag):
    # Instantiating the api
    client = AsyncOWAPI()

    data = {}

    async with aiohttp.ClientSession(
            connector=aiohttp.TCPConnector(verify_ssl=False))
    
        print('Fetching data for {}...'.format(battletag))
        data[PC] = await client.get_hero_stats(
            battletag, session=session, platform=PC)

    return data

def scrape(battletag):
    data = {}

    timeout = True;
    while timeout:      # Repeat loop if a timeout occurs
        try:
            loop = asyncio.get_event_loop()
            data = loop.run_until_complete(testing(loop))
            timeout = False
        except asyncio.TimeoutError:
            print("Timed out, retrying...")
    print("Done!")
    data[PC]['us']['stats']['competitive']['mercy']['general_stats']
    return data[PC]['us']

