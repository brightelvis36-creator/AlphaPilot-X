import os
import requests
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()


def get_price(pair):
    pair = pair.upper()

    if len(pair) == 6:
        pair = pair[:3] + "/" + pair[3:]

    api_key = os.getenv("TWELVE_DATA_API_KEY")

    if not api_key:
        return {
            "pair": pair,
            "price": "Unavailable",
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "status": "Missing API key"
        }

    try:
        url = (
            "https://api.twelvedata.com/price"
            f"?symbol={pair}"
            f"&apikey={api_key}"
        )

        response = requests.get(url, timeout=10)
        data = response.json()

        if "price" not in data:
            return {
                "pair": pair,
                "price": "Unavailable",
                "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "status": data.get("message", "API error")
            }

        return {
            "pair": pair,
            "price": round(float(data["price"]), 5),
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "status": "Connected"
        }

    except Exception as e:
        return {
            "pair": pair,
            "price": "Unavailable",
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "status": str(e)
        }
