# breakout_signal_engine.py

# =========================
# FINAL BREAKOUT SIGNAL
# =========================

def generate_breakout_signal(

    rfact,
    probability,
    smart_money

):

    if (

        rfact >= 7

        and

        probability >= 70

        and

        smart_money ==

        "SMART BUYING"

    ):

        return "STRONG BUY"

    if (

        rfact <= -7

        and

        probability >= 70

        and

        smart_money ==

        "SMART SELLING"

    ):

        return "STRONG SELL"

    return "WAIT"