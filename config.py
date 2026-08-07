# ==========================================
# Institutional Trade Engine
# File : config.py
# Version : 5.1 (Updated with Live Feed Settings)
# ==========================================

from datetime import time

# ==========================================
# APP & MODE CONFIGURATION
# ==========================================

APP_NAME = "Institutional AI Trade Engine"
VERSION = "5.1"
AUTO_REFRESH_SECONDS = 60

# LIVE TRADING TOGGLE & CREDENTIALS
LIVE_MODE = False  # Set to True for Live Feed, False for Mock/Backtest
BROKER = "kite"    # Options: "kite", "upstox", "angelone"

API_KEY = "your_api_key_here"
API_SECRET = "your_api_secret_here"
ACCESS_TOKEN = "your_access_token_here"

# Trading Symbol / Instrument
DEFAULT_SYMBOL = "NSE:NIFTY 50"

# ==========================================
# CAPITAL
# ==========================================

DEFAULT_CAPITAL = 500000
RISK_PERCENT = 1.0
MAX_OPEN_TRADES = 1
MIN_CONFIDENCE = 85

# ==========================================
# MARKET TIMINGS (IST)
# ==========================================

MARKET_OPEN = time(9, 15)
NO_TRADE_BEFORE = time(9, 30)
LAST_ENTRY = time(14, 45)
SQUARE_OFF = time(15, 20)

# ==========================================
# DATA
# ==========================================

DEFAULT_INTERVAL = "15m"
DEFAULT_PERIOD = "30d"
ENTRY_INTERVAL = "5m"
TREND_INTERVAL = "1h"

# ==========================================
# STRATEGY WEIGHTS
# ==========================================

WEIGHTS = {
    "PDH": 10,
    "ORB": 8,
    "VWAP": 8,
    "EMA": 8,
    "CPR": 6,
    "SUPERTREND": 8,
    "ATR": 5,
    "SMART_MONEY": 10,
    "ORDER_BLOCK": 8,
    "LIQUIDITY": 8,
    "MARKET_STRUCTURE": 8,
    "MULTI_TIMEFRAME": 10,
    "OPTION_CHAIN": 5,
    "GLOBAL": 5,
    "SECTOR": 5,
    "BREADTH": 5
}

# ==========================================
# ATR
# ==========================================

ATR_PERIOD = 14
ATR_SL = 1.5
ATR_TARGET1 = 2.0
ATR_TARGET2 = 3.0

# ==========================================
# EMA
# ==========================================

FAST_EMA = 20
SLOW_EMA = 50

# ==========================================
# VWAP
# ==========================================

USE_VWAP = True

# ==========================================
# CPR
# ==========================================

USE_CPR = True

# ==========================================
# OPTION CHAIN
# ==========================================

MIN_PCR = 0.80
MAX_PCR = 1.30

# ==========================================
# VOLUME
# ==========================================

MIN_VOLUME_RATIO = 2.0

# ==========================================
# BACKTEST
# ==========================================

BROKERAGE = 40
SLIPPAGE = 0.0005
STT = 0.00025

# ==========================================
# LOGGING
# ==========================================

DEBUG = True
