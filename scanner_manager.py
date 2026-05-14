# scanner_manager.py

from live_cache import (
    live_market_data
)

from daily_top_gainers_engine import (
    save_daily_top_3
)

from market_memory_engine import (

    get_move_percent,
    get_breakout_time,
    get_market_trend,
    is_scanner_active

)

# =========================
# BREAKOUT BEACON
# =========================

def get_breakout_data():

    breakout_data = []

    # =====================
    # WAIT FOR 9:20
    # =====================

    if not is_scanner_active():
        return []

    for symbol, data in live_market_data.items():

        # =====================
        # LIVE DATA
        # =====================

        ltp = data.get(
            "ltp",
            0
        )

        volume = data.get(
            "volume",
            0
        )

        # =====================
        # REAL MOVE %
        # =====================

        change = get_move_percent(
            symbol
        )

        # =====================
        # BREAKOUT TIME
        # =====================

        breakout_time = (
            get_breakout_time(
                symbol
            )
        )

        # =====================
        # TREND
        # =====================

        trend = get_market_trend(
            symbol
        )

        # =====================
        # SKIP INVALID
        # =====================

        if ltp <= 0:
            continue

        # =====================
        # R FACTOR
        # =====================

        rfact = round(
            abs(change) * 2,
            2
        )

        # =====================
        # SIGNAL
        # =====================

        signal = "BULLISH"

        if change < 0:
            signal = "BEARISH"

        # =====================
        # APPEND
        # =====================

        breakout_data.append({

            "symbol": symbol,

            "ltp": round(
                ltp,
                2
            ),

            "percent_change": round(
                change,
                2
            ),

            "time": breakout_time,

            "chart":
            f"https://www.tradingview.com/chart/?symbol=NSE:{symbol}",

            "rfact": rfact,

            "signal": signal,

            "trend": trend,

            "volume": volume

        })

    # =========================
    # SORT
    # =========================

    breakout_data = sorted(

        breakout_data,

        key=lambda x: abs(
            x["percent_change"]
        ),

        reverse=True

    )

    return breakout_data[:20]

    save_daily_top_3(
        breakout_stocks
    )

# =========================
# INTRADAY BOOST
# =========================

def get_intraday_boost():

    boost_data = []

    # =====================
    # WAIT FOR 9:20
    # =====================

    if not is_scanner_active():
        return []

    for symbol, data in live_market_data.items():

        # =====================
        # LIVE DATA
        # =====================

        ltp = data.get(
            "ltp",
            0
        )

        volume = data.get(
            "volume",
            0
        )

        # =====================
        # REAL MOVE %
        # =====================

        move = get_move_percent(
            symbol
        )

        # =====================
        # BREAKOUT TIME
        # =====================

        breakout_time = (
            get_breakout_time(
                symbol
            )
        )

        # =====================
        # TREND
        # =====================

        trend = get_market_trend(
            symbol
        )

        # =====================
        # SKIP INVALID
        # =====================

        if ltp <= 0:
            continue

        # =====================
        # R FACTOR
        # =====================

        rfact = round(
            abs(move) * 2,
            2
        )

        # =====================
        # APPEND
        # =====================

        boost_data.append({

            "symbol": symbol,

            "ltp": round(
                ltp,
                2
            ),

            "move": round(
                move,
                2
            ),

            "time": breakout_time,

            "trend": trend,

            "rfact": rfact,

            "chart":
            f"https://www.tradingview.com/chart/?symbol=NSE:{symbol}",

            "signal": "BOOST",

            "volume": volume

        })

    # =========================
    # SORT
    # =========================

    boost_data = sorted(

        boost_data,

        key=lambda x: abs(
            x["move"]
        ),

        reverse=True

    )

    return boost_data[:20]