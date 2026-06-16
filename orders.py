import os
import time
import hmac
import hashlib
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_SECRET= os.getenv("API_SECRET")

BASE_URL = "https://testnet.binancefuture.com/fapi/v1"


class Orders:

    def get_price(self, symbol):
        url = f"{BASE_URL}/ticker/price"
        response = requests.get(url, params={"symbol": symbol}, timeout=5)
        data = response.json()
        return float(data["price"])

    def _generate_signature(self, query_string):
        if API_SECRET is None:
            raise Exception("API_SECRET not found in .env file")

        return hmac.new(
            API_SECRET.encode("utf-8"),
            query_string.encode("utf-8"),
            hashlib.sha256
        ).hexdigest()

    def market_order(self, symbol, side, quantity):
        try:
            params = {
                "symbol": symbol,
                "side": side,
                "type": "MARKET",
                "quantity": quantity,
                "timestamp": int(time.time() * 1000)
            }

            query_string = "&".join(
                [f"{k}={v}" for k, v in params.items()]
            )

            signature = self._generate_signature(query_string)

            headers = {
                "X-MBX-APIKEY": API_KEY
            }

            url = f"{BASE_URL}/order?{query_string}&signature={signature}"

            response = requests.post(url, headers=headers, timeout=10)

            data = response.json()

            print("Response:", data)

            return data

        except Exception as e:
            print("Market Order Error:", e)
            return None

    def limit_order(self, symbol, side, quantity, price):
       
        try:
            params = {
                "symbol": symbol,
                "side": side,
                "type": "LIMIT",
                "quantity": quantity,
                "price": price,
                "timeInForce": "GTC",
                "timestamp": int(time.time() * 1000)
            }

            query_string = "&".join(
                [f"{k}={v}" for k, v in params.items()]
            )

            signature = self._generate_signature(query_string)

            headers = {
                "X-MBX-APIKEY": API_KEY
            }

            url = f"{BASE_URL}/order?{query_string}&signature={signature}"

            response = requests.post(
                url,
                headers=headers,
                timeout=10
            )

            data = response.json()
           
            print(data)
            print("Response:", data)

            return data

        except Exception as e:
            print("Limit Order Error:", e)
            return None