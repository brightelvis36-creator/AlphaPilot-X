def analyze_setup(pair, direction, entry, stop_loss, take_profit):
    risk = abs(float(entry) - float(stop_loss))
    reward = abs(float(take_profit) - float(entry))

    if risk == 0:
        return "❌ Invalid setup: Stop Loss cannot equal Entry"

    ratio = reward / risk

    return f"""
📊 Trade Setup Analysis

Pair: {pair.upper()}
Direction: {direction.upper()}
Entry: {entry}
Stop Loss: {stop_loss}
Take Profit: {take_profit}

Risk/Reward: 1:{ratio:.2f}

Status: {"✅ Good setup" if ratio >= 2 else "⚠️ Weak setup"}
"""
