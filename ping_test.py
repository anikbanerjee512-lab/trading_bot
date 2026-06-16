import requests

response = requests.get(
    "https://testnet.binancefuture.com/fapi/v1/time"
)

data = response.json()

print(data["serverTime"])