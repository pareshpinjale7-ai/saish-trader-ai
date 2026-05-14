# ai_score_engine.py

# =========================
# AI SCORE
# =========================

def calculate_ai_score(

    probability,
    rfact,
    momentum,
    sustain

):

    score = 0

    score += probability / 10
    score += abs(rfact)
    score += abs(momentum) * 2
    score += sustain

    return round(score, 2)