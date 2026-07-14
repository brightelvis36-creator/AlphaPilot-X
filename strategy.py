from indicators import sma, ema, rsi


def analyze_market(prices):
    sma_value = sma(prices)
    ema_value = ema(prices)
    rsi_value = rsi(prices)

    signal = "HOLD"
    confidence = 50

    if ema_value > sma_value and rsi_value < 70:
        signal = "BUY"
        confidence = 85

    elif ema_value < sma_value and rsi_value > 30:
        signal = "SELL"
        confidence = 85

    return {
        "sma": round(sma_value, 2),
        "ema": round(ema_value, 2),
        "rsi": round(rsi_value, 2),
        "signal": signal,
        "confidence": confidence
    }
