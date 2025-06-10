import requests
import decimal
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
    
    msg = f"ID: {x} | "
    
    headers = {
        "User-Agent": "Dart/3.4 (dart:io)",
        "Accept-Encoding": "gzip",
        "Content-Type": "application/json",
        "app_version": "4.3.1",
        "authorization": f"Bearer {token}",
    }

    getHash = requests.get(f"{url}/machine:hasFree", headers=headers)

    if getHash.status_code == 200:
        has = getHash.json()
        if has["data"]["has"]:
            claimHash = requests.post(f"{url}/machine:receiveFree", headers=headers)
            msg += f"Claim Hash: {claimHash.json()['data']['miningRatePerCore']} | "
        else:
            msg += "Hash NÃO disponível. | "

        balance = requests.get(f"{url}/machine:income", headers=headers).json()
        b = balance["data"]["balance"]
        minimo = requests.get(f"{url}/config:get?appId=3", headers=headers).json()
        m = minimo["data"]["withdrawal_limit"]["lightning"].split("-")[0]

        if b > m:
            d = decimal.Decimal(b)
            btc = float(d.quantize(decimal.Decimal("0.00000001"), rounding=decimal.ROUND_DOWN))
            urlSacar = f"{url}/withdraw:apply?chain=speed&walletType=speedaddr&asset=BTC&amount={btc}&wallet={wallet}"
            sacar = requests.post(urlSacar, headers=headers)
            msg += f"Saque recebido: {sacar.json()['data']['receivedAmount']} | Saldo: {sacar.json()['data']['balance']}"
        else:
            msg += f"Saldo insuficiente para saque. | Saldo: {b} | Mínimo: {m}"
        
        print(msg)

    else:
        print("Erro ao acessar a API:")
