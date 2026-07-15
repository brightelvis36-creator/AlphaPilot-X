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
def get_history():
    return load_history()


def show_history():
    history = get_history()
def get_stats():
    history = get_history()

    total = len(history)

    if total == 0:
        return "📊 No trades recorded yet."

    wins = 0
    losses = 0

    for trade in history:
        result = trade["result"].upper()

        if result == "WIN":
            wins += 1
        elif result == "LOSS":
            losses += 1

    win_rate = (wins / total) * 100

    return f"""
📊 Trading Statistics

Total Trades: {total}
Wins: {wins}
Losses: {losses}
Win Rate: {win_rate:.1f}%
"""
    if not history:
        return "📒 No trades saved yet."

    output = "📒 AlphaPilot Trade Journal\n\n"

    for i, trade in enumerate(history, start=1):
        output += (
            f"{i}. {trade['pair']} | "
            f"{trade['direction']} | "
            f"{trade['result']}\n"
        )

    return output
