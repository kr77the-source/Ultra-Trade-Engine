# ==========================================
# Institutional Trade Engine
# File : paper_trading.py
# Version : 7.0
# ==========================================

from datetime import datetime


class PaperTrader:

    def __init__(self):
        self.open_trade = None
        self.trade_history = []

    # ---------------------------------------
    # Create Trade
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
        confidence,
    ):

        if self.open_trade is not None:
            return False, "Another trade already running"

        self.open_trade = {
            "symbol": symbol,
            "signal": signal,
            "entry": float(entry),
            "stop_loss": float(stop_loss),
            "target1": float(target1),
            "target2": float(target2),
            "quantity": int(quantity),
            "confidence": confidence,
            "status": "OPEN",
            "entry_time": datetime.now(),
            "exit_time": None,
            "exit_price": None,
            "exit_reason": None,
            "pnl": 0.0,
        }

        return True, "Paper Trade Started"

    # ---------------------------------------
    # Update Live Price
    # ---------------------------------------

    def update_price(self, live_price):

        if self.open_trade is None:
            return

        trade = self.open_trade
        live_price = float(live_price)

        if trade["signal"] == "BUY":

            if live_price <= trade["stop_loss"]:
                self.close_trade(live_price, "STOP LOSS")

            elif live_price >= trade["target2"]:
                self.close_trade(live_price, "TARGET 2")

            elif live_price >= trade["target1"]:
                trade["stop_loss"] = trade["entry"]

        elif trade["signal"] == "SELL":

            if live_price >= trade["stop_loss"]:
                self.close_trade(live_price, "STOP LOSS")

            elif live_price <= trade["target2"]:
                self.close_trade(live_price, "TARGET 2")

            elif live_price <= trade["target1"]:
                trade["stop_loss"] = trade["entry"]

    # ---------------------------------------
    # Close Trade
    # ---------------------------------------

    def close_trade(self, exit_price, reason):

        if self.open_trade is None:
            return

        trade = self.open_trade

        trade["exit_price"] = float(exit_price)
        trade["exit_reason"] = reason
        trade["exit_time"] = datetime.now()
        trade["status"] = "CLOSED"

        if trade["signal"] == "BUY":
            pnl = (trade["exit_price"] - trade["entry"]) * trade["quantity"]
        else:
            pnl = (trade["entry"] - trade["exit_price"]) * trade["quantity"]

        trade["pnl"] = round(pnl, 2)

        self.trade_history.append(trade)
        self.open_trade = None

    # ---------------------------------------
    # Helpers
    # ---------------------------------------

    def has_open_trade(self):
        return self.open_trade is not None

    def get_open_trade(self):
        return self.open_trade

    def get_trade_history(self):
        return self.trade_history

    def reset(self):
        self.open_trade = None
        self.trade_history = []

    # ---------------------------------------
    # Statistics
    # ---------------------------------------

    def summary(self):

        total = len(self.trade_history)

        wins = len([t for t in self.trade_history if t["pnl"] > 0])

        losses = total - wins

        net_pnl = round(sum(t["pnl"] for t in self.trade_history), 2)

        win_rate = round((wins / total) * 100, 2) if total else 0

        return {
            "Total Trades": total,
            "Wins": wins,
            "Losses": losses,
            "Win Rate": win_rate,
            "Net PnL": net_pnl,
            "Open Trade": self.has_open_trade(),
        }
