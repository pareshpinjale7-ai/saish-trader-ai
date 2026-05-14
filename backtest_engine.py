# backtest_engine.py

# =========================
# SIMPLE BACKTEST
# =========================

def run_backtest(

    trades

):

    total = len(trades)

    wins = 0
    losses = 0

    for trade in trades:

        pnl = trade.get(

            "pnl",

            0

        )

        if pnl > 0:

            wins += 1

        else:

            losses += 1

    accuracy = 0

    if total > 0:

        accuracy = (

            wins / total

        ) * 100

    return {

        "total": total,

        "wins": wins,

        "losses": losses,

        "accuracy": round(

            accuracy,

            2

        )

    }