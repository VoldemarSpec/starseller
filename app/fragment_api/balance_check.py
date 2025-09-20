import requests
from dotenv import load_dotenv
import os
load_dotenv()
url = "https://api.fragment-api.com/v1/misc/wallet/"

def check_balance():

    headers = {
        "Accept": "application/json",
        "Authorization": f"JWT {os.getenv("fragment_api")}"
    }

    response = requests.get(url, headers=headers)

    return response.json()["balance"]


print(check_balance())

