# ==========================================
# Institutional Trade Engine
# File : engine.py
# Version : 6.0
# ==========================================

import scanner
from validator import TradeValidator
from portfolio_manager import PortfolioManager
from paper_trading import PaperTrader


class TradeEngine:

    def __init__(self):

        self.validator = TradeValidator()

        self.portfolio = PortfolioManager()

        self.paper = PaperTrader()


    def run(self):

        trade = scanner.get_best_trade()

        if trade is None:

            return {

                "status": "NO TRADE",

                "reason": "Scanner returned no setup"

            }


        validation = self.validator.validate({

            "signal": trade["signal"],

            "confidence": trade["confidence"],

            "pdh": trade["modules"]["pdh"],

            "smart_money": trade["modules"]["smart_money"],

            "order_block": trade["modules"]["order_block"],

            "liquidity": trade["modules"]["liquidity"],

            "multi_timeframe": trade["modules"]["multi_timeframe"],

            "option_chain": trade["modules"]["option_chain"],

            "global": trade["modules"]["global"],

            "volume_ok": trade["modules"]["volume_ok"],

            "risk_reward": trade["setup"]["risk_reward"]

        })


        if not validation["approved"]:

            return validation


        approved, reason = self.portfolio.can_take_trade(

            trade["symbol"],

            trade["setup"]["entry"]

        )


        if not approved:

            return {

                "status": "NO TRADE",

                "reason": reason

            }


        setup = trade["setup"]


        self.paper.create_trade(

            trade["symbol"],

            trade["signal"],

            setup["entry"],

            setup["stop_loss"],

            setup["target_1"],

            setup["target_2"],

            setup["quantity"],

            trade["confidence"]

        )


        self.portfolio.add_trade(

            trade["symbol"],

            setup["entry"]

        )


        return {

            "status": "TRADE APPROVED",

            "trade": trade

        }
