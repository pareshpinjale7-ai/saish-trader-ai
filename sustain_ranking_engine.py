# sustain_ranking_engine.py

# =========================
# SUSTAIN RANKING
# =========================

def rank_sustain_stocks(

    stocks

):

    return sorted(

        stocks,

        key=lambda x:

        x.get(

            "sustain_score",

            0

        ),

        reverse=True

    )