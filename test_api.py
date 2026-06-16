import requests

response = requests.get("https://testnet.binancefuture.com/fapi/v1/ping")

print(response.status_code)
print(response.text)