from nsepy import get_quote, get_history


def get_live_price(symbol):
    return get_quote(symbol)


