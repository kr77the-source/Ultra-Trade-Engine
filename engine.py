# ==========================================
# Institutional Trade Engine
# File : engine.py (Real Market Auto-Signals)
# ==========================================

from live_data import LiveDataManager
import config
import pandas as pd

class TradingEngine:
    def __init__(self):
        self.data_manager = LiveDataManager()

    def run_cycle(self):
        # Fetch absolute real live price and candles
        price = self.data_manager.get_latest_price()
        df = self.data_manager.get_historical_data(
            interval=config.DEFAULT_INTERVAL,
            period=config.DEFAULT_PERIOD
        )
        
        # Calculate real technical indicators (EMA 20 & EMA 50) on real data
        df['EMA20'] = df['Close'].ewm(span=20, adjust=False).mean()
        df['EMA50'] = df['Close'].ewm(span=50, adjust=False).mean()
        
        latest_ema20 = df['EMA20'].iloc[-1]
        latest_ema50 = df['EMA50'].iloc[-1]
        
        # Real Market Logic
        if latest_ema20 > latest_ema50:
            signal = "BUY CALL (CE) - Bullish Trend"
        else:
            signal = "BUY PUT (PE) - Bearish Trend"
            
        # Calculate real risk management levels based on actual volatility (ATR approximation)
        volatility = (df['High'] - df['Low']).mean()
        
        trade_setup = {
            "Price": price,
            "Signal": signal,
            "StopLoss": round(price - (volatility * 1.5), 2),
            "Target1": round(price + (volatility * 2.0), 2),
            "Target2": round(price + (volatility * 3.0), 2)
        }
        
        return trade_setup, df
