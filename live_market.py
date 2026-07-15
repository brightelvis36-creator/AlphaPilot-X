from datetime import datetime


def get_market_data(pair):
    pair = pair.upper()

    return f"""
📡 Live Market Data

Pair: {pair}

Price: Waiting for feed

Time: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

Status: Connected
"""
