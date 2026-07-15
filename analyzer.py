def analyze_market(pair, price):

    result = {
        "pair": pair,
        "price": price,
        "trend": "UNKNOWN",
        "support": "N/A",
        "resistance": "N/A",
        "signal": "WAIT",
        "confidence": "0%"
    }

    try:
        if price == "Unavailable" or price is None:
            result["signal"] = "WAIT"
            result["confidence"] = "0%"
            return result

        price = float(price)

        if price > 1:
            result["trend"] = "BULLISH"
            result["signal"] = "BUY"
            result["confidence"] = "70%"

        elif price < 1:
            result["trend"] = "BEARISH"
            result["signal"] = "SELL"
            result["confidence"] = "70%"

    except Exception:
        pass

    return result
