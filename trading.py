from market_feed import get_price
from strategy import analyze_strategy
from risk_reward import calculate_rr


def calculate_risk(balance, risk_percent):
    amount = balance * (risk_percent / 100)
    return round(amount, 2)


def trade_setup(pair="EURUSD", balance=1000, risk_percent=2):

    market = get_price(pair)
    
    if market["price"] == "Unavailable":
        return "❌ Market price unavailable."

    price = float(market["price"])

    strategy = analyze_strategy(pair)

    signal = strategy["signal"]
    confidence = strategy["confidence"]

    if signal == "BUY":
        stop_loss = round(price - 0.0050, 5)
        take_profit = round(price + 0.0100, 5)

    elif signal == "SELL":
        stop_loss = round(price + 0.0050, 5)
        take_profit = round(price - 0.0100, 5)

    else:
        return f"""
📊 AlphaPilot Trade Plan

Pair: {pair}

Signal: WAIT

Confidence: {confidence}%

Reason:
{strategy["reason"]}

⚠️ No trade setup.
"""

    risk_amount = calculate_risk(balance, risk_percent)

    reward_distance = abs(take_profit - price)
    risk_distance = abs(price - stop_loss)

    rr = calculate_rr(risk_distance, reward_distance)

    return f"""
📊 AlphaPilot Trade Plan

Pair: {pair}

Signal: {signal}

Entry: {round(price,5)}

Stop Loss: {stop_loss}

Take Profit: {take_profit}

Risk Amount: ${risk_amount}

{rr}

Confidence: {confidence}%

Reason:
{strategy["reason"]}

⚠️ Confirm before trading.
"""
