# execution_tracker.py

# =========================
# EXECUTION TRACKER
# =========================

executions = []

# =========================
# SAVE
# =========================

def save_execution(

    symbol,
    signal,
    entry

):

    executions.append({

        "symbol": symbol,

        "signal": signal,

        "entry": entry

    })

# =========================
# GET
# =========================

def get_executions():

    return executions