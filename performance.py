# ==========================================
# Institutional Trade Engine
# File : performance.py
# Version : 7.0
# ==========================================

import os
import pandas as pd

LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "trade_log.csv")


# ------------------------------------------
# Load History
# ------------------------------------------

def load_history():

    # Create logs folder automatically
    os.makedirs(LOG_DIR, exist_ok=True)

    # If log file doesn't exist
    if not os.path.exists(LOG_FILE):
        return pd.DataFrame()

    try:

        df = pd.read_csv(LOG_FILE)

        if df is None:
            return pd.DataFrame()

        return df

    except Exception as e:

        print(f"Performance Load Error : {e}")

        return pd.DataFrame()


# ------------------------------------------
# Empty Statistics
# ------------------------------------------

def empty_statistics():

    return {

        "total_trades": 0,
        "wins": 0,
        "losses": 0,
        "win_rate": 0.0,
        "loss_rate": 0.0,
        "total_pnl": 0.0,
        "average_pnl": 0.0,
        "profit_factor": 0.0,
        "max_drawdown": 0.0

    }


# ------------------------------------------
# Statistics
# ------------------------------------------

def get_statistics():

    df = load_history()

    if df.empty:
        return empty_statistics()

    required_columns = [

        "Status",
        "PnL"

    ]

    for col in required_columns:

        if col not in df.columns:
            return empty_statistics()

    closed = df[df["Status"] != "OPEN"]

    if closed.empty:
        return empty_statistics()

    wins = closed[closed["PnL"] > 0]

    losses = closed[closed["PnL"] < 0]

    total = len(closed)

    total_pnl = float(closed["PnL"].sum())

    average_pnl = float(closed["PnL"].mean())

    gross_profit = float(wins["PnL"].sum())

    gross_loss = abs(float(losses["PnL"].sum()))

    if gross_loss == 0:

        profit_factor = round(gross_profit, 2)

    else:

        profit_factor = round(

            gross_profit / gross_loss,

            2

        )

    equity = closed["PnL"].cumsum()

    drawdown = equity - equity.cummax()

    max_drawdown = round(

        drawdown.min(),

        2

    )

    return {

        "total_trades": total,

        "wins": len(wins),

        "losses": len(losses),

        "win_rate": round(

            len(wins) * 100 / total,

            2

        ),

        "loss_rate": round(

            len(losses) * 100 / total,

            2

        ),

        "total_pnl": round(

            total_pnl,

            2

        ),

        "average_pnl": round(

            average_pnl,

            2

        ),

        "profit_factor": profit_factor,

        "max_drawdown": max_drawdown

    }


# ------------------------------------------
# Monthly Report
# ------------------------------------------

def monthly_report():

    df = load_history()

    if df.empty:
        return pd.DataFrame()

    if "Date" not in df.columns:

        return pd.DataFrame()

    if "PnL" not in df.columns:

        return pd.DataFrame()

    df["Date"] = pd.to_datetime(

        df["Date"],

        errors="coerce"

    )

    df = df.dropna(

        subset=["Date"]

    )

    if df.empty:

        return pd.DataFrame()

    df["Month"] = df["Date"].dt.strftime(

        "%Y-%m"

    )

    report = (

        df.groupby("Month")["PnL"]

        .sum()

        .reset_index()

    )

    return report


# ------------------------------------------
# Performance Summary
# ------------------------------------------

def performance_summary():

    stats = get_statistics()

    print("\n========== PERFORMANCE ==========")

    for k, v in stats.items():

        print(f"{k:20}: {v}")

    print("=================================\n")


# ------------------------------------------
# Test
# ------------------------------------------

if __name__ == "__main__":

    performance_summary()
