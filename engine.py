# ==========================================
# Institutional Trade Engine
# File : engine.py
# ==========================================

from live_data import LiveDataManager
import config

class TradingEngine:
    def __init__(self):
        self.data_manager = LiveDataManager()
        print(f"Engine Initialized. Mode -> LIVE_MODE: {config.LIVE_MODE}")

    def get_market_data(self):
        """Fetches latest price and historical candles using LiveDataManager."""
        latest_price = self.data_manager.get_latest_price()
        historical_df = self.data_manager.get_historical_data(
            interval=config.DEFAULT_INTERVAL,
            period=config.DEFAULT_PERIOD
        )
        return latest_price, historical_df

    def run_cycle(self):
        """Main execution cycle for analysis and trade setup."""
        price, df = self.get_market_data()
        print(f"[{config.DEFAULT_SYMBOL}] Current Price: {price}")
        # Add your indicator calculations and strategy scoring logic here
        return price, df
