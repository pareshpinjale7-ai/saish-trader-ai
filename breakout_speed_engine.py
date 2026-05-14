# breakout_speed_engine.py

from timeframe_store import candles_1m

# =========================
# BREAKOUT SPEED
# =========================

def calculate_breakout_speed(

    symbol

):

    if symbol not in candles_1m:

        return 0

    candles = list(

        candles_1m[symbol].values()

    )

    if len(candles) < 3:

        return 0

    first = candles[-3]["close"]
    last = candles[-1]["close"]

    if first == 0:

        return 0

    speed = (

        (last - first)

        / first

    ) * 100

    return round(speed, 2)