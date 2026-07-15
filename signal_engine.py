from market_feed import get_price
from strategy import analyze_strategy
from candles import get_candles
from trade_setup import calculate_trade_setup


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

Reason:
{result["reason"]}

SMA: {result["SMA"]}
EMA: {result["EMA"]}
RSI: {result["RSI"]}

⚠️ No clear setup.
"""

    candles = get_candles(pair)

    setup = calculate_trade_setup(
        pair,
        signal,
        price,
        candles
    )

    return f"""
📡 AlphaPilot Smart Signal

Pair: {pair}

Signal: {signal}

Confidence: {confidence}%

Entry: {setup["entry"]}

Stop Loss: {setup["stop_loss"]}

Take Profit: {setup["take_profit"]}

Risk Reward: {setup["risk_reward"]}

Reason:
{result["reason"]}

SMA: {result["SMA"]}
EMA: {result["EMA"]}
RSI: {result["RSI"]}
"""
