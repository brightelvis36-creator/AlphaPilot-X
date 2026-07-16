from smart_money import analyze_smart_money
from multi_timeframe import analyze_multi_timeframe


def make_final_decision(pair="EURUSD"):

    # Get Multi-Timeframe Analysis
    mtf = analyze_multi_timeframe(pair)

    # Get Smart Money Analysis
    from candles import get_candles
    candles = get_candles(pair, "1h")

    smart_money = analyze_smart_money(candles)


    score = 0
    reasons = []


    # Multi-Timeframe Score
    if mtf["decision"] == "BUY":
        score += 40
        reasons.append("Multi-timeframe bullish")

    elif mtf["decision"] == "SELL":
        score -= 40
        reasons.append("Multi-timeframe bearish")


    # Smart Money Score
    score += smart_money["score"]

    if smart_money["score"] > 0:
        reasons.append("Smart money bullish")

    elif smart_money["score"] < 0:
        reasons.append("Smart money bearish")


    # Final Decision

    if score >= 50:
        decision = "BUY"

    elif score <= -50:
        decision = "SELL"

    else:
        decision = "WAIT"


    confidence = min(abs(score) + 50, 95)


    return {
        "pair": pair.upper(),
        "decision": decision,
        "confidence": confidence,
        "score": score,
        "multi_timeframe": mtf,
        "smart_money": smart_money,
        "reason": ", ".join(reasons)
    }
