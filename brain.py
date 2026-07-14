from datetime import datetime
from memory import remember, get_all_memory

def alphapilot_response(message):
    message = message.lower().strip()

    if message == "hello":
        return "👋 Hello Boss! AlphaPilot is online. 🧠"

    elif message == "status":
        return "🟢 AlphaPilot is online."

    elif message == "time":
        return datetime.now().strftime("🕒 %Y-%m-%d %H:%M:%S")

    elif message == "help":
        return """
🚀 AlphaPilot Commands

hello
status
time
help
"""

    else:
        return "🤖 Unknown command. Type 'help'."
