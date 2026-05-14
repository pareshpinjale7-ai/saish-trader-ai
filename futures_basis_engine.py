# futures_basis_engine.py

# =========================
# FUTURES BASIS
# =========================

def calculate_basis(

    spot_price,
    futures_price

):

    if spot_price == 0:

        return 0

    basis = (

        (futures_price - spot_price)

        / spot_price

    ) * 100

    return round(

        basis,

        2

    )