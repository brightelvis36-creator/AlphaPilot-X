def calculate_risk(balance, risk_percent):

    risk_amount = balance * (risk_percent / 100)

    return round(risk_amount, 2)


def calculate_stop_distance(entry, stop_loss):

    distance = abs(entry - stop_loss)

    return round(distance, 5)


def calculate_pips(entry, stop_loss):

    distance = abs(entry - stop_loss)

    pips = distance * 10000

    return round(pips, 1)


def calculate_lot_size(risk_amount, stop_pips):

    if stop_pips <= 0:
        return 0

    pip_value = 10

    lot_size = risk_amount / (stop_pips * pip_value)

    return round(lot_size, 2)


def risk_report(balance, risk_percent, entry, stop_loss):

    risk_amount = calculate_risk(
        balance,
        risk_percent
    )

    stop_distance = calculate_stop_distance(
        entry,
        stop_loss
    )

    stop_pips = calculate_pips(
        entry,
        stop_loss
    )

    lot_size = calculate_lot_size(
        risk_amount,
        stop_pips
    )

    return f"""
💰 AlphaPilot Risk Manager

Balance: ${balance}

Risk: {risk_percent}%

Maximum Loss: ${risk_amount}

Entry: {entry}

Stop Loss: {stop_loss}

Stop Distance: {stop_distance}

Stop Pips: {stop_pips}

Suggested Lot Size: {lot_size}
"""

