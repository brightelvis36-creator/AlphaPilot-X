import requests
from datetime import datetime


def get_price(pair):
    pair = pair.upper()

    try:
        url = f"https://api.twelvedata.com/price?symbol={pair}"

        response = requests.get(url, timeout=10)
        data = response.json()

        price = data.get("price")

        if price:
            return {
                "pair": pair,
                "price": price,
                "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "status": "Live"
            }

        return {
            "pair": pair,
            "price": "Unavailable",
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "status": data.get("message", "No data")
        }

    except Exception as e:
        return {
            "pair": pair,
            "price": "Unavailable",
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "status": str(e)
        }
