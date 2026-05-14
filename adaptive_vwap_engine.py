# adaptive_vwap_engine.py

# =========================
# ADAPTIVE VWAP
# =========================

def adaptive_vwap_signal(

    ltp,
    vwap,
    momentum

):

    if vwap is None:

        return "NO DATA"

    if (

        ltp > vwap

        and

        momentum > 0

    ):

        return "STRONG ABOVE VWAP"

    if (

        ltp < vwap

        and

        momentum < 0

    ):

        return "STRONG BELOW VWAP"

    return "WEAK TREND"