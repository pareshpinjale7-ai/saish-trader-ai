# liquidity_engine.py

# =========================
# LIQUIDITY SCORE
# =========================

def calculate_liquidity(

    volume

):

    if volume >= 50000000:

        return "ULTRA HIGH"

    if volume >= 10000000:

        return "HIGH"

    if volume >= 1000000:

        return "MEDIUM"

    return "LOW"