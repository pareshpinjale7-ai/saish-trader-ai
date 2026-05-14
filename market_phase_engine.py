# market_phase_engine.py

# =========================
# MARKET PHASE
# =========================

def detect_market_phase(

    bullish,
    bearish

):

    total = bullish + bearish

    if total == 0:

        return "SIDEWAYS"

    bullish_ratio = (

        bullish / total

    ) * 100

    if bullish_ratio >= 70:

        return "STRONG BULL"

    if bullish_ratio <= 30:

        return "STRONG BEAR"

    return "RANGE MARKET"