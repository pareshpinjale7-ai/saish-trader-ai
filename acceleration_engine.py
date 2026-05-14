# acceleration_engine.py

from timeframe_store import candles_1m

# =========================
# PRICE ACCELERATION
# =========================

def calculate_acceleration(

    symbol

):

    if symbol not in candles_1m:

        return 0

    candles = list(

        candles_1m[symbol].values()

    )

    if len(candles) < 3:

        return 0

    move1 = (

        candles[-2]["close"]

        - candles[-3]["close"]

    )

    move2 = (

        candles[-1]["close"]

        - candles[-2]["close"]

    )

    acceleration = (

        move2 - move1

    )

    return round(

        acceleration,

        2

    )