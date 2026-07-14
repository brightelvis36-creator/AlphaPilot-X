def calculate_risk(balance, risk_percent):
    amount = balance * (risk_percent / 100)
    return round(amount, 2)


def trade_plan():
    return """
📊 AlphaPilot Trade Plan

Pair: EURUSD
Direction: BUY
Entry: Manual
Stop Loss: Manual
Take Profit: Manual

Always confirm before trading.
"""
