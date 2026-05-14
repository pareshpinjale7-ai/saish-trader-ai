# market_snapshot_engine.py

import json
import os

from datetime import datetime

# =========================
# SNAPSHOT FILE
# =========================

SNAPSHOT_FILE = "market_snapshot.json"

# =========================
# SNAPSHOT DATA
# =========================

market_snapshot = {}

# =========================
# SAVE SNAPSHOT
# =========================

def save_market_snapshot():

    with open(
        SNAPSHOT_FILE,
        "w"
    ) as f:

        json.dump(

            market_snapshot,

            f,

            indent=4

        )

# =========================
# LOAD SNAPSHOT
# =========================

def load_market_snapshot():

    global market_snapshot

    if not os.path.exists(
        SNAPSHOT_FILE
    ):

        market_snapshot = {}

        return

    try:

        with open(
            SNAPSHOT_FILE,
            "r"
        ) as f:

            market_snapshot = json.load(
                f
            )

        print(
            "MARKET SNAPSHOT LOADED"
        )

    except:

        market_snapshot = {}

# =========================
# SAVE STOCK SNAPSHOT
# =========================

def save_stock_snapshot(

    symbol,
    ltp,
    volume=0,
    sector="UNKNOWN"

):

    # =====================
    # ALREADY EXISTS
    # =====================

    if symbol in market_snapshot:

        return

    # =====================
    # SAVE DATA
    # =====================

    market_snapshot[symbol] = {

        "reference_price": ltp,

        "volume": volume,

        "sector": sector,

        "time":

        datetime.now().strftime(
            "%H:%M"
        )

    }

    # =====================
    # SAVE FILE
    # =====================

    save_market_snapshot()

    print(
        f"SNAPSHOT SAVED: {symbol}"
    )

# =========================
# GET SNAPSHOT
# =========================

def get_stock_snapshot(symbol):

    return market_snapshot.get(
        symbol,
        {}
    )

# =========================
# GET REFERENCE PRICE
# =========================

def get_reference_price(symbol):

    stock = market_snapshot.get(
        symbol,
        {}
    )

    return stock.get(
        "reference_price",
        None
    )

# =========================
# AUTO LOAD ON START
# =========================

load_market_snapshot()