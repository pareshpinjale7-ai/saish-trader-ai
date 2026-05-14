# smart_entry_engine.py

# =========================
# SMART ENTRY
# =========================

def detect_smart_entry(

    vwap_signal,
    orb_signal,
    structure,
    rel_volume

):

    bullish = (

        vwap_signal == "ABOVE VWAP"

        and

        orb_signal == "ORB BULLISH"

        and

        structure == "HH_HL"

        and

        rel_volume >= 1.5

    )

    bearish = (

        vwap_signal == "BELOW VWAP"

        and

        orb_signal == "ORB BEARISH"

        and

        structure == "LH_LL"

        and

        rel_volume >= 1.5

    )

    if bullish:

        return "SMART LONG"

    if bearish:

        return "SMART SHORT"

    return "WAIT"