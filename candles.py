import os
import requests
from dotenv import load_dotenv

load_dotenv()


def get_candles(pair="EURUSD", interval="1h"):
    pair = pair.upper()

    if len(pair) == 6:
        pair = pair[:3] + "/" + pair[3:]

    api_key = os.getenv("TWELVE_DATA_API_KEY")

    url = (
        "https://api.twelvedata.com/time_series"
        f"?symbol={pair}"
        f"&interval={interval}"
        f"&outputsize=100"
        f"&apikey={api_key}"
    )

    response = requests.get(url, timeout=15)
    data = response.json()

    if "values" not in data:
        return None

    candles = []

    for item in reversed(data["values"]):
        candles.append({
            "open": float(item["open"]),
            "high": float(item["high"]),
            "low": float(item["low"]),
            "close": float(item["close"])
        })

    return candles
