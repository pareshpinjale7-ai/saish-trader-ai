# trend_score_engine.py

# =========================
# TREND SCORE
# =========================

def calculate_trend_score(

    momentum,
    structure,
    vwap_signal

):

    score = 0

    if momentum > 0:

        score += 3
    else:

        score -= 3

    if structure == "HH_HL":

        score += 3

    elif structure == "LH_LL":

        score -= 3

    if vwap_signal == "ABOVE VWAP":

        score += 4

    elif vwap_signal == "BELOW VWAP":

        score -= 4

    return score