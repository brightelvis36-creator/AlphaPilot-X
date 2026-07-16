import os
import requests
from dotenv import load_dotenv

load_dotenv()


def get_candles(pair="EURUSD", timeframe="1h"):

    pair = pair.upper()

    if len(pair) == 6:
        pair = pair[:3] + "/" + pair[3:]

    timeframe_map = {
        "5m": "5min",
        "15m": "15min",
        "30m": "30min",
        "1h": "1h",
        "4h": "4h",
        "1d": "1day"
    }

    interval = timeframe_map.get(
        timeframe.lower(),
        "1h"
    )

    api_key = os.getenv("TWELVE_DATA_API_KEY")

    url = (
        "https://api.twelvedata.com/time_series"
        f"?symbol={pair}"
        f"&interval={interval}"
        f"&outputsize=100"
        f"&apikey={api_key}"
    )

    try:

        response = requests.get(url, timeout=30)

        data = response.json()

    except Exception:

        return None

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

