# directional_strength_engine.py

# =========================
# DIRECTIONAL STRENGTH
# =========================

def calculate_directional_strength(

    bullish,
    bearish

):

    total = bullish + bearish

    if total == 0:

        return 0

    strength = abs(

        bullish - bearish

    ) / total * 100

    return round(

        strength,

        2

    )