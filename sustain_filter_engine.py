# sustain_filter_engine.py

# =========================
# SUSTAIN FILTER
# =========================

def is_sustainable(

    stock

):

    rfact = stock.get(

        "rfact",

        0

    )

    probability = stock.get(

        "probability",

        0

    )

    rel_volume = stock.get(

        "relative_volume",

        0

    )

    momentum = abs(

        stock.get(

            "momentum",

            0

        )

    )

    # =====================
    # CONDITIONS
    # =====================

    if (

        abs(rfact) >= 6

        and

        probability >= 60

        and

        rel_volume >= 1.5

        and

        momentum >= 1

    ):

        return True

    return False