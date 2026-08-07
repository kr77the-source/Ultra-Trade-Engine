# ==========================================
# Institutional Trade Engine
# File : live_data.py
# Version : 2.1 (Fixed Pandas Frequency)
# ==========================================

import pandas as pd
import numpy as np
from datetime import datetime
import config

class LiveDataManager:
    def __init__(self):
        self.live_mode = getattr(config, "LIVE_MODE", False)
        self.symbol = getattr(config, "DEFAULT_SYMBOL", "NSE:NIFTY 50")
        
    def get_latest_price(self):
        """Fetches real-time price if LIVE_MODE is True, otherwise returns mock price."""
        if self.live_mode:
            try:
                # TODO: Implement actual broker WebSocket/REST call here
                pass
            except Exception as e:
                print(f"Live feed error: {e}. Falling back to mock data.")
        
        # Mock / Dummy price generation
        base_price = 22000.00
        noise = np.random.uniform(-5, 5)
        return round(base_price + noise, 2)

    def get_historical_data(self, interval="15m", period="30d"):
        """Fetches real historical candles or generates mock OHLCV dataframe based on mode."""
        if self.live_mode:
            try:
                # TODO: Implement actual broker historical data API fetch here
                pass
            except Exception as e:
                print(f"Live historical data error: {e}. Using mock data.")

        # Map config intervals to valid Pandas frequency strings
        freq_map = {
            "1m": "1min",
            "5m": "5min",
            "15m": "15min",
            "30m": "30min",
            "1h": "1h",
            "1D": "1D"
        }
        pd_freq = freq_map.get(interval, "15min")

        # Fallback / Mock OHLCV DataFrame generator
        dates = pd.date_range(end=datetime.now(), periods=100, freq=pd_freq)
        np.random.seed(42)
        close = 22000 + np.cumsum(np.random.randn(100) * 20)
        high = close + np.random.uniform(2, 10, size=100)
        low = close - np.random.uniform(2, 10, size=100)
        open_p = low + (high - low) * np.random.uniform(0, 1, size=100)
        volume = np.random.randint(1000, 50000, size=100)

        df = pd.DataFrame({
            "Open": open_p,
            "High": high,
            "Low": low,
            "Close": close,
            "Volume": volume
        }, index=dates)

        return df

def fetch_live_feed():
    manager = LiveDataManager()
    return manager.get_latest_price()
