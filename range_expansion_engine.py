# range_expansion_engine.py

from timeframe_store import candles_5m

# =========================
# RANGE EXPANSION
# =========================

def detect_range_expansion(

    symbol

):

    if symbol not in candles_5m:

        return False

    candles = list(

        candles_5m[symbol].values()

    )

    if len(candles) < 3:

        return False

    current = candles[-1]

    prev = candles[-2]

    current_range = (

        current["high"]

        - current["low"]

    )

    prev_range = (

        prev["high"]

        - prev["low"]

    )

    return current_range > (

        prev_range * 1.5

    )