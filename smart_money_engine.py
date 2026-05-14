# smart_money_engine.py

from volume_engine import (
    calculate_relative_volume
)

from momentum_engine import (
    calculate_momentum
)

# =========================
# SMART MONEY FLOW
# =========================

def detect_smart_money(

    symbol

):

    rel_volume = (

        calculate_relative_volume(

            symbol

        )

    )

    momentum = (

        calculate_momentum(

            symbol

        )

    )

    # =====================
    # STRONG BUYING
    # =====================

    if (

        rel_volume > 2

        and

        momentum > 1

    ):

        return {

            "signal":

            "SMART BUYING"

        }

    # =====================
    # STRONG SELLING
    # =====================

    if (

        rel_volume > 2

        and

        momentum < -1

    ):

        return {

            "signal":

            "SMART SELLING"

        }

    return {

        "signal":

        "NEUTRAL"

    }