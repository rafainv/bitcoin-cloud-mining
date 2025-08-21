import requests
import json
import os

url = os.getenv("URL_A")
wallet = os.getenv("WALLET")
device_id = os.getenv("DEVICE_ID")
lang_country = os.getenv("LANG_COUNTRY")
token_A1 = os.getenv("TOKEN_A1")

headers = {
  'User-Agent': "okhttp/4.9.1",
  'Connection': "Keep-Alive",
  'Accept-Encoding': "gzip",
  'Content-Type': "application/json",
  'log-header': "I am the log request header.",
  'appVersion': "188",
  'deviceCountry': lang_country,
  'deviceId': device_id,
  'langCountry': lang_country,
  'token': token_A1,
  'Content-Type': "application/json; charset=UTF-8"
}

payload = {
  "nid": "1"
}

response = requests.post(url, data=json.dumps(payload), headers=headers)

if response.status_code == 200:
    print("Acesso à API bem-sucedido")
else:
    print("Erro ao acessar a API")
