# imbalance_engine.py

from timeframe_store import candles_1m

# =========================
# IMBALANCE
# =========================

def detect_imbalance(

    symbol

):

    if symbol not in candles_1m:

        return {

            "signal": "NO DATA"

        }

    candles = list(

        candles_1m[symbol].values()

    )

    if len(candles) < 2:

        return {

            "signal": "NO DATA"

        }

    current = candles[-1]

    prev = candles[-2]

    current_range = (

        current["high"]

        - current["low"]

    )

    prev_range = (

        prev["high"]

        - prev["low"]

    )

    if prev_range == 0:

        return {

            "signal": "NO DATA"

        }

    ratio = (

        current_range / prev_range

    )

    if ratio >= 2:

        return {

            "signal":

            "HIGH IMBALANCE"

        }

    return {

        "signal":

        "NORMAL"

    }