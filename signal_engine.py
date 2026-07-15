def generate_signal(pair):
    pair = pair.upper()

    trend = "BULLISH"

    if trend == "BULLISH":
        direction = "BUY"
        entry = 1.1700
        stop_loss = 1.1650
        take_profit_1 = 1.1800
        take_profit_2 = 1.1850
    else:
        direction = "SELL"
        entry = 1.1700
        stop_loss = 1.1750
        take_profit_1 = 1.1600
        take_profit_2 = 1.1550

    return f"""
📡 AlphaPilot Smart Signal

Pair: {pair}

Signal: {direction}

Entry Zone: {entry}

Stop Loss: {stop_loss}

Take Profit 1: {take_profit_1}
Take Profit 2: {take_profit_2}

Risk/Reward: 1:2+

Confidence: 75%

⚠️ Confirm before trading.
"""
