from datetime import datetime


def get_price(pair):
    pair = pair.upper()

    return {
        "pair": pair,
        "price": "Waiting for live feed",
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
