# ==========================================
# Institutional Trade Engine
# File : paper_trading.py
# Version : 6.0
# ==========================================

from datetime import datetime


class PaperTrader:

    def __init__(self):

        self.open_trade = None

        self.trade_history = []


    # ---------------------------------------
    # Create Virtual Trade
    # ---------------------------------------

    def create_trade(

        self,

        symbol,

        signal,

        entry,

        stop_loss,

        target1,

        target2,

        quantity,

        confidence

    ):

        if self.open_trade is not None:

            return False, "Another trade already running"


        self.open_trade = {

            "symbol": symbol,

            "signal": signal,

            "entry": entry,

            "stop_loss": stop_loss,

            "target1": target1,

            "target2": target2,

            "quantity": quantity,

            "confidence": confidence,

            "status": "OPEN",

            "entry_time": datetime.now(),

            "exit_price": None,

            "exit_reason": None,

            "pnl": 0

        }

        return True, "Paper Trade Started"


    # ---------------------------------------
    # Update Live Price
    # ---------------------------------------

    def update_price(

        self,

        live_price

    ):

        if self.open_trade is None:

            return


        trade = self.open_trade


        # BUY Trade

        if trade["signal"] == "BUY":


            if live_price <= trade["stop_loss"]:

                self.close_trade(

                    live_price,

                    "STOP LOSS"

                )


            elif live_price >= trade["target2"]:

                self.close_trade(

                    live_price,

                    "TARGET 2"

                )


            elif live_price >= trade["target1"]:

                trade["stop_loss"] = trade["entry"]


        # SELL Trade

        elif trade["signal"] == "SELL":


            if live_price >= trade["stop_loss"]:

                self.close_trade(

                    live_price,

                    "STOP LOSS"

                )


            elif live_price <= trade["target2"]:

                self.close_trade(

                    live_price,

                    "TARGET 2"

                )


            elif live_price <= trade["target1"]:

                trade["stop_loss"] = trade["entry"]


    # ---------------------------------------
    # Close Trade
    # ---------------------------------------

    def close_trade(

        self,

        exit_price,

        reason

    ):

        if self.open_trade is None:

            return


        trade = self.open_trade


        trade["exit_price"] = exit_price

        trade["exit_reason"] = reason

        trade["exit_time"] = datetime.now()

        trade["status"] = "CLOSED"


        if trade["signal"] == "BUY":

            pnl = (

                exit_price -

                trade["entry"]

            ) * trade["quantity"]


        else:

            pnl = (

                trade["entry"] -

                exit_price

            ) * trade["quantity"]


        trade["pnl"] = round(

            pnl,

            2

        )


        self.trade_history.append(trade)

        self.open_trade = None


    # ---------------------------------------
    # Running Trade
    # ---------------------------------------

    def get_open_trade(self):

        return self.open_trade


    # ---------------------------------------
    # History
    # ---------------------------------------

    def get_trade_history(self):

        return self.trade_history


    # ---------------------------------------
    # Summary
    # ---------------------------------------

    def summary(self):

        total = len(self.trade_history)

        wins = len(

            [

                x for x in self.trade_history

                if x["pnl"] > 0

            ]

        )

        losses = total - wins

        pnl = sum(

            [

                x["pnl"]

                for x in self.trade_history

            ]

        )


        return {

            "Total Trades": total,

            "Wins": wins,

            "Losses": losses,

            "Net PnL": round(pnl,2)

        }
