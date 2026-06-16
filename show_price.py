
import requests

response = requests.get(
    "https://testnet.binancefuture.com/fapi/v1/ticker/price?symbol=BTCUSDT"
)

data = response.json()

print(data["price"])