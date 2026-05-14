# distribution_engine.py

from timeframe_store import candles_5m

# =========================
# DISTRIBUTION PHASE
# =========================

def detect_distribution(

    symbol

):

    if symbol not in candles_5m:

        return False

    candles = list(

        candles_5m[symbol].values()

    )

    if len(candles) < 5:

        return False

    bearish = 0

    for candle in candles[-5:]:

        if (

            candle["close"]

            <

            candle["open"]

        ):

            bearish += 1

    return bearish >= 4