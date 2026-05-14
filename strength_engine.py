# strength_engine.py

# =========================
# FINAL STRENGTH
# =========================

def calculate_strength(

    probability,
    breakout_quality,
    sustain_score

):

    strength = 0

    strength += probability / 10

    strength += breakout_quality

    strength += sustain_score

    return round(

        strength,

        2

    )