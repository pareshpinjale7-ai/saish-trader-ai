# consolidation_engine.py

from timeframe_store import candles_5m

# =========================
# CONSOLIDATION
# =========================

def detect_consolidation(

    symbol

):

    if symbol not in candles_5m:

        return False

    candles = list(

        candles_5m[symbol].values()

    )

    if len(candles) < 5:

        return False

    highs = [

        c["high"]

        for c in candles[-5:]

    ]

    lows = [

        c["low"]

        for c in candles[-5:]

    ]

    high_range = (

        max(highs)

        - min(highs)

    )

    low_range = (

        max(lows)

        - min(lows)

    )

    avg_price = sum(highs) / len(highs)

    if avg_price == 0:

        return False

    consolidation_range = (

        (high_range + low_range)

        / avg_price

    ) * 100

    return consolidation_range < 1.5