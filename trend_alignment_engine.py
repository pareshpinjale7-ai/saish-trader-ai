# trend_alignment_engine.py

# =========================
# MULTI TF ALIGNMENT
# =========================

def check_trend_alignment(

    momentum,
    vwap_signal,
    structure

):

    bullish = (

        momentum > 0

        and

        vwap_signal == "ABOVE VWAP"

        and

        structure == "HH_HL"

    )

    bearish = (

        momentum < 0

        and

        vwap_signal == "BELOW VWAP"

        and

        structure == "LH_LL"

    )

    if bullish:

        return "BULLISH ALIGNMENT"

    if bearish:

        return "BEARISH ALIGNMENT"

    return "NO ALIGNMENT"