from datetime import datetime
from memory import remember, recall, forget, get_all_memory
from trading import trade_setup
from history import add_trade, get_history, show_history, get_stats


def alphapilot_response(message):
    original = message
    message = message.lower().strip()

    if message in ["hello", "hi", "hey"]:
        return "👋 Hello Boss! AlphaPilot Brain v8.3 is online. 🧠"

    elif message == "status":
        return "🟢 AlphaPilot systems online. Memory Intelligence active."

    elif message == "time":
        return datetime.now().strftime("🕒 %Y-%m-%d %H:%M:%S")

    elif message == "memory":
        memories = get_all_memory()
        if memories:
            return f"🧠 Memory:\n{memories}"
        return "🧠 No memories stored yet."

    elif message.startswith("learn "):
        info = original[6:]
        remember("user_info", info)
        return f"✅ Learned: {info}"

    elif message.startswith("remember "):
        info = original[9:]

        if " is " in info:
            key, value = info.split(" is ", 1)
            remember(key.strip(), value.strip())
            return f"🧠 Saved memory: {key.strip()} = {value.strip()}"

        return "⚠️ Use: remember key is value"

    elif message.startswith("recall "):
        key = original[7:].strip()
        result = recall(key)

        if result is not None:
            return f"🧠 {key}: {result}"

        return f"🧠 I don't remember '{key}'."

    elif message.startswith("forget "):
        key = original[7:].strip()

        if forget(key):
            return f"🗑️ Forgot: {key}"

        return f"🧠 I couldn't find '{key}'."

    elif message == "help":
        return """
🚀 AlphaPilot Brain v8.3 Commands

hello
status
time
memory
learn [information]
remember key is value
recall key
forget key
help

Examples:
learn my name is Bright
remember favorite pair is EURUSD
recall favorite pair
forget favorite pair
"""
    elif message.startswith("trade "):
        pair = original[6:].strip().upper()
        return trade_setup(pair)
    elif message == "journal":
        return show_history()

    elif message.startswith("journal "):
        ...

        if len(parts) == 7:
            _, pair, direction, entry, stop_loss, take_profit, result = parts

            return add_trade(
                pair.upper(),
                direction.upper(),
                entry,
                stop_loss,
                take_profit,
                result.upper()
            )

        return (
            "Usage:\n"
            "journal PAIR BUY/SELL ENTRY STOPLOSS TAKEPROFIT WIN/LOSS\n"
            "Example:\n"
            "journal EURUSD BUY 1.1700 1.1660 1.1780 WIN"
        )
    elif message == "stats":
        return get_stats()

    else:
        return "🤖 I don't understand that command yet. Type 'help' to see available commands."
    
  
