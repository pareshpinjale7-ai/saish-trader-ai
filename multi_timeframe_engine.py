# multi_timeframe_engine.py

from timeframe_store import (
    candles_1m,
    candles_5m,
    candles_15m
)

# =========================
# MULTI TF TREND
# =========================

def get_multi_tf_trend(

    symbol

):

    result = {}

    stores = {

        "1m": candles_1m,
        "5m": candles_5m,
        "15m": candles_15m

    }

    for tf, store in stores.items():

        if symbol not in store:

            result[tf] = "NO DATA"
            continue

        candles = list(

            store[symbol].values()

        )

        if len(candles) < 2:

            result[tf] = "NO DATA"
            continue

        prev_close = candles[-2]["close"]
        latest_close = candles[-1]["close"]

        if latest_close > prev_close:

            result[tf] = "UPTREND"

        elif latest_close < prev_close:

            result[tf] = "DOWNTREND"

        else:

            result[tf] = "SIDEWAYS"

    return result