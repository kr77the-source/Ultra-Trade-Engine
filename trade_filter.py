# ==========================================
# Institutional Trade Engine
# File : trade_filter.py
# Version : 6.0
# ==========================================

from datetime import datetime
from config import (
    MARKET_OPEN,
    NO_TRADE_BEFORE,
    LAST_ENTRY,
    MIN_CONFIDENCE
)


class TradeFilter:

    def __init__(self):
        pass

    # -----------------------------
    # Market Timing Filter
    # -----------------------------
    def check_market_time(self):

        now = datetime.now().time()

        if now < NO_TRADE_BEFORE:
            return False, "Waiting for first 3 candles"

        if now > LAST_ENTRY:
            return False, "No new entries after cutoff"

        return True, "Market timing OK"

    # -----------------------------
    # Confidence Filter
    # -----------------------------
    def check_confidence(self, confidence):

        if confidence < MIN_CONFIDENCE:
            return False, "Confidence below threshold"

        return True, "Confidence OK"

    # -----------------------------
    # Risk Reward Filter
    # -----------------------------
    def check_rr(self, rr):

        if rr < 2.0:
            return False, "Risk Reward less than 1:2"

        return True, "Risk Reward OK"

    # -----------------------------
    # Volume Filter
    # -----------------------------
    def check_volume(self, current_volume, average_volume):

        if average_volume <= 0:
            return False, "Invalid average volume"

        ratio = current_volume / average_volume

        if ratio < 1.5:
            return False, "Low volume"

        return True, "Volume confirmed"

    # -----------------------------
    # Final Filter
    # -----------------------------
    def approve_trade(
        self,
        confidence,
        rr,
        current_volume,
        average_volume
    ):

        checks = []

        checks.append(self.check_market_time())
        checks.append(self.check_confidence(confidence))
        checks.append(self.check_rr(rr))
        checks.append(
            self.check_volume(
                current_volume,
                average_volume
            )
        )

        failed = [msg for ok, msg in checks if not ok]

        if failed:
            return {
                "approved": False,
                "reason": " | ".join(failed)
            }

        return {
            "approved": True,
            "reason": "All filters passed"
        }
