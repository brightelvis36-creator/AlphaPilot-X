def detect_structure(candles):

    if len(candles) < 5:
        return {
            "structure": "UNKNOWN",
            "reason": "Not enough candle data"
        }

    highs = [candle["high"] for candle in candles]
    lows = [candle["low"] for candle in candles]

    recent_high = highs[-1]
    previous_high = highs[-3]

    recent_low = lows[-1]
    previous_low = lows[-3]


    if recent_high > previous_high and recent_low > previous_low:
        structure = "BULLISH"
        pattern = "Higher High + Higher Low"

    elif recent_high < previous_high and recent_low < previous_low:
        structure = "BEARISH"
        pattern = "Lower High + Lower Low"

    elif recent_high > previous_high:
        structure = "BULLISH"
        pattern = "Higher High"

    elif recent_low < previous_low:
        structure = "BEARISH"
        pattern = "Lower Low"

    else:
        structure = "RANGE"
        pattern = "No clear structure"


    return {
        "structure": structure,
        "pattern": pattern,
        "high": recent_high,
        "low": recent_low
    }
