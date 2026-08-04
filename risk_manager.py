# ==========================================
# Institutional Trade Engine
# File : risk_manager.py
# Version : 5.0
# ==========================================

import math


class RiskManager:

    def __init__(

        self,

        capital,

        risk_percent=1

    ):

        self.capital = capital

        self.risk_percent = risk_percent


    def risk_amount(self):

        return (

            self.capital *

            self.risk_percent /

            100

        )


    def position_size(

        self,

        entry,

        stop_loss,

        lot_size=1

    ):

        risk = abs(

            entry -

            stop_loss

        )

        if risk <= 0:

            return 0


        qty = (

            self.risk_amount()

            /

            risk

        )

        qty = math.floor(

            qty /

            lot_size

        ) * lot_size


        return max(

            qty,

            lot_size

        )


    def risk_reward(

        self,

        entry,

        stop_loss,

        target

    ):

        risk = abs(

            entry -

            stop_loss

        )

        reward = abs(

            target -

            entry

        )

        if risk == 0:

            return 0

        return round(

            reward /

            risk,

            2

        )


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
