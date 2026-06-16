import argparse
from bot.client import get_price
from bot.validators import validate_symbol
from bot.logging_config import logger
from orders import Orders


class API:
    def get_price(self, symbol):
        return get_price(symbol)


parser = argparse.ArgumentParser()

parser.add_argument("--symbol", required=True)
parser.add_argument("--side", required=True)
parser.add_argument("--type", required=True)
parser.add_argument("--qty", type=float, default=0.01)
parser.add_argument("--limit", type=float, default=None)

args = parser.parse_args()

symbol = args.symbol.upper()

if not validate_symbol(symbol):
    print("Invalid Symbol")
    exit()

api = API()
orders = Orders()

price = api.get_price(symbol)
print("Price:", price)

logger.info(f"Price fetched for {symbol}: {price}")

order_type = args.type.upper()

if order_type == "MARKET":
    result = orders.market_order(symbol, args.side.upper(), args.qty)
    print("RESULT:", result)

elif order_type == "LIMIT":
    
    if args.limit is None:
        print("ERROR: LIMIT price required (--limit)")
    else:
        result = orders.limit_order(
            symbol,
            args.side.upper(),
            args.qty,
            args.limit
        )
        print("RESULT:", result)

else:
    print("Invalid order type (use MARKET or LIMIT)")

