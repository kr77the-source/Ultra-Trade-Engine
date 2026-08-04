# ==========================================
# Institutional Trade Engine
# File : scheduler.py
# Version : 6.0
# ==========================================

import time
from datetime import datetime

from engine import TradeEngine
from config import (
    MARKET_OPEN,
    LAST_ENTRY,
    AUTO_REFRESH_SECONDS
)


class MarketScheduler:

    def __init__(self):

        self.engine = TradeEngine()

        self.running = False


    def market_open(self):

        now = datetime.now().time()

        return MARKET_OPEN <= now <= LAST_ENTRY


    def run_once(self):

        if not self.market_open():

            return {

                "status": "MARKET CLOSED"

            }

        return self.engine.run()


    def start(self):

        self.running = True

        print("Market Scheduler Started")

        while self.running:

            result = self.run_once()

            print(result)

            time.sleep(AUTO_REFRESH_SECONDS)


    def stop(self):

        self.running = False

        print("Scheduler Stopped")
