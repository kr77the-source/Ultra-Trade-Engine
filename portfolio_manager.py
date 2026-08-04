# ==========================================
# Institutional Trade Engine
# File : portfolio_manager.py
# Version : 5.0
# ==========================================

from config import (
    DEFAULT_CAPITAL,
    MAX_OPEN_TRADES
)


class PortfolioManager:

    def __init__(self):

        self.capital = DEFAULT_CAPITAL

        self.open_trades = []

        self.used_capital = 0


    def available_capital(self):

        return round(

            self.capital -

            self.used_capital,

            2

        )


    def can_take_trade(

        self,

        symbol,

        required_capital

    ):

        if len(self.open_trades) >= MAX_OPEN_TRADES:

            return False, "Maximum open trades reached"


        for trade in self.open_trades:

            if trade["symbol"] == symbol:

                return False, "Trade already exists"


        if required_capital > self.available_capital():

            return False, "Insufficient capital"


        return True, "Approved"


    def add_trade(

        self,

        symbol,

        capital

    ):

        self.open_trades.append({

            "symbol": symbol,

            "capital": capital

        })

        self.used_capital += capital


    def close_trade(

        self,

        symbol

    ):

        for trade in self.open_trades:

            if trade["symbol"] == symbol:

                self.used_capital -= trade["capital"]

                self.open_trades.remove(trade)

                return True

        return False


    def summary(self):

        return {

            "total_capital": self.capital,

            "used_capital": round(

                self.used_capital,

                2

            ),

            "available_capital": self.available_capital(),

            "open_trades": len(self.open_trades)

        }
