# history_store.py

# =========================
# BREAKOUT HISTORY
# =========================

breakout_history = {}

# =========================
# SAVE BREAKOUT
# =========================

def save_breakout(

    symbol,

    data

):

    if symbol not in breakout_history:

        breakout_history[symbol] = []

    breakout_history[symbol].append(data)

    breakout_history[symbol] = (

        breakout_history[symbol][-100:]

    )

# =========================
# GET HISTORY
# =========================

def get_breakout_history(

    symbol

):

    return breakout_history.get(

        symbol,

        []

    )