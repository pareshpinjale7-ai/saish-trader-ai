# breakout_confirmation_engine.py

# =========================
# BREAKOUT CONFIRMATION
# =========================

def confirm_breakout(

    breakout_quality,
    trend_score,
    probability

):

    total = (

        breakout_quality

        + trend_score

        + probability

    )

    return total >= 80