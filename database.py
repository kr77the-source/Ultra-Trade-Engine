# ==========================================
# Institutional Trade Engine
# File : database.py
# Version : 5.0
# ==========================================

from typing import Dict, Optional

# ==========================================
# NSE Watchlist
# ==========================================

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
# Helpers
# ==========================================

def get_fno_universe() -> Dict:
    return WATCHLIST


def get_symbol(symbol: str) -> Optional[dict]:
    return WATCHLIST.get(symbol.upper())


def get_ticker(symbol: str) -> Optional[str]:
    item = get_symbol(symbol)
    return item["ticker"] if item else None


def get_lot_size(symbol: str) -> int:
    item = get_symbol(symbol)
    return item["lot_size"] if item else 0


def get_strike_step(symbol: str) -> int:
    item = get_symbol(symbol)
    return item["strike_step"] if item else 50


def get_asset_type(symbol: str) -> str:
    item = get_symbol(symbol)
    return item["type"] if item else "STOCK"


# ==========================================
# NSE Holidays (2026)
# ==========================================

NSE_HOLIDAYS = {
    "2026-01-26",
    "2026-03-03",
    "2026-03-26",
    "2026-04-14",
    "2026-08-15",
    "2026-10-02",
    "2026-11-10",
    "2026-12-25",
}


def is_market_holiday(date) -> bool:
    return str(date) in NSE_HOLIDAYS
