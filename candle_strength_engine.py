# candle_strength_engine.py

# =========================
# CANDLE STRENGTH
# =========================

def calculate_candle_strength(

    candle

):

    body = abs(

        candle["close"]

        - candle["open"]

    )

    range_size = abs(

        candle["high"]

        - candle["low"]

    )

    if range_size == 0:

        return 0

    strength = (

        body / range_size

    ) * 100

    return round(

        strength,

        2

    )