# ==========================================
# Institutional Trade Engine
# File : risk_manager.py
# Version : 6.0
# ==========================================

import math


class RiskManager:

    def __init__(self, capital, risk_percent=1):

        self.capital = float(capital)
        self.risk_percent = float(risk_percent)

    # ---------------------------------------
    # Risk Amount
    # ---------------------------------------

    def risk_amount(self):

        return round(
            self.capital * self.risk_percent / 100,
            2
        )

    # ---------------------------------------
    # Position Size
    # ---------------------------------------

    def position_size(
        self,
        entry,
        stop_loss,
        lot_size=1
    ):

        entry = float(entry)
        stop_loss = float(stop_loss)
        lot_size = max(int(lot_size), 1)

        risk_per_unit = abs(entry - stop_loss)

        if risk_per_unit <= 0:
            return 0

        qty = self.risk_amount() / risk_per_unit

        qty = math.floor(qty / lot_size) * lot_size

        return max(qty, lot_size)

    # ---------------------------------------
    # Risk Reward
    # ---------------------------------------

    def risk_reward(
        self,
        entry,
        stop_loss,
        target
    ):

        risk = abs(float(entry) - float(stop_loss))
        reward = abs(float(target) - float(entry))

        if risk == 0:
            return 0.0

        return round(reward / risk, 2)

    # ---------------------------------------
    # Trade Validation
    # ---------------------------------------

    def validate_trade(
        self,
        confidence,
        rr
    ):

        if confidence < 85:
            return False, "Confidence below threshold"

        if rr < 2:
            return False, "Risk Reward below 1:2"

        return True, "Trade Approved"

    # ---------------------------------------
    # Capital at Risk %
    # ---------------------------------------

    def capital_at_risk(self):

        return round(self.risk_percent, 2)

    # ---------------------------------------
    # Update Capital
    # ---------------------------------------

    def update_capital(self, pnl):

        self.capital += float(pnl)

        if self.capital < 0:
            self.capital = 0

        return round(self.capital, 2)

    # ---------------------------------------
    # Summary
    # ---------------------------------------

    def summary(self):

        return {
            "capital": round(self.capital, 2),
            "risk_percent": round(self.risk_percent, 2),
            "risk_amount": self.risk_amount()
        }
