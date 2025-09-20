import aiohttp

async def get_exchangerate():

    async with aiohttp.ClientSession() as session:
        async with session.get('https://api.privatbank.ua/p24api/pubinfo?exchange&json&coursid=11') as response:

            html = await response.json()
            return float(html[1]["sale"])

