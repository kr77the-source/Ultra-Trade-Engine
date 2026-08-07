# ==========================================
# Institutional Trade Engine
# File : app.py
# ==========================================

import time
import config
from engine import TradingEngine

def main():
    print("=" * 50)
    print(f"Starting {config.APP_NAME} v{config.VERSION}")
    print(f"Target Symbol : {config.DEFAULT_SYMBOL}")
    print(f"Live Trading  : {config.LIVE_MODE}")
    print("=" * 50)

    engine = TradingEngine()

    try:
        while True:
            engine.run_cycle()
            time.sleep(config.AUTO_REFRESH_SECONDS)
    except KeyboardInterrupt:
        print("\nTrade Engine stopped safely by user.")

if __name__ == "__main__":
    main()
