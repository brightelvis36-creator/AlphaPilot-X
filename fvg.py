def detect_fvg(candles):

    if len(candles) < 3:
        return {
            "fvg": "UNKNOWN",
            "reason": "Not enough candle data"
        }

    candle1 = candles[-3]
    candle3 = candles[-1]


    # Bullish FVG
    if candle3["low"] > candle1["high"]:

        return {
            "fvg": "BULLISH FVG",
            "reason": "Price left bullish imbalance",
            "gap_high": candle3["low"],
            "gap_low": candle1["high"]
        }


    # Bearish FVG
    elif candle3["high"] < candle1["low"]:

        return {
            "fvg": "BEARISH FVG",
            "reason": "Price left bearish imbalance",
            "gap_high": candle1["low"],
            "gap_low": candle3["high"]
        }


    else:

        return {
            "fvg": "NO FVG",
            "reason": "No imbalance detected"
        }
