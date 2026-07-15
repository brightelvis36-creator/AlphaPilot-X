import json
import os

HISTORY_FILE = "trade_history.json"


def load_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as file:
            return json.load(file)
    return []


def save_history(history):
    with open(HISTORY_FILE, "w") as file:
        json.dump(history, file, indent=4)


def add_trade(pair, direction, entry, stop_loss, take_profit, result):
    history = load_history()

    trade = {
        "pair": pair,
        "direction": direction,
        "entry": entry,
        "stop_loss": stop_loss,
        "take_profit": take_profit,
        "result": result
    }

    history.append(trade)
    save_history(history)

    return "✅ Trade saved successfully."


def get_history():
    return load_history()
