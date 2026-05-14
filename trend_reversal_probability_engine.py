# trend_reversal_probability_engine.py

# =========================
# REVERSAL PROBABILITY
# =========================

def calculate_reversal_probability(

    rsi,
    momentum

):

    probability = 0

    if rsi >= 75:

        probability += 40

    if rsi <= 25:

        probability += 40

    if abs(momentum) >= 3:

        probability += 30

    return min(

        probability,

        100

    )