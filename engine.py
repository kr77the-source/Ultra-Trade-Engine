# ==========================================
# Institutional Trade Engine
# File : engine.py (With Trade Signals)
# ==========================================

from live_data import LiveDataManager
import config
import numpy as np

class TradingEngine:
    def __init__(self):
        self.data_manager = LiveDataManager()

    def get_market_data(self):
        latest_price = self.data_manager.get_latest_price()
        historical_df = self.data_manager.get_historical_data(
            interval=config.DEFAULT_INTERVAL,
            period=config.DEFAULT_PERIOD
        )
        return latest_price, historical_df

    def run_cycle(self):
        price, df = self.get_market_data()
        
        # Dummy / Strategy Scoring Logic (Yahan aap apne indicators ki logic jod sakte hain)
        np.random.seed(int(price) % 100)
        confidence_score = np.random.randint(60, 95)
        
        signal = "WAIT / NO TRADE"
        if confidence_score >= config.MIN_CONFIDENCE:
            signal = "BUY CALL (CE)" if np.random.rand() > 0.5 else "BUY PUT (PE)"
        
        trade_setup = {
            "Price": price,
            "Signal": signal,
            "Confidence": f"{confidence_score}%",
            "StopLoss": round(price - 50, 2),
            "Target1": round(price + 100, 2),
            "Target2": round(price + 150, 2)
        }
        
        return trade_setup, df
