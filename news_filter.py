# ==========================================
# Institutional Trade Engine
# File : news_filter.py
# Version : 1.0
# ==========================================

from datetime import datetime

# High Impact Events
HIGH_IMPACT_EVENTS = [

    "RBI POLICY",
    "FED MEETING",
    "US CPI",
    "INDIA CPI",
    "US GDP",
    "INDIA GDP",
    "NON FARM PAYROLL",
    "FOMC",
    "BUDGET",
    "UNION BUDGET",
    "ELECTION RESULT",
    "GIFT NIFTY GAP > 1%",
    "MAJOR COMPANY RESULTS"

]


def check_news(event_name):

    event = event_name.upper()

    if event in HIGH_IMPACT_EVENTS:

        return {

            "allow_trade": False,

            "confidence": 0,

            "message": "High Impact News"

        }

    return {

        "allow_trade": True,

        "confidence": 100,

        "message": "No Major News"

    }


def market_session():

    now = datetime.now()

    hour = now.hour

    minute = now.minute

    current = hour * 60 + minute

    if current < 555:

        return "PRE MARKET"

    elif current <= 930:

        return "LIVE MARKET"

    return "POST MARKET"
