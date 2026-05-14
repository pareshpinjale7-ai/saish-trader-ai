# opening_memory.py

from datetime import datetime

# =========================
# OPENING MEMORY
# =========================

opening_memory = {}

# =========================
# MARKET OPEN WINDOW
# =========================

OPENING_START = (9, 15)

OPENING_END = (9, 45)

# =========================
# CHECK OPENING SESSION
# =========================

def is_opening_session():

    now = datetime.now()

    current = (

        now.hour,

        now.minute

    )

    return (

        current >= OPENING_START

        and

        current <= OPENING_END

    )

# =========================
# UPDATE OPENING MEMORY
# =========================

def update_opening_memory(

    symbol,

    ltp,

    volume

):

    if not is_opening_session():

        return

    # =====================
    # INIT SYMBOL
    # =====================

    if symbol not in opening_memory:

        opening_memory[symbol] = {

            "opening_high": ltp,

            "opening_low": ltp,

            "opening_volume": volume,

            "opening_vwap_total": (

                ltp * volume

            ),

            "opening_total_volume": volume,

            "opening_vwap": ltp,

            "first_breakout_time": None,

            "opening_strength": 0

        }

    data = opening_memory[symbol]

    # =====================
    # UPDATE HIGH LOW
    # =====================

    data["opening_high"] = max(

        data["opening_high"],

        ltp

    )

    data["opening_low"] = min(

        data["opening_low"],

        ltp

    )

    # =====================
    # UPDATE VOLUME
    # =====================

    data["opening_volume"] += volume

    # =====================
    # VWAP
    # =====================

    data["opening_vwap_total"] += (

        ltp * volume

    )

    data["opening_total_volume"] += volume

    total_vol = data["opening_total_volume"]

    if total_vol > 0:

        data["opening_vwap"] = round(

            data["opening_vwap_total"]

            / total_vol,

            2

        )

    # =====================
    # OPENING STRENGTH
    # =====================

    high = data["opening_high"]

    low = data["opening_low"]

    if low > 0:

        strength = (

            (ltp - low)

            / low

        ) * 100

        data["opening_strength"] = round(

            strength,

            2

        )

# =========================
# GET OPENING DATA
# =========================

def get_opening_data(symbol):

    return opening_memory.get(

        symbol,

        {}

    )