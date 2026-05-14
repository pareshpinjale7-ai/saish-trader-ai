# scoring_engine.py

# =========================
# FINAL SCORE
# =========================

def calculate_final_score(

    trend_score,
    probability,
    breakout_quality,
    sustain_score

):

    score = 0

    score += trend_score
    score += probability / 5
    score += breakout_quality
    score += sustain_score

    return round(score, 2)