# execution_engine.py

# =========================
# EXECUTION DECISION
# =========================

def get_execution_signal(

    probability,
    trend_score,
    breakout_quality

):

    total = (

        probability
        + trend_score
        + breakout_quality

    )

    if total >= 90:

        return "AGGRESSIVE BUY"

    if total >= 70:

        return "BUY"

    if total <= -90:

        return "AGGRESSIVE SELL"

    if total <= -70:

        return "SELL"

    return "WAIT"