def sma(prices):
    if not prices:
        return 0
    return sum(prices) / len(prices)


def ema(prices):
    if not prices:
        return 0

    alpha = 2 / (len(prices) + 1)
    ema_value = prices[0]

    for price in prices[1:]:
        ema_value = (price * alpha) + (ema_value * (1 - alpha))

    return round(ema_value, 5)


def rsi(prices):
    if len(prices) < 2:
        return 50

    gains = []
    losses = []

    for i in range(1, len(prices)):
        change = prices[i] - prices[i - 1]

        if change > 0:
            gains.append(change)
        else:
            losses.append(abs(change))

    avg_gain = sum(gains) / max(len(gains), 1)
    avg_loss = sum(losses) / max(len(losses), 1)

    if avg_loss == 0:
        return 100

    rs = avg_gain / avg_loss
    value = 100 - (100 / (1 + rs))

    return round(value, 2)


def atr(candles, period=14):

    if len(candles) < period + 1:
        return 0

    true_ranges = []

    for i in range(1, len(candles)):

        high = candles[i]["high"]
        low = candles[i]["low"]
        previous_close = candles[i-1]["close"]

        tr = max(
            high - low,
            abs(high - previous_close),
            abs(low - previous_close)
        )

        true_ranges.append(tr)

    return round(sum(true_ranges[-period:]) / period, 5)
