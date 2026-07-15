def calculate_risk(balance, risk_percent):

    risk_amount = balance * (risk_percent / 100)

    return round(risk_amount, 2)


def calculate_stop_distance(entry, stop_loss):

    distance = abs(entry - stop_loss)

    return round(distance, 5)


def risk_report(balance, risk_percent, entry, stop_loss):

    risk_amount = calculate_risk(balance, risk_percent)

    stop_distance = calculate_stop_distance(
        entry,
        stop_loss
    )

    return f"""
💰 AlphaPilot Risk Manager

Balance: ${balance}

Risk: {risk_percent}%

Maximum Loss: ${risk_amount}

Entry: {entry}

Stop Loss: {stop_loss}

Stop Distance: {stop_distance}
"""
