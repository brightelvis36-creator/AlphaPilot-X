def calculate_risk(balance, risk_percent):
    amount = balance * (risk_percent / 100)
    return round(amount, 2)


def trade_setup(pair="EURUSD"):
    return f"""
📊 AlphaPilot Trade Plan

Pair: {pair}
Direction: Manual
Trend: Manual
Entry: Manual
Stop Loss: Manual
Take Profit: Manual
Risk/Reward: 1:2 (Recommended)

Checklist:
☐ Trend confirmed
☐ Support identified
☐ Resistance identified
☐ Risk calculated
☐ Entry confirmed

⚠️ Always confirm your setup before placing a trade.
"""
