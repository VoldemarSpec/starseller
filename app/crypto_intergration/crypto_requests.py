import asyncio

import aiohttp
import json
from dotenv import load_dotenv
import os

load_dotenv()
headers = {
    "Authorization": "Token " + os.getenv("CRYPTO_CLOUD_KEY"),
    "Content-Type": "application/json"
}


async def create_invoice(amount, order_id):
    async with aiohttp.ClientSession() as session:
        data = {
            "amount": amount * float(os.getenv("PRICE")),
            "shop_id": os.getenv("CRYPTO_STORE_ID"),
            "currency": "USD",
            "ordr_id": order_id,
            "add_fields": {"cryptocurrency": "USDT_TON"}
        }
        url = "https://api.cryptocloud.plus/v2/invoice/create"
        async with session.post(url, headers=headers, json=data) as response:
            html = await response.json()
            return ([html["result"]["link"], html["result"]["uuid"]])


async def cancel_invoice(uuid):
    async with aiohttp.ClientSession() as session:
        url = "https://api.cryptocloud.plus/v2/invoice/merchant/canceled"
        data = {
            "uuid": uuid
        }
        async with session.post(url, json=data, headers=headers) as response:
            html = await response.json()
            return html
