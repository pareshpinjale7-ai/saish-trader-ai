# orb_engine.py

from opening_memory import opening_memory

# =========================
# ORB CHECK
# =========================

def check_orb_breakout(

    symbol,

    ltp

):

    if symbol not in opening_memory:

        return {

            "signal": "NO DATA"

        }

    data = opening_memory[symbol]

    opening_high = data["opening_high"]
    opening_low = data["opening_low"]

    if ltp > opening_high:

        return {

            "signal":

            "ORB BULLISH"

        }

    if ltp < opening_low:

        return {

            "signal":

            "ORB BEARISH"

        }

    return {

        "signal":

        "INSIDE RANGE"

    }