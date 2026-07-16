from market_structure import detect_structure


def detect_choch(candles):

    structure = detect_structure(candles)

    if structure["structure"] == "UNKNOWN":
        return {
            "choch": "NONE",
            "reason": "Not enough candle data"
        }

    last_close = candles[-1]["close"]

    structure_high = structure["high"]
    structure_low = structure["low"]


    if structure["structure"] == "BULLISH":

        if last_close < structure_low:
            return {
                "choch": "BEARISH CHOCH",
                "reason": "Price broke bullish structure low",
                "level": structure_low
            }


    elif structure["structure"] == "BEARISH":

        if last_close > structure_high:
            return {
                "choch": "BULLISH CHOCH",
                "reason": "Price broke bearish structure high",
                "level": structure_high
            }


    return {
        "choch": "NO CHOCH",
        "reason": "Trend structure remains valid"
    }
