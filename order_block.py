# ==========================================
# Institutional Trade Engine
# File : order_block.py
# Version : 1.0
# ==========================================


def detect_order_block(df, lookback=20):

    try:

        if len(df) < lookback:

            return None


        blocks = []


        for i in range(
            len(df)-lookback,
            len(df)-1
        ):

            candle = df.iloc[i]

            next_candle = df.iloc[i+1]


            # Bullish Order Block
            # Red candle followed by strong bullish move

            if (

                candle["Close"] < candle["Open"]

                and

                next_candle["Close"] > candle["High"]

            ):

                blocks.append({

                    "type": "DEMAND",

                    "high": float(candle["High"]),

                    "low": float(candle["Low"])

                })


            # Bearish Order Block
            # Green candle followed by strong bearish move

            elif (

                candle["Close"] > candle["Open"]

                and

                next_candle["Close"] < candle["Low"]

            ):

                blocks.append({

                    "type": "SUPPLY",

                    "high": float(candle["High"]),

                    "low": float(candle["Low"])

                })


        if len(blocks) == 0:

            return {

                "signal": "NEUTRAL",

                "confidence": 50

            }


        last_block = blocks[-1]


        current_price = float(
            df["Close"].iloc[-1]
        )


        signal = "NEUTRAL"

        confidence = 50


        if last_block["type"] == "DEMAND":

            if current_price >= last_block["low"]:

                signal = "BUY"

                confidence = 85



        elif last_block["type"] == "SUPPLY":

            if current_price <= last_block["high"]:

                signal = "SELL"

                confidence = 85



        return {

            "signal": signal,

            "confidence": confidence,

            "zone": last_block

        }


    except Exception as e:

        print(
            "Order Block Error:",
            e
        )

        return None
