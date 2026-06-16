import requests

BASE_URL = "https://testnet.binancefuture.com/fapi/v1"

def get_price(symbol):
    try:
        url = f"{BASE_URL}/ticker/price"
        params = {"symbol": symbol}

        response = requests.get(url, params=params, timeout=5)

        if response.status_code != 200:
            raise Exception(f"API Error: {response.text}")

        data = response.json()

        if "price" not in data:
            raise Exception(f"Invalid response: {data}")

        return float(data["price"])

    except Exception as e:
        print("Price Fetch Error:", e)
        return None