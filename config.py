# ==========================
# Institutional Trade Engine
# config.py
# ==========================

APP_NAME = "Institutional Trade Engine"

MARKET_START = "09:15"
MARKET_SCAN_START = "09:30"
MARKET_CLOSE = "15:30"

TIMEFRAME = "5m"

SCAN_INTERVAL = 60

CONFIDENCE_SCORE = 95

RISK_REWARD = 2.0

MAX_TRADES_PER_DAY = 1

CAPITAL = 100000

RISK_PER_TRADE = 1.0

USE_GLOBAL_MARKET = True
USE_OPTION_CHAIN = True
USE_FII_DII = True
USE_SECTOR = True
USE_VOLUME = True
USE_SMART_MONEY = True
USE_BREADTH = True

LOG_LEVEL = "INFO"
