from market_structure import detect_structure


def detect_bos(candles):

    structure = detect_structure(candles)

    if structure["structure"] == "UNKNOWN":
        return {
            "bos": "NONE",
            "reason": "Not enough data"
        }

    last_close = candles[-1]["close"]

    structure_high = structure["high"]
    structure_low = structure["low"]


    if last_close > structure_high:
        return {
            "bos": "BULLISH BOS",
            "reason": "Price broke previous structure high",
            "level": structure_high
        }


    elif last_close < structure_low:
        return {
            "bos": "BEARISH BOS",
            "reason": "Price broke previous structure low",
            "level": structure_low
        }


    else:
        return {
            "bos": "NO BOS",
            "reason": "Structure still holding"
        }
