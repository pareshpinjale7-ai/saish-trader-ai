# analytics_engine.py

# =========================
# ANALYTICS
# =========================

def generate_analytics(

    trades

):

    total_pnl = 0

    wins = 0
    losses = 0

    for trade in trades:

        pnl = trade.get(

            "pnl",

            0

        )

        total_pnl += pnl

        if pnl > 0:

            wins += 1

        else:

            losses += 1

    total = wins + losses

    accuracy = 0

    if total > 0:

        accuracy = (

            wins / total

        ) * 100

    return {

        "total_pnl":

        round(total_pnl, 2),

        "wins": wins,

        "losses": losses,

        "accuracy":

        round(accuracy, 2)

    }