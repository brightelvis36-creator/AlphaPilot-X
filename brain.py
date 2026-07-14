from datetime import datetime
from memory import remember, get_all_memory


def alphapilot_response(message):
    message = message.lower().strip()

    if message in ["hello", "hi", "hey"]:
        return "👋 Hello Boss! AlphaPilot Brain v2 is online. 🧠"

    elif message == "status":
        return "🟢 AlphaPilot systems online. Brain v2 active."

    elif message == "time":
        return datetime.now().strftime("🕒 %Y-%m-%d %H:%M:%S")

    elif message == "memory":
        memories = get_all_memory()
        if memories:
            return f"🧠 Memory:\n{memories}"
        else:
            return "🧠 No memories stored yet."

    elif message.startswith("learn "):
        info = message.replace("learn ", "", 1)
        remember("user_info", info)
        return f"✅ Learned: {info}"

    elif message == "help":
        return """
🚀 AlphaPilot Brain v2 Commands

hello
status
time
memory
learn [information]
help

Example:
learn my name is Bright
"""

    else:
        return "🤖 I don't understand yet. Type 'help' to see commands."
