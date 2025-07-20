import requests
import decimal
import random
import json
import os
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("URL")
wallet = os.getenv("WALLET")

tokens = []
ver = True
i = 1

while ver == True:
    token = os.getenv(f"TOKEN{i}")
    if not token:
        ver = False
        break
    else:
        tokens.append(token)
        i += 1

x = 0

for token in tokens:
    x += 1

    headers = {
        "User-Agent": "Dart/3.3 (dart:io)",
        "Accept-Encoding": "gzip",
        "x-access-token": token,
    }

    response = requests.get(f"{url}/mining-contracts", headers=headers)

    if response.status_code == 200:

        # 24 horas
        response = requests.post(f"{url}/daily-reward", headers=headers)

        # 8 horas
        response = requests.post(
            f"{url}/free-mining-contract", headers=headers)

        # Ver Ads 24 horas 4.02 Gh/s
        payload = {
            "ecpm_tier": "FIVE",
        }
        response = requests.post(
            f"{url}/rewarded-mining-contract", data=payload, headers=headers)

        # Sacar
        response = requests.get(url, headers=headers)
        balance = response.json()["btc_balance_in_satoshi_nanos"]
        if balance >= 10000000000:
            print(f"ID: {x} | Sacando: {balance}")
        else:
            print(f"ID: {x} | Saldo insuficiente para saque: {balance}")

    else:
        print("Erro ao acessar a API:")
