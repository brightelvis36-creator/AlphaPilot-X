def detect_order_block(candles):

    if len(candles) < 3:
        return {
            "order_block": "UNKNOWN",
            "reason": "Not enough candle data"
        }

    previous = candles[-2]
    current = candles[-1]

    previous_open = previous["open"]
    previous_close = previous["close"]

    current_close = current["close"]


    # Bullish Order Block
    if previous_close < previous_open and current_close > previous["high"]:

        return {
            "order_block": "BULLISH ORDER BLOCK",
            "reason": "Bearish candle followed by bullish displacement",
            "zone_high": previous["high"],
            "zone_low": previous["low"]
        }


    # Bearish Order Block
    elif previous_close > previous_open and current_close < previous["low"]:

        return {
            "order_block": "BEARISH ORDER BLOCK",
            "reason": "Bullish candle followed by bearish displacement",
            "zone_high": previous["high"],
            "zone_low": previous["low"]
        }


    else:

        return {
            "order_block": "NO ORDER BLOCK",
            "reason": "No institutional displacement detected"
        }
