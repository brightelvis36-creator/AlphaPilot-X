from strategy import analyze_strategy


def analyze_multi_timeframe(pair="EURUSD"):

    trend_4h = analyze_strategy(pair, "4h")
    confirmation_1h = analyze_strategy(pair, "1h")
    entry_15m = analyze_strategy(pair, "15m")

    signals = [
        trend_4h["signal"],
        confirmation_1h["signal"],
        entry_15m["signal"]
    ]

    buy_count = signals.count("BUY")
    sell_count = signals.count("SELL")

    if buy_count == 3:
        decision = "BUY"
        confidence = 92
        setup = "🔥 Elite Setup"

    elif sell_count == 3:
        decision = "SELL"
        confidence = 92
        setup = "🔥 Elite Setup"

    elif buy_count >= 2:
        decision = "BUY"
        confidence = 80
        setup = "🟢 Strong Setup"

    elif sell_count >= 2:
        decision = "SELL"
        confidence = 80
        setup = "🟢 Strong Setup"

    else:
        decision = "WAIT"
        confidence = 50
        setup = "⚪ Mixed Timeframes"

    return {
        "pair": pair.upper(),
        "trend_4h": trend_4h,
        "confirmation_1h": confirmation_1h,
        "entry_15m": entry_15m,
        "decision": decision,
        "confidence": confidence,
        "setup": setup
    }
