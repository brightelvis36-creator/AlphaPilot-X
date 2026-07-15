from datetime import datetime
from market_feed import get_price

def get_market_data(pair):
    data = get_price(pair)

    return f"""
📡 Live Market Data

Pair: {data['pair']}

Price: {data['price']}

Time: {data['time']}

Status: Connected
"""

