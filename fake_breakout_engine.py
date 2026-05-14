# fake_breakout_engine.py

# =========================
# FAKE BREAKOUT FILTER
# =========================

def detect_fake_breakout(

    rel_volume,
    momentum,
    probability

):

    if (

        rel_volume < 1

        and

        abs(momentum) < 0.5

        and

        probability < 40

    ):

        return True

    return False