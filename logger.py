# ==========================================
# Institutional Trade Engine
# File : logger.py
# Version : 5.0
# ==========================================

import os
import csv
from datetime import datetime

LOG_FOLDER = "logs"
LOG_FILE = os.path.join(LOG_FOLDER, "trade_log.csv")


def create_log_file():

    if not os.path.exists(LOG_FOLDER):
        os.makedirs(LOG_FOLDER)

    if not os.path.exists(LOG_FILE):

        with open(LOG_FILE, "w", newline="") as file:

            writer = csv.writer(file)

            writer.writerow([

                "Date",
                "Time",
                "Symbol",
                "Signal",
                "Entry",
                "StopLoss",
                "Target1",
                "Target2",
                "Quantity",
                "Confidence",
                "Status",
                "PnL"

            ])


def log_trade(

    symbol,
    signal,
    entry,
    stop_loss,
    target1,
    target2,
    quantity,
    confidence

):

    create_log_file()

    now = datetime.now()

    with open(LOG_FILE, "a", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([

            now.strftime("%Y-%m-%d"),

            now.strftime("%H:%M:%S"),

            symbol,

            signal,

            entry,

            stop_loss,

            target1,

            target2,

            quantity,

            confidence,

            "OPEN",

            0

        ])


def update_trade_result(

    symbol,

    pnl,

    status

):

    if not os.path.exists(LOG_FILE):

        return

    rows = []

    with open(LOG_FILE, "r") as file:

        reader = csv.reader(file)

        rows = list(reader)

    for i in range(1, len(rows)):

        if rows[i][2] == symbol and rows[i][10] == "OPEN":

            rows[i][10] = status

            rows[i][11] = pnl

            break

    with open(LOG_FILE, "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerows(rows)


def get_trade_history():

    create_log_file()

    trades = []

    with open(LOG_FILE, "r") as file:

        reader = csv.DictReader(file)

        for row in reader:

            trades.append(row)

    return trades
