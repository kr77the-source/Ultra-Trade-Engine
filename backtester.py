# ==========================================
# Institutional Trade Engine
# File : backtester.py
# Version : 5.0
# ==========================================

import pandas as pd


class Backtester:

    def __init__(
        self,
        initial_capital=500000,
        brokerage=40,
        slippage=0.0005
    ):

        self.initial_capital = initial_capital
        self.capital = initial_capital
        self.brokerage = brokerage
        self.slippage = slippage

        self.trades = []


    def add_trade(

        self,

        symbol,

        signal,

        entry,

        exit_price,

        quantity

    ):

        if signal == "BUY":

            pnl = (
                (exit_price - entry)
                * quantity
            )

        else:

            pnl = (
                (entry - exit_price)
                * quantity
            )


        pnl -= self.brokerage

        self.capital += pnl


        self.trades.append({

            "Symbol": symbol,

            "Signal": signal,

            "Entry": entry,

            "Exit": exit_price,

            "Qty": quantity,

            "PnL": round(pnl,2),

            "Capital": round(self.capital,2)

        })


    def report(self):

        if len(self.trades)==0:

            return None


        df = pd.DataFrame(self.trades)


        wins = len(df[df.PnL>0])

        losses = len(df[df.PnL<=0])

        total = len(df)


        win_rate = round(

            wins*100/total,

            2

        )


        gross_profit = df[df.PnL>0].PnL.sum()

        gross_loss = abs(

            df[df.PnL<0].PnL.sum()

        )


        if gross_loss==0:

            pf=999

        else:

            pf=round(

                gross_profit/

                gross_loss,

                2

            )


        equity = df["Capital"]

        drawdown = equity-equity.cummax()


        return {

            "Initial Capital":

                self.initial_capital,

            "Final Capital":

                round(self.capital,2),

            "Trades":

                total,

            "Wins":

                wins,

            "Losses":

                losses,

            "Win Rate":

                win_rate,

            "Profit Factor":

                pf,

            "Max Drawdown":

                round(drawdown.min(),2),

            "Trade Book":

                df

        }
