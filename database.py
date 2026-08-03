# ==========================================
# Institutional Trade Engine
# database.py
# ==========================================

# Major Indices
INDEX_DB = {
    "NIFTY": {
        "symbol": "^NSEI",
        "exchange": "NSE",
        "type": "INDEX",
        "strike_step": 50,
        "lot_size": 25
    },

    "BANKNIFTY": {
        "symbol": "^NSEBANK",
        "exchange": "NSE",
        "type": "INDEX",
        "strike_step": 100,
        "lot_size": 15
    },

    "FINNIFTY": {
        "symbol": "NIFTY_FIN_SERVICE.NS",
        "exchange": "NSE",
        "type": "INDEX",
        "strike_step": 50,
        "lot_size": 40
    }
}

# Sample F&O Stocks
STOCK_DB = {

    "RELIANCE": {
        "symbol": "RELIANCE.NS",
        "sector": "Energy",
        "lot_size": 250
    },

    "HDFCBANK": {
        "symbol": "HDFCBANK.NS",
        "sector": "Bank",
        "lot_size": 550
    },

    "ICICIBANK": {
        "symbol": "ICICIBANK.NS",
        "sector": "Bank",
        "lot_size": 700
    },

    "SBIN": {
        "symbol": "SBIN.NS",
        "sector": "Bank",
        "lot_size": 750
    }

}
