# trade_journal_engine.py

# =========================
# TRADE JOURNAL
# =========================

trade_journal = []

# =========================
# SAVE TRADE
# =========================

def save_trade(

    symbol,
    entry,
    exit_price,
    pnl

):

    trade_journal.append({

        "symbol": symbol,

        "entry": entry,

        "exit": exit_price,

        "pnl": pnl

    })

# =========================
# GET JOURNAL
# =========================

def get_trade_journal():

    return trade_journal