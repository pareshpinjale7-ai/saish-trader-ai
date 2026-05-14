# breakout_strength_engine.py

# =========================
# BREAKOUT STRENGTH
# =========================

def calculate_breakout_strength(

    rfact,
    rel_volume,
    momentum,
    probability

):

    strength = 0

    strength += abs(rfact) * 2

    strength += rel_volume * 5

    strength += abs(momentum) * 5

    strength += probability / 10

    return round(

        strength,

        2

    )