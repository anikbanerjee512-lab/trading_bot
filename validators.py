def validate_symbol(symbol):
    if not symbol:
        return False

    symbol = symbol.upper()

    if len(symbol) < 6:
        return False

    if not symbol.endswith("USDT"):
        return False

    return True