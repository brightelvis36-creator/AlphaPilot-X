from datetime import datetime

from memory import remember, get_all_memory
from analyzer import analyze_market
from market_feed import get_price
from signal_engine import generate_signal
from trade_plan import generate_trade_plan


def alphapilot_response(message):

    message = message.strip()

    if message.lower() in ["hello", "hi", "hey"]:
        return "👋 Hello Boss! AlphaPilot Brain v15.1 is online. 🧠"

    elif message.lower() == "status":
        return "🟢 AlphaPilot systems online."

    elif message.lower() == "time":
        return datetime.now().strftime("🕒 %Y-%m-%d %H:%M:%S")

    elif message.lower() == "memory":
        memories = get_all_memory()
        return f"🧠 Memory:\n{memories}"

    elif message.lower().startswith("learn "):
        info = message[6:]
        remember("user_info", info)
        return f"✅ Learned: {info}"

    elif message.lower().startswith("signal "):

        parts = message.split()

        if len(parts) < 2:
            return "Usage: signal EURUSD"

        pair = parts[1].upper()

        return generate_signal(pair)

    elif message.lower().startswith("plan "):

        parts = message.split()

        if len(parts) < 2:
            return """
Usage:

plan EURUSD

or

plan EURUSD 500

or

plan EURUSD 500 1
"""

        pair = parts[1].upper()

        balance = 1000
        risk = 2

        if len(parts) >= 3:
            try:
                balance = float(parts[2])
            except ValueError:
                return "❌ Invalid account balance."

        if len(parts) >= 4:
            try:
                risk = float(parts[3])
            except ValueError:
                return "❌ Invalid risk percentage."

        return generate_trade_plan(
            pair,
            balance=balance,
            risk_percent=risk
        )

    elif message.lower().startswith("analyze "):

        parts = message.split()

        if len(parts) < 2:
            return "Usage: analyze EURUSD"

        pair = parts[1].upper()

        market = get_price(pair)
        price = market.get("price")

        result = analyze_market(pair, price)

        return f"""
📊 AlphaPilot Market Analysis

Pair: {result['pair']}
Price: {result['price']}

Trend: {result['trend']}

Support: {result['support']}
Resistance: {result['resistance']}

Signal: {result['signal']}
Confidence: {result['confidence']}
"""

    elif message.lower() == "help":

        return """
🚀 AlphaPilot X Commands

hello
status
time
memory
learn [information]

signal EURUSD

plan EURUSD

plan EURUSD 500

plan EURUSD 500 1

analyze EURUSD

help
"""

    else:
        return "🤖 I don't understand that command. Type 'help'."
