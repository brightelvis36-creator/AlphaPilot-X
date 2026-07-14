import requests


def get_price(pair):
    symbols = {
        "BTCUSD": "bitcoin",
        "ETHUSD": "ethereum",
        "SOLUSD": "solana"
    }

    pair = pair.upper()

    if pair not in symbols:
        return f"❌ Pair {pair} not supported yet."

    try:
        url = (
            f"https://api.coingecko.com/api/v3/simple/price"
            f"?ids={symbols[pair]}&vs_currencies=usd"
        )

        response = requests.get(url, timeout=10)
        data = response.json()

        price = data[symbols[pair]]["usd"]

        return f"""
📈 AlphaPilot Live Market

Pair: {pair}

Current Price: ${price}

Status: Live ✅
"""

    except Exception as e:
        return f"❌ Network Error: {e}"


def market_status():
    return """
📊 AlphaPilot Market Status

🟢 Crypto Market: Live

🚀 Live Forex coming soon.
"""
