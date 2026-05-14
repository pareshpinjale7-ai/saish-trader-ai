# breakout_time_engine.py

from datetime import datetime

# =========================
# BREAKOUT TIMES
# =========================

breakout_times = {}

# =========================
# SAVE FIRST BREAKOUT
# =========================

def save_breakout_time(

    symbol

):

    if symbol not in breakout_times:

        breakout_times[symbol] = (

            datetime.now()

            .strftime("%H:%M:%S")

        )

# =========================
# GET BREAKOUT TIME
# =========================

def get_breakout_time(

    symbol

):

    return breakout_times.get(

        symbol,

        "LIVE"

    )