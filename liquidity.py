def detect_liquidity(candles):

    if len(candles) < 5:
        return {
            "liquidity": "UNKNOWN",
            "reason": "Not enough candle data"
        }

    highs = [candle["high"] for candle in candles]
    lows = [candle["low"] for candle in candles]

    recent_highs = highs[-5:]
    recent_lows = lows[-5:]

    high_range = max(recent_highs) - min(recent_highs)
    low_range = max(recent_lows) - min(recent_lows)


    if high_range < 0.0005:
        return {
            "liquidity": "BUY SIDE LIQUIDITY",
            "reason": "Similar highs detected",
            "level": max(recent_highs)
        }


    elif low_range < 0.0005:
        return {
            "liquidity": "SELL SIDE LIQUIDITY",
            "reason": "Similar lows detected",
            "level": min(recent_lows)
        }


    else:
        return {
            "liquidity": "NO CLEAR LIQUIDITY",
            "reason": "No equal highs or lows detected"
        }
