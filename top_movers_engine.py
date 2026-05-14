# top_movers_engine.py

from live_cache import (
    live_market_data
)

from market_memory_engine import (

    get_move_percent,
    get_market_trend,
    get_breakout_time

)

# =========================
# TOP MOVERS
# =========================

def get_top_movers():

    movers = []

    for symbol, data in live_market_data.items():

        ltp = data.get(

            "ltp",

            0

        )

        # =====================
        # REAL MOVE %
        # =====================

        move = get_move_percent(

            symbol

        )

        # =====================
        # TREND
        # =====================

        trend = get_market_trend(

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
        # SKIP INVALID
        # =====================

        if ltp <= 0:

            continue

        movers.append({

            "symbol": symbol,

            "ltp": round(

                ltp,

                2

            ),

            "move": round(

                move,

                2

            ),

            "trend": trend,

            "breakout_time":

            breakout_time

        })

    # =========================
    # SORT BY MOVE
    # =========================

    movers = sorted(

        movers,

        key=lambda x:

        abs(

            x["move"]

        ),

        reverse=True

    )

    return movers[:20]