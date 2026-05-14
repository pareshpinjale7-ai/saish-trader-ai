# price_speed_engine.py

from timeframe_store import candles_1m

# =========================
# PRICE SPEED
# =========================

def calculate_price_speed(

    symbol

):

    if symbol not in candles_1m:

        return 0

    candles = list(

        candles_1m[symbol].values()

    )

    if len(candles) < 2:

        return 0

    first = candles[-2]["close"]

    last = candles[-1]["close"]

    if first == 0:

        return 0

    speed = (

        (last - first)

        / first

    ) * 100

    return round(

        speed,

        2

    )