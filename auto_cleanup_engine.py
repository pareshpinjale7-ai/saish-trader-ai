# auto_cleanup_engine.py

# =========================
# AUTO CLEANUP
# =========================

def cleanup_old_data(

    store,
    limit=500

):

    for symbol in store:

        if len(store[symbol]) > limit:

            keys = sorted(

                store[symbol]

            )

            extra = len(

                store[symbol]

            ) - limit

            for key in keys[:extra]:

                del store[symbol][key]