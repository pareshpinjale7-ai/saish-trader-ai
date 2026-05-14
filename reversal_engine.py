# reversal_engine.py

from timeframe_store import candles_5m

# =========================
# REVERSAL DETECTOR
# =========================

def detect_reversal(symbol):

    if symbol not in candles_5m:

        return {

            "signal": "NO DATA"

        }

    candles = list(

        candles_5m[symbol].values()

    )

    if len(candles) < 3:

        return {

            "signal": "NO DATA"

        }

    c1 = candles[-3]
    c2 = candles[-2]
    c3 = candles[-1]

    # =====================
    # BULLISH REVERSAL
    # =====================

    if (

        c1["close"] < c1["open"]

        and

        c2["close"] < c2["open"]

        and

        c3["close"] > c3["open"]

    ):

        return {

            "signal":

            "BULLISH REVERSAL"

        }

    # =====================
    # BEARISH REVERSAL
    # =====================

    if (

        c1["close"] > c1["open"]

        and

        c2["close"] > c2["open"]

        and

        c3["close"] < c3["open"]

    ):

        return {

            "signal":

            "BEARISH REVERSAL"

        }

    return {

        "signal":

        "NO REVERSAL"

    }