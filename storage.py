from rich import print
from datetime import datetime
import random

print("[bold green]🚀 AlphaPilot v1.0[/bold green]")
print("[yellow]Type 'help' to see commands[/yellow]")

balance = 0
risk = 0

def response(text):
    print(f"[cyan]AlphaPilot:[/cyan] {text}")

while True:
    command = input("\nYou: ").lower()

    if command == "hello":
        response("Hello boss 👋 I'm AlphaPilot, ready.")

    elif command == "who are you":
        response("I'm AlphaPilot, your personal AI assistant.")

    elif command == "creator":
        response("I was created by Bright.")

    elif command == "time":
        response(str(datetime.now()))

    elif command == "help":
        print("""
[bold]Available Commands:[/bold]

hello
who are you
creator
time
set account
risk
analyze
signal
motivate
status
exit
""")

    elif command == "set account":
        balance = float(input("Account balance: $"))
        response(f"Account set to ${balance}")

    elif command == "risk":
        risk = float(input("Risk percentage: "))
        amount = balance * (risk / 100)
        response(f"Risk amount: ${amount:.2f}")

    elif command == "analyze":
        response("Market analysis system loading 📊")
        response("Checking trend, support and resistance...")

    elif command == "signal":
        pairs = ["EURUSD", "GBPUSD", "USDJPY", "BTCUSD"]
        choice = random.choice(pairs)
        direction = random.choice(["BUY", "SELL"])

        response(f"Pair: {choice}")
        response(f"Possible direction: {direction}")
        response("Always confirm with your own analysis.")

    elif command == "motivate":
        response("Keep building. Every great project starts small 🚀")

    elif command == "status":
        response("AlphaPilot is online ✅")

    elif command == "exit":
        response("Goodbye boss 👋")
        break

    else:
        response("I don't understand that command.")
