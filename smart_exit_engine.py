# smart_exit_engine.py

# =========================
# SMART EXIT
# =========================

def detect_exit(

    momentum,
    rsi,
    reversal_signal

):

    if (

        momentum < -1

        and

        rsi < 40

    ):

        return "EXIT"

    if (

        reversal_signal

        ==

        "BEARISH REVERSAL"

    ):

        return "EXIT"

    return "HOLD"