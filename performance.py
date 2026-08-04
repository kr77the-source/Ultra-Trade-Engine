# ==========================================
# Institutional Trade Engine
# File : performance.py
# Version : 5.0
# ==========================================

import pandas as pd
import os

LOG_FILE = "logs/trade_log.csv"


def load_history():

    if not os.path.exists(LOG_FILE):
        return pd.DataFrame()

    return pd.read_csv(LOG_FILE)


def get_statistics():

    df = load_history()

    if df.empty:

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

    closed = df[df["Status"] != "OPEN"]

    if closed.empty:

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

    wins = closed[closed["PnL"] > 0]

    losses = closed[closed["PnL"] < 0]

    total_trades = len(closed)

    total_pnl = closed["PnL"].sum()

    avg_pnl = closed["PnL"].mean()

    gross_profit = wins["PnL"].sum()

    gross_loss = abs(losses["PnL"].sum())

    if gross_loss == 0:

        profit_factor = gross_profit

    else:

        profit_factor = round(

            gross_profit /

            gross_loss,

            2

        )

    equity = closed["PnL"].cumsum()

    drawdown = equity - equity.cummax()

    max_dd = drawdown.min()

    return {

        "total_trades": total_trades,

        "wins": len(wins),

        "losses": len(losses),

        "win_rate": round(

            len(wins) *

            100 /

            total_trades,

            2

        ),

        "loss_rate": round(

            len(losses) *

            100 /

            total_trades,

            2

        ),

        "total_pnl": round(

            total_pnl,

            2

        ),

        "average_pnl": round(

            avg_pnl,

            2

        ),

        "profit_factor": profit_factor,

        "max_drawdown": round(

            max_dd,

            2

        )

    }


def monthly_report():

    df = load_history()

    if df.empty:

        return pd.DataFrame()

    df["Date"] = pd.to_datetime(df["Date"])

    df["Month"] = df["Date"].dt.strftime("%Y-%m")

    report = (

        df.groupby("Month")["PnL"]

        .sum()

        .reset_index()

    )

    return report
