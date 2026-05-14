# structure_engine.py

from timeframe_store import candles_5m

# =========================
# MARKET STRUCTURE
# =========================

def detect_structure(symbol):

    if symbol not in candles_5m:

        return "NO DATA"

    candles = list(

        candles_5m[symbol].values()

    )

    if len(candles) < 3:

        return "NO DATA"

    c1 = candles[-3]
    c2 = candles[-2]
    c3 = candles[-1]

    # =====================
    # HIGHER HIGH
    # =====================

    if (

        c3["high"] > c2["high"]

        and

        c2["high"] > c1["high"]

    ):

        return "HH_HL"

    # =====================
    # LOWER LOW
    # =====================

    if (

        c3["low"] < c2["low"]

        and

        c2["low"] < c1["low"]

    ):

        return "LH_LL"

    return "RANGE"