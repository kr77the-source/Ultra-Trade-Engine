# ==========================================
# Institutional Trade Engine
# File : performance.py
# Version : 6.0
# ==========================================

import os
import pandas as pd

LOG_FILE = "logs/trade_log.csv"


# ------------------------------------------
# Load History
# ------------------------------------------

def load_history():

    if not os.path.exists(LOG_FILE):
        return pd.DataFrame()

    try:
        return pd.read_csv(LOG_FILE)
    except Exception:
        return pd.DataFrame()


# ------------------------------------------
# Empty Statistics
# ------------------------------------------

def empty_statistics():

    return {

        "total_trades": 0,
        "wins": 0,
        "losses": 0,
        "win_rate": 0,
        "loss_rate": 0,
        "total_pnl": 0,
        "average_pnl": 0,
        "profit_factor": 0,
        "max_drawdown": 0

    }


# ------------------------------------------
# Statistics
# ------------------------------------------

def get_statistics():

    df = load_history()

    if df.empty:
        return empty_statistics()

    required = ["Status", "PnL"]

    for col in required:
        if col not in df.columns:
            return empty_statistics()

    closed = df[df["Status"] != "OPEN"]

    if closed.empty:
        return empty_statistics()

    wins = closed[closed["PnL"] > 0]
    losses = closed[closed["PnL"] < 0]

    total = len(closed)

    total_pnl = closed["PnL"].sum()

    average = closed["PnL"].mean()

    gross_profit = wins["PnL"].sum()

    gross_loss = abs(losses["PnL"].sum())

    profit_factor = (
        round(gross_profit / gross_loss, 2)
        if gross_loss > 0
        else round(gross_profit, 2)
    )

    equity = closed["PnL"].cumsum()

    drawdown = equity - equity.cummax()

    max_dd = round(drawdown.min(), 2)

    return {

        "total_trades": total,

        "wins": len(wins),

        "losses": len(losses),

        "win_rate": round(len(wins) * 100 / total, 2),

        "loss_rate": round(len(losses) * 100 / total, 2),

        "total_pnl": round(total_pnl, 2),

        "average_pnl": round(average, 2),

        "profit_factor": profit_factor,

        "max_drawdown": max_dd

    }


# ------------------------------------------
# Monthly Report
# ------------------------------------------

def monthly_report():

    df = load_history()

    if df.empty:
        return pd.DataFrame()

    if "Date" not in df.columns or "PnL" not in df.columns:
        return pd.DataFrame()

    df["Date"] = pd.to_datetime(
        df["Date"],
        errors="coerce"
    )

    df = df.dropna(subset=["Date"])

    if df.empty:
        return pd.DataFrame()

    df["Month"] = df["Date"].dt.strftime("%Y-%m")

    return (

        df.groupby("Month")["PnL"]

        .sum()

        .reset_index()

    )
