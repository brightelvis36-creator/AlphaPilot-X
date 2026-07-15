from market_feed import get_price
from strategy import analyze_strategy


def generate_signal(pair):

    market = get_price(pair)

    if market["price"] == "Unavailable":
        return "❌ Live market price unavailable."

    price = float(market["price"])

    result = analyze_strategy(pair)

    signal = result["signal"]
    confidence = result["confidence"]

    if signal == "WAIT":
        return f"""
📡 AlphaPilot Smart Signal

Pair: {pair}

Signal: WAIT

Confidence: {confidence}%

Reason: {result["reason"]}

SMA: {result["SMA"]}
EMA: {result["EMA"]}
RSI: {result["RSI"]}

⚠️ No clear setup.
"""

    if signal == "BUY":
        sl = price - 0.0050
        tp1 = price + 0.0100
        tp2 = price + 0.0150

    else:
        sl = price + 0.0050
        tp1 = price - 0.0100
        tp2 = price - 0.0150

    return f"""
📡 AlphaPilot Smart Signal

Pair: {pair}

Signal: {signal}

Entry: {round(price,5)}

Stop Loss: {round(sl,5)}

Take Profit 1: {round(tp1,5)}

Take Profit 2: {round(tp2,5)}

Confidence: {confidence}%

Reason: {result["reason"]}

⚠️ Confirm before trading.
"""

