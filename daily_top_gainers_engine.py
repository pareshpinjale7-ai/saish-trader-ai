# daily_top_gainers_engine.py

import json
import os

from datetime import datetime

# =========================
# FILE
# =========================

TOP_GAINERS_FILE = "daily_top_gainers.json"

# =========================
# STORAGE
# =========================

daily_top_data = {}

# =========================
# LOAD FILE
# =========================

def load_daily_top_data():

    global daily_top_data

    if not os.path.exists(
        TOP_GAINERS_FILE
    ):

        daily_top_data = {}

        return

    try:

        with open(
            TOP_GAINERS_FILE,
            "r"
        ) as f:

            daily_top_data = json.load(
                f
            )

        print(
            "TOP GAINERS HISTORY LOADED"
        )

    except:

        daily_top_data = {}

# =========================
# SAVE FILE
# =========================

def save_daily_top_data():

    with open(
        TOP_GAINERS_FILE,
        "w"
    ) as f:

        json.dump(

            daily_top_data,

            f,

            indent=4

        )

# =========================
# SAVE TOP 3
# =========================

def save_daily_top_3(

    breakout_data

):

    # =====================
    # DATE
    # =====================

    today = datetime.now().strftime(
        "%d-%m-%Y"
    )

    # =====================
    # SORT
    # =====================

    sorted_data = sorted(

        breakout_data,

        key=lambda x:

        x.get(
            "move_percent",
            0
        ),

        reverse=True

    )

    # =====================
    # TOP 3
    # =====================

    top_3 = sorted_data[:3]

    # =====================
    # FORMAT
    # =====================

    final_data = []

    for stock in top_3:

        final_data.append({

            "symbol":

            stock.get(
                "symbol",
                ""
            ),

            "ltp":

            stock.get(
                "ltp",
                0
            ),

            "move_percent":

            stock.get(
                "move_percent",
                0
            ),

            "r_factor":

            stock.get(
                "r_factor",
                0
            ),

            "chart":

            stock.get(
                "chart",
                "📈"
            )

        })

    # =====================
    # SAVE DATE
    # =====================

    daily_top_data[today] = (
        final_data
    )

    # =====================
    # SAVE FILE
    # =====================

    save_daily_top_data()

    print(
        f"TOP 3 SAVED: {today}"
    )

# =========================
# GET TODAY TOP
# =========================

def get_today_top():

    today = datetime.now().strftime(
        "%d-%m-%Y"
    )

    return daily_top_data.get(
        today,
        []
    )

# =========================
# GET ALL HISTORY
# =========================

def get_all_top_history():

    return daily_top_data

# =========================
# AUTO LOAD
# =========================

load_daily_top_data()