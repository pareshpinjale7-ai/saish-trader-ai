# breakout_quality_engine.py

# =========================
# BREAKOUT QUALITY
# =========================

def calculate_breakout_quality(

    probability,
    sustain_score,
    rel_volume,
    momentum

):

    quality = 0

    quality += probability / 10

    quality += sustain_score

    quality += rel_volume * 2

    quality += abs(momentum)

    return round(

        quality,

        2

    )