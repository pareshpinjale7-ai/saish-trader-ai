# market_history_engine.py

import json
import os

from datetime import datetime

# =========================
# HISTORY FILE
# =========================

HISTORY_FILE = "market_history.json"

# =========================
# MARKET HISTORY
# =========================

market_history = {}

# =========================
# LOAD HISTORY
# =========================

def load_market_history():

    global market_history

    if not os.path.exists(
        HISTORY_FILE
    ):

        market_history = {}

        return

    try:

        with open(
            HISTORY_FILE,
            "r"
        ) as f:

            market_history = json.load(
                f
            )

        print(
            "MARKET HISTORY LOADED"
        )

    except:

        market_history = {}

# =========================
# SAVE HISTORY
# =========================

def save_market_history():

    with open(
        HISTORY_FILE,
        "w"
    ) as f:

        json.dump(

            market_history,

            f,

            indent=4

        )

# =========================
# SAVE STOCK HISTORY
# =========================

def save_stock_history(

    symbol,
    ltp,
    volume=0,
    move=0,
    rfact=0,
    trend="SIDEWAYS",
    signal="NONE"

):

    # =====================
    # INIT SYMBOL
    # =====================

    if symbol not in market_history:

        market_history[symbol] = []

    # =====================
    # CURRENT TIME
    # =====================

    current_time = (

        datetime.now().strftime(
            "%H:%M:%S"
        )

    )

    # =====================
    # PREVENT DUPLICATE
    # =====================

    if len(
        market_history[symbol]
    ) > 0:

        last_entry = (
            market_history[symbol][-1]
        )

        if (

            last_entry["time"]

            ==

            current_time

        ):

            return

    # =====================
    # SAVE ENTRY
    # =====================

    market_history[symbol].append({

        "time": current_time,

        "ltp": ltp,

        "volume": volume,

        "move": move,

        "rfact": rfact,

        "trend": trend,

        "signal": signal

    })

    # =====================
    # LIMIT MEMORY
    # =====================

    if len(
        market_history[symbol]
    ) > 5000:

        market_history[symbol] = (

            market_history[symbol][-5000:]

        )

    # =====================
    # SAVE FILE
    # =====================

    save_market_history()

# =========================
# GET STOCK HISTORY
# =========================

def get_stock_history(symbol):

    return market_history.get(
        symbol,
        []
    )

# =========================
# GET FULL HISTORY
# =========================

def get_full_market_history():

    return market_history

# =========================
# CLEAR HISTORY
# =========================

def clear_market_history():

    global market_history

    market_history = {}

    save_market_history()

# =========================
# AUTO LOAD
# =========================

load_market_history()