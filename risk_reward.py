def calculate_rr(risk, reward):
    if risk <= 0:
        return "❌ Risk must be greater than 0"

    ratio = reward / risk

    return f"""
📐 Risk Reward Calculator

Risk: ${risk}
Reward: ${reward}
Ratio: 1:{ratio:.2f}
"""
