# market_depth_engine.py

# =========================
# BID ASK ANALYSIS
# =========================

def analyze_market_depth(

    bid_qty,

    ask_qty

):

    if ask_qty == 0:

        return {

            "ratio": 0,

            "signal": "NO DATA"

        }

    ratio = (

        bid_qty / ask_qty

    )

    signal = "NEUTRAL"

    if ratio > 1.5:

        signal = "BUYER DOMINANCE"

    elif ratio < 0.7:

        signal = "SELLER DOMINANCE"

    return {

        "ratio": round(

            ratio,

            2

        ),

        "signal": signal

    }