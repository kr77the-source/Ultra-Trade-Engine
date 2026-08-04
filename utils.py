# ==========================================
# Institutional Trade Engine
# File : utils.py
# Version : 7.0
# ==========================================

from datetime import datetime, time
import math


# -------------------------------
# Market Time
# -------------------------------

def is_market_open():

    now = datetime.now().time()

    market_open = time(9, 15)
    market_close = time(15, 30)

    return market_open <= now <= market_close


# -------------------------------
# Round Price
# -------------------------------

def round_price(price):

    return round(price, 2)


# -------------------------------
# ATM Strike
# -------------------------------

def atm_strike(price, step):

    return int(round(price / step) * step)


# -------------------------------
# Risk Reward
# -------------------------------

def risk_reward(entry, sl, target):

    risk = abs(entry - sl)

    reward = abs(target - entry)

    if risk == 0:
        return 0

    return round(reward / risk, 2)


# -------------------------------
# Position Size
# -------------------------------

def position_size(capital, risk_percent, entry, sl):

    risk_amount = capital * risk_percent / 100

    risk = abs(entry - sl)

    if risk == 0:
        return 0

    return math.floor(risk_amount / risk)


# -------------------------------
# Percentage Change
# -------------------------------

def percent_change(old, new):

    if old == 0:
        return 0

    return round(((new - old) / old) * 100, 2)


# -------------------------------
# Current Time
# -------------------------------

def current_time():

    return datetime.now().strftime("%H:%M:%S")


# -------------------------------
# Current Date
# -------------------------------

def current_date():

    return datetime.now().strftime("%Y-%m-%d")
