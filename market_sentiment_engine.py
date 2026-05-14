# market_sentiment_engine.py

# =========================
# MARKET SENTIMENT
# =========================

def get_market_sentiment(

    bullish,
    bearish

):

    if bullish > bearish * 2:

        return "EXTREME BULLISH"

    if bearish > bullish * 2:

        return "EXTREME BEARISH"

    if bullish > bearish:

        return "BULLISH"

    if bearish > bullish:

        return "BEARISH"

    return "NEUTRAL"