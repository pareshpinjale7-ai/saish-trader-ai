# sustain_engine.py

# =========================
# SUSTAIN STOCKS
# =========================

sustain_store = {}

# =========================
# UPDATE
# =========================

def update_sustain(

    symbol,

    rfact

):

    if symbol not in sustain_store:

        sustain_store[symbol] = []

    sustain_store[symbol].append(

        rfact

    )

    sustain_store[symbol] = (

        sustain_store[symbol][-50:]

    )

# =========================
# SUSTAIN SCORE
# =========================

def get_sustain_score(

    symbol

):

    if symbol not in sustain_store:

        return 0

    scores = sustain_store[symbol]

    if len(scores) == 0:

        return 0

    avg = (

        sum(

            abs(x)

            for x in scores

        )

        / len(scores)

    )

    return round(avg, 2)