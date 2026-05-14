# high_low_break_engine.py

from timeframe_store import candles_15m

# =========================
# HIGH LOW BREAK
# =========================

def detect_high_low_break(

    symbol

):

    if symbol not in candles_15m:

        return {

            "signal": "NO DATA"

        }

    candles = list(

        candles_15m[symbol].values()

    )

    if len(candles) < 20:

        return {

            "signal": "NO DATA"

        }

    highs = [

        c["high"]

        for c in candles[-20:]

    ]

    lows = [

        c["low"]

        for c in candles[-20:]

    ]

    latest = candles[-1]["close"]

    if latest >= max(highs):

        return {

            "signal":

            "20D HIGH BREAK"

        }

    if latest <= min(lows):

        return {

            "signal":

            "20D LOW BREAK"

        }

    return {

        "signal":

        "NO BREAK"

    }