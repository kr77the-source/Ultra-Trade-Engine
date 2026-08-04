# ==========================================
# Institutional Trade Engine
# File : validator.py
# Version : 6.0
# ==========================================


class TradeValidator:

    def __init__(self):

        self.minimum_confidence = 85

        self.minimum_rr = 2.0


    def validate(self, data):

        failed = []


        # -------------------------
        # AI Confidence
        # -------------------------

        if data["confidence"] < self.minimum_confidence:

            failed.append("Low Confidence")


        # -------------------------
        # PDH / PDL
        # -------------------------

        if data["pdh"]["signal"] != data["signal"]:

            failed.append("PDH Confirmation Failed")


        # -------------------------
        # Smart Money
        # -------------------------

        if data["smart_money"]["signal"] != data["signal"]:

            failed.append("Smart Money Failed")


        # -------------------------
        # Order Block
        # -------------------------

        if data["order_block"]["signal"] != data["signal"]:

            failed.append("Order Block Failed")


        # -------------------------
        # Liquidity Grab
        # -------------------------

        if data["liquidity"]["signal"] != data["signal"]:

            failed.append("Liquidity Failed")


        # -------------------------
        # Multi Time Frame
        # -------------------------

        if data["multi_timeframe"]["signal"] != data["signal"]:

            failed.append("MTF Failed")


        # -------------------------
        # Option Chain
        # -------------------------

        if data["option_chain"]["signal"] != data["signal"]:

            failed.append("Option Chain Failed")


        # -------------------------
        # Global Market
        # -------------------------

        if data["global"]["signal"] != data["signal"]:

            failed.append("Global Market Failed")


        # -------------------------
        # Volume
        # -------------------------

        if not data["volume_ok"]:

            failed.append("Volume Low")


        # -------------------------
        # Risk Reward
        # -------------------------

        if data["risk_reward"] < self.minimum_rr:

            failed.append("Risk Reward < 1:2")


        # -------------------------
        # Final Decision
        # -------------------------

        if len(failed) == 0:

            return {

                "approved": True,

                "status": "TRADE APPROVED",

                "reason": "All Filters Passed"

            }


        return {

            "approved": False,

            "status": "NO TRADE",

            "reason": failed

        }
