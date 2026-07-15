from candles import get_candles
from indicators import sma, ema, rsi


def analyze_strategy(pair="EURUSD"):

    candles = get_candles(pair)

    if not candles:
        return {
            "signal": "WAIT",
            "confidence": 0,
            "reason": "No candle data available"
        }

    prices = [candle["close"] for candle in candles]

    sma_value = sma(prices)
    ema_value = ema(prices)
    rsi_value = rsi(prices)

    signal = "HOLD"
    confidence = 50

    reason = []

    if ema_value > sma_value and rsi_value > 50:
        signal = "BUY"
        confidence = 75
        reason.append("EMA above SMA")
        reason.append("RSI bullish")

    elif ema_value < sma_value and rsi_value < 50:
        signal = "SELL"
        confidence = 75
        reason.append("EMA below SMA")
        reason.append("RSI bearish")

    else:
        signal = "WAIT"
        confidence = 50
        reason.append("Mixed indicators")

    return {
        "pair": pair.upper(),
        "signal": signal,
        "confidence": confidence,
        "SMA": round(sma_value, 5),
        "EMA": round(ema_value, 5),
        "RSI": round(rsi_value, 2),
        "reason": ", ".join(reason)
    }
