# market_memory_engine.py

from datetime import datetime

from market_snapshot_engine import (

    save_stock_snapshot,
    get_reference_price

)

from market_history_engine import (

    save_stock_history

)

# =========================
# MARKET MEMORY
# =========================

market_memory = {}

# =========================
# SNAPSHOT TIME
# =========================

SNAPSHOT_START = "09:20"
SNAPSHOT_END = "09:21"

# =========================
# INIT STOCK MEMORY
# =========================

def init_stock(symbol):

    if symbol not in market_memory:

        market_memory[symbol] = {

            # =====================
            # REFERENCE PRICE
            # =====================

            "reference_price":

            get_reference_price(
                symbol
            ),

            # =====================
            # LIVE DATA
            # =====================

            "high": 0,

            "low": 999999,

            # =====================
            # MOVE %
            # =====================

            "move_percent": 0,

            # =====================
            # TREND
            # =====================

            "trend": "SIDEWAYS",

            # =====================
            # BREAKOUT
            # =====================

            "breakout_price": None,

            "breakout_time": None,

            # =====================
            # EXTREME MOVES
            # =====================

            "highest_move": 0,

            "lowest_move": 0,

            # =====================
            # UPDATE TIME
            # =====================

            "last_update": None

        }

# =========================
# UPDATE MARKET MEMORY
# =========================

def update_market_memory(

    symbol,
    ltp,
    volume=0,
    sector="UNKNOWN"

):

    # =====================
    # INIT
    # =====================

    init_stock(symbol)

    stock = market_memory[symbol]

    # =====================
    # CURRENT TIME
    # =====================

    now = datetime.now()

    current_time = now.strftime(
        "%H:%M"
    )

    # =====================
    # SAVE 9:20 SNAPSHOT
    # =====================

    if (

        SNAPSHOT_START <= current_time <= SNAPSHOT_END

        and

        stock["reference_price"] is None

    ):

        # =================
        # SAVE SNAPSHOT
        # =================

        save_stock_snapshot(

            symbol=symbol,
            ltp=ltp,
            volume=volume,
            sector=sector

        )

        # =================
        # LOAD REFERENCE
        # =================

        stock["reference_price"] = (

            get_reference_price(
                symbol
            )

        )

        print(

            f"REFERENCE LOCKED: "

            f"{symbol} = "

            f"{ltp}"

        )

    # =====================
    # WAIT FOR REFERENCE
    # =====================

    if stock["reference_price"] is None:

        return

    # =====================
    # UPDATE HIGH LOW
    # =====================

    stock["high"] = max(

        stock["high"],
        ltp

    )

    stock["low"] = min(

        stock["low"],
        ltp

    )

    # =====================
    # CALCULATE MOVE %
    # =====================

    reference_price = stock[
        "reference_price"
    ]

    if reference_price > 0:

        move_percent = round(

            (
                (
                    ltp -
                    reference_price
                )

                /

                reference_price

            ) * 100,

            2

        )

    else:

        move_percent = 0

    stock["move_percent"] = (
        move_percent
    )

    # =====================
    # STORE EXTREMES
    # =====================

    stock["highest_move"] = max(

        stock["highest_move"],
        move_percent

    )

    stock["lowest_move"] = min(

        stock["lowest_move"],
        move_percent

    )

    # =====================
    # TREND
    # =====================

    if move_percent >= 2:

        stock["trend"] = (
            "BULLISH"
        )

    elif move_percent <= -2:

        stock["trend"] = (
            "BEARISH"
        )

    else:

        stock["trend"] = (
            "SIDEWAYS"
        )

    # =====================
    # BREAKOUT MEMORY
    # =====================

    if (

        abs(move_percent) >= 1

        and

        stock["breakout_time"] is None

    ):

        stock["breakout_price"] = (
            ltp
        )

        stock["breakout_time"] = (
            current_time
        )

    # =====================
    # UPDATE TIME
    # =====================

    stock["last_update"] = (

        now.strftime(
            "%H:%M:%S"
        )

    )

    # =====================
    # SAVE HISTORY
    # =====================

    save_stock_history(

        symbol=symbol,

        ltp=ltp,

        volume=volume,

        move=move_percent,

        rfact=round(
            abs(move_percent) * 2,
            2
        ),

        trend=stock["trend"],

        signal=stock["trend"]

    )

# =========================
# GET MOVE %
# =========================

def get_move_percent(symbol):

    stock = market_memory.get(
        symbol,
        {}
    )

    return stock.get(
        "move_percent",
        0
    )

# =========================
# GET TREND
# =========================

def get_market_trend(symbol):

    stock = market_memory.get(
        symbol,
        {}
    )

    return stock.get(
        "trend",
        "SIDEWAYS"
    )

# =========================
# GET BREAKOUT TIME
# =========================

def get_breakout_time(symbol):

    stock = market_memory.get(
        symbol,
        {}
    )

    return stock.get(
        "breakout_time",
        "LIVE"
    )

# =========================
# GET REFERENCE PRICE
# =========================

def get_reference_price_live(symbol):

    stock = market_memory.get(
        symbol,
        {}
    )

    return stock.get(
        "reference_price",
        0
    )

# =========================
# GET MARKET MEMORY
# =========================

def get_market_memory(symbol):

    return market_memory.get(
        symbol,
        {}
    )

# =========================
# SCANNER ACTIVE
# =========================

def is_scanner_active():

    now = datetime.now()

    current_time = now.strftime(
        "%H:%M"
    )

    return current_time >= SNAPSHOT_START