# intraday_boost_engine.py

from breakout_beacon_engine import (
    get_breakout_beacon
)

# =========================
# INTRADAY BOOST
# =========================

def get_intraday_boost():

    data = (

        get_breakout_beacon()

    )

    result = []

    for stock in data:

        # =====================
        # SUSTAIN FILTER
        # =====================

        if (

            abs(stock["rfact"])

            >= 6

            and

            abs(stock["momentum"])

            >= 1

        ):

            result.append({

                "symbol":

                stock["symbol"],

                "ltp":

                stock["ltp"],

                "move":

                stock["percent_change"],

                "rfact":

                stock["rfact"],

                "chart":

                stock["chart"]

            })

    return result[:20]