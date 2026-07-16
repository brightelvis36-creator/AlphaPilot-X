from multi_timeframe import analyze_multi_timeframe
from signal_engine import generate_signal
from market_feed import get_price
from candles import get_candles
from trade_setup import calculate_trade_setup
from risk_manager import calculate_risk, calculate_lot_size, calculate_pips


def generate_trade_plan(
    pair,
    timeframe="15m",
    balance=1000,
    risk_percent=2
):

    elite = analyze_multi_timeframe(pair)

    strategy = elite["entry_15m"]

    market = get_price(pair)

    if market["price"] == "Unavailable":
        return "❌ Live market unavailable."

    price = float(market["price"])

    if elite["decision"] == "WAIT":
        return f"""
📡 AlphaPilot Elite Trade Plan

Pair: {pair}

4H Trend:
{elite["trend_4h"]["signal"]}

1H Confirmation:
{elite["confirmation_1h"]["signal"]}

15M Entry:
{elite["entry_15m"]["signal"]}

Decision:
WAIT ⏳

Confidence:
{elite["confidence"]}%

Setup:
{elite["setup"]}

Reason:
Waiting for stronger confirmation.
"""

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
📡 AlphaPilot Elite Trade Plan

Pair: {pair}

4H Trend:
{elite["trend_4h"]["signal"]}

1H Confirmation:
{elite["confirmation_1h"]["signal"]}

15M Entry:
{elite["entry_15m"]["signal"]}

🔥 Decision:
{elite["decision"]}

Confidence:
{elite["confidence"]}%

Setup:
{elite["setup"]}

Entry:
{setup["entry"]}

Stop Loss:
{setup["stop_loss"]}

Take Profit:
{setup["take_profit"]}

Balance:
${balance}

Risk:
{risk_percent}%

Maximum Loss:
${risk_amount}

Suggested Lot Size:
{lot_size}

Risk Reward:
{setup["risk_reward"]}

Reason:
• {strategy["reason"].replace(", ", "\n• ")}
"""
