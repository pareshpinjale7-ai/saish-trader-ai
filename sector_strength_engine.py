# sector_strength_engine.py

from sector_map import SECTOR_MAP

from market_memory_engine import (
    get_move_percent
)

# =========================
# LIVE SECTOR STRENGTH
# =========================

sector_strength_data = {}

# =========================
# CALCULATE STRENGTH
# =========================

def calculate_sector_strength():

    global sector_strength_data

    sector_strength_data = {}

    # =====================
    # LOOP SECTORS
    # =====================

    for sector, stocks in SECTOR_MAP.items():

        total_move = 0

        count = 0

        # =================
        # LOOP STOCKS
        # =================

        for symbol in stocks:

            move = get_move_percent(
                symbol
            )

            total_move += move

            count += 1

        # =================
        # AVG MOVE
        # =================

        avg_move = 0

        if count > 0:

            avg_move = round(

                total_move / count,

                2

            )

        # =================
        # TREND
        # =================

        if avg_move > 0:

            trend = "BULLISH"

        elif avg_move < 0:

            trend = "BEARISH"

        else:

            trend = "SIDEWAYS"

        # =================
        # SAVE
        # =================

        sector_strength_data[sector] = {

            "strength": avg_move,

            "trend": trend,

            "stock_count": count

        }

    return sector_strength_data

# =========================
# GET DATA
# =========================

def get_sector_strength():

    return sector_strength_data

# =========================
# TOP SECTOR
# =========================

def get_top_sector():

    if not sector_strength_data:

        return {}

    return max(

        sector_strength_data.items(),

        key=lambda x:

        x[1]["strength"]

    )

# =========================
# WEAK SECTOR
# =========================

def get_weak_sector():

    if not sector_strength_data:

        return {}

    return min(

        sector_strength_data.items(),

        key=lambda x:

        x[1]["strength"]

    )