import asyncio
import aiohttp
from dotenv import load_dotenv
import os
load_dotenv()

async def purchase(amount, username):
    async with aiohttp.ClientSession() as session:
        token = os.getenv("FRAGMENT_API")
        url = "https://api.fragment-api.com/v1/order/stars/"
        payload = {
                  "username": username,
                  "quantity": amount,
                  "show_sender": False
                }

        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": f"JWT {token}"
        }
        async with session.post(url, json=payload, headers=headers) as response:
            return await response.json()




