from signal_engine import generate_signal
from strategy import analyze_strategy
from market_feed import get_price
from candles import get_candles
from trade_setup import calculate_trade_setup
from risk_manager import calculate_risk, calculate_lot_size, calculate_pips


def generate_trade_plan(
    pair,
    timeframe="1h",
    balance=1000,
    risk_percent=2
):

    market = get_price(pair)

    if market["price"] == "Unavailable":
        return "❌ Live market unavailable."

    price = float(market["price"])

    strategy = analyze_strategy(pair, timeframe)

    if strategy["signal"] == "WAIT":
        return generate_signal(pair)

    candles = get_candles(pair, timeframe)

    setup = calculate_trade_setup(
        pair,
        strategy["signal"],
        price,
        candles
    )

    risk_amount = calculate_risk(
        balance,
        risk_percent
    )

    stop_pips = calculate_pips(
        setup["entry"],
        setup["stop_loss"]
    )

    lot_size = calculate_lot_size(
        risk_amount,
        stop_pips
    )

    return f"""
📡 AlphaPilot Trade Plan

Pair: {pair}

Timeframe: {timeframe}

Signal: {strategy["signal"]}

Confidence: {strategy["confidence"]}%

Setup: {strategy["setup"]}

Entry: {setup["entry"]}

Stop Loss: {setup["stop_loss"]}

Take Profit: {setup["take_profit"]}

Balance: ${balance}

Risk: {risk_percent}%

Maximum Loss: ${risk_amount}

Suggested Lot Size: {lot_size}

Risk Reward: {setup["risk_reward"]}

Reason:
• {strategy["reason"].replace(", ", "\n• ")}
"""
