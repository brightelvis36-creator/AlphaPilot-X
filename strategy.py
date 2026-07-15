from candles import get_candles
from indicators import sma, ema, rsi


def analyze_strategy(pair="EURUSD"):

    candles = get_candles(pair)

    if not candles:
        return {
            "pair": pair.upper(),
            "signal": "WAIT",
            "confidence": 0,
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

    # Trend check
    if ema_value > sma_value:
        score += 30
        reasons.append("EMA bullish trend")
    else:
        score -= 30
        reasons.append("EMA bearish trend")

    # RSI check
    if rsi_value > 55:
        score += 30
        reasons.append("RSI bullish momentum")

    elif rsi_value < 45:
        score -= 30
        reasons.append("RSI bearish momentum")

    else:
        reasons.append("RSI neutral")

    # Candle movement
    if last_price > previous_price:
        score += 20
        reasons.append("Price rising")
    else:
        score -= 20
        reasons.append("Price falling")

    # Final decision
    if score >= 50:
        signal = "BUY"

    elif score <= -50:
        signal = "SELL"

    else:
        signal = "WAIT"

    # Confidence
    if signal == "WAIT":
        confidence = 50
    else:
        confidence = min(abs(score) + 20, 95)

    return {
        "pair": pair.upper(),
        "signal": signal,
        "confidence": confidence,
        "SMA": round(sma_value, 5),
        "EMA": round(ema_value, 5),
        "RSI": round(rsi_value, 2),
        "reason": ", ".join(reasons)
    }
