# ranking_engine.py

# =========================
# SORT BY RFACTOR
# =========================

def rank_stocks(data):

    return sorted(

        data,

        key=lambda x:

        abs(

            x["rfact"]

        ),

        reverse=True

    )