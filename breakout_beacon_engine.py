# breakout_beacon_engine.py

from live_cache import (
    live_market_data
)

from vwap_engine import (
    get_vwap_signal
)

from orb_engine import (
    check_orb_breakout
)

from structure_engine import (
    detect_structure
)

from momentum_engine import (
    calculate_momentum
)

from rsi_engine import (
    calculate_rsi
)

from rfactor_engine import (
    calculate_rfactor
)

# =========================
# BREAKOUT BEACON
# =========================

def get_breakout_beacon():

    result = []

    for symbol, data in live_market_data.items():

        ltp = data.get(

            "ltp",

            0

        )

        if ltp <= 0:

            continue

        # =====================
        # ENGINES
        # =====================

        vwap_data = (

            get_vwap_signal(

                symbol,

                ltp

            )

        )

        orb_data = (

            check_orb_breakout(

                symbol,

                ltp

            )

        )

        structure = (

            detect_structure(

                symbol

            )

        )

        momentum = (

            calculate_momentum(

                symbol

            )

        )

        rsi = (

            calculate_rsi(

                symbol

            )

        )

        # =====================
        # RFACTOR
        # =====================

        rfact = (

            calculate_rfactor(

                vwap_data["signal"],
                orb_data["signal"],
                structure,
                momentum,
                rsi

            )

        )

        # =====================
        # CHANGE %
        # =====================

        change = data.get(

            "change_percent",

            0

        )

        # =====================
        # FINAL
        # =====================

        result.append({

            "symbol": symbol,

            "ltp": round(

                ltp,

                2

            ),

            "percent_change": round(

                change,

                2

            ),

            "time": "LIVE",

            "chart":

            f"https://www.tradingview.com/chart/?symbol=NSE:{symbol}",

            "rfact": rfact,

            "vwap":

            vwap_data["signal"],

            "orb":

            orb_data["signal"],

            "structure":

            structure,

            "momentum":

            momentum,

            "rsi": rsi

        })

    result = sorted(

        result,

        key=lambda x:

        abs(

            x["rfact"]

        ),

        reverse=True

    )

    return result[:20]