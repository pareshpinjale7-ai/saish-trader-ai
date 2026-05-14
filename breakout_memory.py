# breakout_memory.py

# =========================
# BREAKOUT MEMORY
# =========================

breakout_memory = {}

# =========================
# SAVE BREAKOUT
# =========================

def save_breakout(

    symbol,

    breakout_type,

    breakout_price

):

    if symbol not in breakout_memory:

        breakout_memory[symbol] = {

            "type": breakout_type,

            "price": breakout_price

        }

# =========================
# GET
# =========================

def get_breakout(symbol):

    return breakout_memory.get(

        symbol,

        {}

    )