# ==========================================
# Institutional Trade Engine
# File : portfolio_manager.py
# Version : 6.0
# ==========================================

from config import (
    DEFAULT_CAPITAL,
    MAX_OPEN_TRADES
)


class PortfolioManager:

    def __init__(self):

        self.capital = float(DEFAULT_CAPITAL)
        self.used_capital = 0.0
        self.open_trades = []

    # ---------------------------------------
    # Capital
    # ---------------------------------------

    def available_capital(self):

        return round(
            self.capital - self.used_capital,
            2
        )

    # ---------------------------------------
    # Validation
    # ---------------------------------------

    def can_take_trade(
        self,
        symbol,
        required_capital
    ):

        required_capital = float(required_capital)

        if len(self.open_trades) >= MAX_OPEN_TRADES:
            return False, "Maximum open trades reached"

        for trade in self.open_trades:

            if trade["symbol"] == symbol:
                return False, "Trade already exists"

        if required_capital > self.available_capital():
            return False, "Insufficient capital"

        return True, "Approved"

    # ---------------------------------------
    # Add Trade
    # ---------------------------------------

    def add_trade(
        self,
        symbol,
        capital
    ):

        capital = float(capital)

        ok, message = self.can_take_trade(
            symbol,
            capital
        )

        if not ok:
            return False, message

        self.open_trades.append({

            "symbol": symbol,

            "capital": capital

        })

        self.used_capital += capital

        return True, "Trade Added"

    # ---------------------------------------
    # Close Trade
    # ---------------------------------------

    def close_trade(
        self,
        symbol
    ):

        for trade in list(self.open_trades):

            if trade["symbol"] == symbol:

                self.used_capital -= trade["capital"]

                self.open_trades.remove(trade)

                return True

        return False

    # ---------------------------------------
    # Helpers
    # ---------------------------------------

    def get_open_trades(self):

        return self.open_trades

    def has_trade(self, symbol):

        return any(
            t["symbol"] == symbol
            for t in self.open_trades
        )

    def reset(self):

        self.used_capital = 0.0
        self.open_trades = []

    # ---------------------------------------
    # Summary
    # ---------------------------------------

    def summary(self):

        utilisation = 0

        if self.capital > 0:

            utilisation = round(

                (self.used_capital / self.capital) * 100,

                2

            )

        return {

            "total_capital": round(self.capital, 2),

            "used_capital": round(self.used_capital, 2),

            "available_capital": self.available_capital(),

            "capital_utilisation": utilisation,

            "open_trades": len(self.open_trades),

            "max_open_trades": MAX_OPEN_TRADES

        }
