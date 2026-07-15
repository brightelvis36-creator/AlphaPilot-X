from brain import alphapilot_response

print("=" * 45)
print("🚀 AlphaPilot X v13")
print("Personal AI Trading Assistant")
print("Type 'help' for commands.")
print("Type 'exit' to quit.")
print("=" * 45)

while True:
    user = input("\nYou: ").strip()

    if user.lower() in ["exit", "quit"]:
        print("AlphaPilot: Goodbye Boss 👋")
        break

    response = alphapilot_response(user)
    print(f"\nAlphaPilot: {response}")
