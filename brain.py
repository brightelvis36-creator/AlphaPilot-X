from datetime import datetime

from memory import remember, get_all_memory
from analyzer import analyze_market
from market_feed import get_price
from signal_engine import generate_signal


def alphapilot_response(message):
    message = message.lower().strip()

    if message in ["hello", "hi", "hey"]:
        return "👋 Hello Boss! AlphaPilot Brain v9.4 is online. 🧠"

    elif message == "status":
        return "🟢 AlphaPilot systems online. Brain active."

    elif message == "time":
        return datetime.now().strftime("🕒 %Y-%m-%d %H:%M:%S")

    elif message == "memory":
        memories = get_all_memory()
        return f"🧠 Memory:\n{memories}"

    elif message.startswith("learn "):
        info = message.replace("learn ", "", 1)
        remember("user_info", info)
        return f"✅ Learned: {info}"

    elif message.startswith("signal "):
        pair = message.replace("signal ", "", 1).upper()
        return generate_signal(pair)

    elif message.startswith("analyze "):
        parts = message.split()

        if len(parts) >= 2:
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

        return "Usage: analyze EURUSD"

    elif message == "help":
        return """
🚀 AlphaPilot Commands

hello
status
time
memory
learn [info]
signal EURUSD
analyze EURUSD
help
"""

    else:
        return "🤖 I don't understand that command. Type help."
