from indicators import atr


def calculate_trade_setup(pair, signal, price, candles, risk_reward=2):

    volatility = atr(candles)

    if volatility == 0:
        return {
            "error": "Unable to calculate volatility"
        }

    if signal == "BUY":

        stop_loss = price - volatility * 2
        take_profit = price + (volatility * 2 * risk_reward)

    elif signal == "SELL":

        stop_loss = price + volatility * 2
        take_profit = price - (volatility * 2 * risk_reward)

    else:

        return {
            "pair": pair,
            "signal": "WAIT",
            "message": "No trade setup"
        }

    return {
        "pair": pair,
        "signal": signal,
        "entry": round(price, 5),
        "stop_loss": round(stop_loss, 5),
        "take_profit": round(take_profit, 5),
        "risk_reward": f"1:{risk_reward}"
    }
