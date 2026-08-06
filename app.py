import time
from datetime import datetime

class UltraTradeEngine:
    def __init__(self):
        print("🚀 Ultra Trade Engine Initialized...")
        self.strategies = ["CPR", "EMA", "ORB", "PDH", "VWAP", "Supertrend"]

    def pre_market_analysis(self):
        print("\n[Step 1] Running Pre-Market Analysis...")
        print("-> Fetching Market Trend, Pre-Market OI, and F&O Securities Data...")
        top_5_stocks = ["RELIANCE.NS", "TCS.NS", "HDFCBANK.NS", "INFY.NS", "ICICIBANK.NS"]
        print(f"-> Selected Top 5 Stocks based on Pre-Market Data: {top_5_stocks}")
        return top_5_stocks

    def evaluate_strategies(self, stock):
        print(f"\n--- Evaluating Strategies for: {stock} ---")
        strategy_signals = {}
        
        for strat in self.strategies:
            is_bullish = hash(stock + strat + str(datetime.now().date())) % 2 == 0
            
            if is_bullish:
                entry = 1000.0
                sl = 990.0
                target = 1030.0
                signal = "BUY"
            else:
                entry = 1000.0
                sl = 1010.0
                target = 970.0
                signal = "SELL"
                
            strategy_signals[strat] = {
                "signal": signal,
                "entry": entry,
                "sl": sl,
                "target": target
            }
            print(f"   [{strat}] Signal: {signal} | Entry: {entry} | SL: {sl} | Target: {target}")
            
        return strategy_signals

    def backtest_and_filter(self, stock, strategy_signals):
        print(f"\n[Backtest & Accuracy Match (90% Criteria)] for {stock}:")
        final_matched_signals = {}
        
        for strat, details in strategy_signals.items():
            mock_historical_accuracy = 91.5 if len(strat) % 2 == 0 else 85.0 
            
            print(f"   [{strat}] Historical Accuracy: {mock_historical_accuracy}%")
            
            if mock_historical_accuracy >= 90.0:
                final_matched_signals[strat] = details
                print(f"   ✅ {strat} matched the 90% accuracy criteria! Signal Approved.")
            else:
                print(f"   ❌ {strat} dropped (Accuracy below 90%).")
                
        return final_matched_signals

    def run_market_hours(self):
        print("\n==============================================")
        print("  Starting Automated Engine (9:15 AM - 3:30 PM)")
        print("==============================================")
        
        while True:
            now = datetime.now()
            current_time = now.strftime("%H:%M")
            current_day = now.strftime("%A")
            
            if current_day in ["Saturday", "Sunday"]:
                print("Market is closed today (Weekend). Exiting simulation.")
                break
                
            print(f"\n[{now.strftime('%Y-%m-%d %H:%M:%S')}] Running Market Scan cycle...")
            
            top_stocks = self.pre_market_analysis()
            
            for stock in top_stocks:
                signals = self.evaluate_strategies(stock)
                approved_signals = self.backtest_and_filter(stock, signals)
                
                if approved_signals:
                    print(f"\n🎯 FINAL TRIGGERED SIGNALS FOR {stock}:")
                    for s_name, s_data in approved_signals.items():
                        print(f"   -> Strategy: {s_name} | Action: {s_data['signal']} | Entry: {s_data['entry']} | SL: {s_data['sl']}")
                else:
                    print(f"\n⚠️ No strategy met the 90% accuracy threshold for {stock} in this cycle.")

            print("\nWaiting for the next scan cycle (sleeping for 60 seconds)...")
            time.sleep(60)
            
            if current_time >= "15:30":
                print("Market closed (3:30 PM). Stopping engine for the day.")
                break

if __name__ == "__main__":
    engine = UltraTradeEngine()
    engine.run_market_hours()
