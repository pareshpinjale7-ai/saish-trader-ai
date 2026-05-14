# rfactor_engine.py

# =========================
# FINAL RFACTOR
# =========================

def calculate_rfactor(

    vwap_signal,
    orb_signal,
    structure,
    momentum,
    rsi

):

    score = 0

    # =====================
    # VWAP
    # =====================

    if (

        vwap_signal

        ==

        "ABOVE VWAP"

    ):

        score += 2

    else:

        score -= 2

    # =====================
    # ORB
    # =====================

    if (

        orb_signal

        ==

        "ORB BULLISH"

    ):

        score += 2

    elif (

        orb_signal

        ==

        "ORB BEARISH"

    ):

        score -= 2

    # =====================
    # STRUCTURE
    # =====================

    if structure == "HH_HL":

        score += 2

    elif structure == "LH_LL":

        score -= 2

    # =====================
    # MOMENTUM
    # =====================

    if momentum > 1:

        score += 2

    elif momentum < -1:

        score -= 2

    # =====================
    # RSI
    # =====================

    if rsi > 60:

        score += 2

    elif rsi < 40:

        score -= 2

    return round(score, 2)