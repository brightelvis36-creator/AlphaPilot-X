from candles import get_candles
from indicators import sma, ema, rsi


def analyze_strategy(pair="EURUSD"):

    candles = get_candles(pair)

    if not candles:
        return {
            "pair": pair.upper(),
            "signal": "WAIT",
            "confidence": 0,
            "setup": "No Setup",
            "reason": "No candle data available"
        }

    prices = [candle["close"] for candle in candles]

    sma_value = sma(prices)
    ema_value = ema(prices)
    rsi_value = rsi(prices)

    score = 0
    reasons = []

    last_price = prices[-1]
    previous_price = prices[-2]


    if ema_value > sma_value:
        score += 35
        reasons.append("EMA bullish trend")
    else:
        score -= 35
        reasons.append("EMA bearish trend")


    if rsi_value > 60:
        score += 35
        reasons.append("Strong RSI momentum")

    elif rsi_value >= 50:
        score += 15
        reasons.append("RSI positive")

    elif rsi_value < 40:
        score -= 35
        reasons.append("Strong RSI weakness")

    else:
        reasons.append("RSI neutral")


    if last_price > previous_price:
        score += 30
        reasons.append("Price confirmation bullish")
    else:
        score -= 30
        reasons.append("Price confirmation bearish")


    if score >= 60:
        signal = "BUY"

    elif score <= -60:
        signal = "SELL"

    else:
        signal = "WAIT"


    confidence = min(abs(score), 95)


    if confidence >= 90:
        setup = "🔥 Elite Setup"

    elif confidence >= 75:
        setup = "🟢 Strong Setup"

    elif confidence >= 60:
        setup = "🟡 Moderate Setup"

    else:
        setup = "⚪ Weak Setup"


    if signal == "WAIT":
        confidence = 50
        setup = "⚪ No Clear Setup"


    return {
        "pair": pair.upper(),
        "signal": signal,
        "confidence": confidence,
        "setup": setup,
        "SMA": round(sma_value, 5),
        "EMA": round(ema_value, 5),
        "RSI": round(rsi_value, 2),
        "reason": ", ".join(reasons)
    }
