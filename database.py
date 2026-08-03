# ==========================================
# Institutional Trade Engine
# File : database.py
# Version : 4.0
# ==========================================


# NSE Watchlist Database


WATCHLIST = {


    "NIFTY": {

        "ticker": "^NSEI",

        "type": "INDEX",

        "lot_size": 75,

        "strike_step": 50

    },


    "BANKNIFTY": {

        "ticker": "^NSEBANK",

        "type": "INDEX",

        "lot_size": 30,

        "strike_step": 100

    },


    "FINNIFTY": {

        "ticker": "NIFTY_FIN_SERVICE.NS",

        "type": "INDEX",

        "lot_size": 40,

        "strike_step": 50

    },


    "RELIANCE": {

        "ticker": "RELIANCE.NS",

        "type": "STOCK",

        "lot_size": 250,

        "strike_step": 20

    },


    "HDFCBANK": {

        "ticker": "HDFCBANK.NS",

        "type": "STOCK",

        "lot_size": 550,

        "strike_step": 20

    },


    "ICICIBANK": {

        "ticker": "ICICIBANK.NS",

        "type": "STOCK",

        "lot_size": 700,

        "strike_step": 20

    },


    "SBIN": {

        "ticker": "SBIN.NS",

        "type": "STOCK",

        "lot_size": 750,

        "strike_step": 10

    },


    "INFY": {

        "ticker": "INFY.NS",

        "type": "STOCK",

        "lot_size": 400,

        "strike_step": 20

    },


    "TATAMOTORS": {

        "ticker": "TATAMOTORS.NS",

        "type": "STOCK",

        "lot_size": 1400,

        "strike_step": 10

    },


    "LT": {

        "ticker": "LT.NS",

        "type": "STOCK",

        "lot_size": 175,

        "strike_step": 50

    }

}




# ==========================================
# F&O Universe Helper
# ==========================================


def get_fno_universe():

    return WATCHLIST



# ==========================================
# NSE Holidays Placeholder
# ==========================================


NSE_HOLIDAYS = [

    "2026-01-26",

    "2026-03-03",

    "2026-03-26",

    "2026-04-14",

    "2026-08-15",

    "2026-10-02",

    "2026-11-10",

    "2026-12-25"

]



def is_market_holiday(date):

    date=str(date)

    return date in NSE_HOLIDAYS
