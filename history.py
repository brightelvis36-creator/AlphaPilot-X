import requests


def get_history(pair="BTCUSD", days=30):

    coins = {
        "BTCUSD": "bitcoin",
        "ETHUSD": "ethereum",
        "SOLUSD": "solana"
    }

    pair = pair.upper()

    if pair not in coins:
        return []

    try:
        url = (
            f"https://api.coingecko.com/api/v3/coins/"
            f"{coins[pair]}/market_chart?vs_currency=usd&days={days}"
        )

        response = requests.get(url, timeout=10)
        data = response.json()

        prices = []

        for item in data["prices"]:
            prices.append(item[1])

        return prices

    except:
        return []
