# ==========================================
# Institutional Trade Engine
# database.py
# ==========================================

WATCHLIST = {

    "NIFTY": {
        "ticker": "^NSEI",
        "type": "INDEX",
        "strike_step": 50,
        "lot_size": 25
    },

    "BANKNIFTY": {
        "ticker": "^NSEBANK",
        "type": "INDEX",
        "strike_step": 100,
        "lot_size": 15
    },

    "FINNIFTY": {
        "ticker": "NIFTY_FIN_SERVICE.NS",
        "type": "INDEX",
        "strike_step": 50,
        "lot_size": 40
    },

    "RELIANCE": {
        "ticker": "RELIANCE.NS",
        "type": "STOCK",
        "sector": "Energy"
    },

    "HDFCBANK": {
        "ticker": "HDFCBANK.NS",
        "type": "STOCK",
        "sector": "Bank"
    },

    "ICICIBANK": {
        "ticker": "ICICIBANK.NS",
        "type": "STOCK",
        "sector": "Bank"
    },

    "SBIN": {
        "ticker": "SBIN.NS",
        "type": "STOCK",
        "sector": "Bank"
    },

    "INFY": {
        "ticker": "INFY.NS",
        "type": "STOCK",
        "sector": "IT"
    },

    "TCS": {
        "ticker": "TCS.NS",
        "type": "STOCK",
        "sector": "IT"
    }

}
