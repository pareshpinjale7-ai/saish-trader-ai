# recovery_engine.py

from timeframe_store import candles_5m

# =========================
# RECOVERY FROM LOW
# =========================

def detect_recovery(

    symbol

):

    if symbol not in candles_5m:

        return False

    candles = list(

        candles_5m[symbol].values()

    )

    if len(candles) < 5:

        return False

    lows = [

        c["low"]

        for c in candles[-5:]

    ]

    closes = [

        c["close"]

        for c in candles[-5:]

    ]

    recent_low = min(lows)

    latest_close = closes[-1]

    if recent_low == 0:

        return False

    recovery = (

        (latest_close - recent_low)

        / recent_low

    ) * 100

    return recovery >= 2