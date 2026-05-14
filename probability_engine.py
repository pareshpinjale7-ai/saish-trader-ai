# probability_engine.py

# =========================
# BREAKOUT PROBABILITY
# =========================

def calculate_probability(

    rfact,
    momentum,
    rsi,
    rel_volume

):

    probability = 0

    # =====================
    # RFACTOR
    # =====================

    probability += abs(rfact) * 5

    # =====================
    # MOMENTUM
    # =====================

    probability += abs(momentum) * 10

    # =====================
    # RSI
    # =====================

    if rsi > 60:

        probability += 10

    elif rsi < 40:

        probability += 10

    # =====================
    # RELATIVE VOLUME
    # =====================

    probability += rel_volume * 5

    probability = min(

        probability,

        100

    )

    return round(

        probability,

        2

    )