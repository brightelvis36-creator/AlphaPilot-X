from market_structure import detect_structure
from bos import detect_bos
from choch import detect_choch
from liquidity import detect_liquidity
from order_block import detect_order_block
from fvg import detect_fvg


def analyze_smart_money(candles):

    structure = detect_structure(candles)
    bos = detect_bos(candles)
    choch = detect_choch(candles)
    liquidity = detect_liquidity(candles)
    order_block = detect_order_block(candles)
    fvg = detect_fvg(candles)

    score = 0
    reasons = []

    # Market Structure
    if structure.get("structure") == "BULLISH":
        score += 20
        reasons.append("Bullish market structure")

    elif structure.get("structure") == "BEARISH":
        score -= 20
        reasons.append("Bearish market structure")


    # Break of Structure
    if bos.get("bos") == "BULLISH BOS":
        score += 25
        reasons.append("Bullish BOS")

    elif bos.get("bos") == "BEARISH BOS":
        score -= 25
        reasons.append("Bearish BOS")


    # Change of Character
    if choch.get("choch") == "BULLISH CHOCH":
        score += 30
        reasons.append("Bullish CHOCH")

    elif choch.get("choch") == "BEARISH CHOCH":
        score -= 30
        reasons.append("Bearish CHOCH")


    # Order Block
    if order_block.get("order_block") == "BULLISH ORDER BLOCK":
        score += 15
        reasons.append("Bullish Order Block")

    elif order_block.get("order_block") == "BEARISH ORDER BLOCK":
        score -= 15
        reasons.append("Bearish Order Block")


    # Liquidity
    if liquidity.get("liquidity") == "BUY SIDE LIQUIDITY":
        score += 10
        reasons.append("Buy side liquidity")

    elif liquidity.get("liquidity") == "SELL SIDE LIQUIDITY":
        score -= 10
        reasons.append("Sell side liquidity")


    # Fair Value Gap
    if fvg.get("fvg") == "BULLISH FVG":
        score += 10
        reasons.append("Bullish FVG")

    elif fvg.get("fvg") == "BEARISH FVG":
        score -= 10
        reasons.append("Bearish FVG")


    # Final Decision
    if score >= 40:
        decision = "BUY"

    elif score <= -40:
        decision = "SELL"

    else:
        decision = "WAIT"


    confidence = min(abs(score) + 50, 95)


    return {
        "decision": decision,
        "confidence": confidence,
        "score": score,
        "structure": structure,
        "bos": bos,
        "choch": choch,
        "liquidity": liquidity,
        "order_block": order_block,
        "fvg": fvg,
        "reason": ", ".join(reasons)
    }
