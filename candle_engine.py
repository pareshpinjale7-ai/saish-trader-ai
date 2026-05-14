# candle_engine.py

from datetime import datetime

from timeframe_store import (

    candles_1m,
    candles_3m,
    candles_5m,
    candles_10m,
    candles_15m,
    candles_30m,
    MAX_CANDLES

)

# =========================
# GET TIMEFRAME KEY
# =========================

def get_time_bucket(

    timeframe

):

    now = datetime.now()

    minute = now.minute

    bucket = (

        minute // timeframe

    ) * timeframe

    return now.strftime(

        f"%Y-%m-%d %H:{bucket:02d}"

    )

# =========================
# CREATE / UPDATE CANDLE
# =========================

def update_candle(

    candle_store,

    symbol,

    timeframe,

    ltp,

    volume

):

    bucket = get_time_bucket(

        timeframe

    )

    # =====================
    # INIT SYMBOL
    # =====================

    if symbol not in candle_store:

        candle_store[symbol] = {}

    # =====================
    # NEW CANDLE
    # =====================

    if bucket not in candle_store[symbol]:

        candle_store[symbol][bucket] = {

            "time": bucket,

            "open": ltp,

            "high": ltp,

            "low": ltp,

            "close": ltp,

            "volume": volume

        }

    else:

        candle = candle_store[symbol][bucket]

        # =================
        # UPDATE CANDLE
        # =================

        candle["high"] = max(

            candle["high"],

            ltp

        )

        candle["low"] = min(

            candle["low"],

            ltp

        )

        candle["close"] = ltp

        candle["volume"] += volume

    # =====================
    # LIMIT STORAGE
    # =====================

    if len(

        candle_store[symbol]

    ) > MAX_CANDLES:

        oldest = sorted(

            candle_store[symbol]

        )[0]

        del candle_store[symbol][oldest]

# =========================
# MAIN CANDLE ENGINE
# =========================

def process_tick(

    symbol,

    ltp,

    volume

):

    # =====================
    # 1 MIN
    # =====================

    update_candle(

        candles_1m,

        symbol,

        1,

        ltp,

        volume

    )

    # =====================
    # 3 MIN
    # =====================

    update_candle(

        candles_3m,

        symbol,

        3,

        ltp,

        volume

    )

    # =====================
    # 5 MIN
    # =====================

    update_candle(

        candles_5m,

        symbol,

        5,

        ltp,

        volume

    )

    # =====================
    # 10 MIN
    # =====================

    update_candle(

        candles_10m,

        symbol,

        10,

        ltp,

        volume

    )

    # =====================
    # 15 MIN
    # =====================

    update_candle(

        candles_15m,

        symbol,

        15,

        ltp,

        volume

    )

    # =====================
    # 30 MIN
    # =====================

    update_candle(

        candles_30m,

        symbol,

        30,

        ltp,

        volume

    )