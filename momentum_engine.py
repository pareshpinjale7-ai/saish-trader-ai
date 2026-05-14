# momentum_engine.py

from timeframe_store import candles_1m

# =========================
# MOMENTUM SCORE
# =========================

def calculate_momentum(symbol):

    if symbol not in candles_1m:

        return 0

    candles = list(

        candles_1m[symbol].values()

    )

    if len(candles) < 5:

        return 0

    first = candles[-5]["close"]

    last = candles[-1]["close"]

    if first == 0:

        return 0

    momentum = (

        (last - first)

        / first

    ) * 100

    return round(

        momentum,

        2

    )