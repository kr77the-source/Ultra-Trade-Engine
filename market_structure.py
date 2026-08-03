# ==========================================
# Institutional Trade Engine
# File : market_structure.py
# Version : 1.0
# ==========================================


def detect_market_structure(df, lookback=5):

    try:

        highs = df["High"].tolist()

        lows = df["Low"].tolist()

        close = df["Close"].tolist()


        if len(df) < lookback + 2:

            return None


        last_high = max(
            highs[-lookback-1:-1]
        )

        last_low = min(
            lows[-lookback-1:-1]
        )


        current_close = close[-1]


        signal = "NEUTRAL"

        structure = "NONE"

        confidence = 50


        # Break Of Structure - Bullish

        if current_close > last_high:

            signal = "BUY"

            structure = "BOS BULLISH"

            confidence = 90


        # Break Of Structure - Bearish

        elif current_close < last_low:

            signal = "SELL"

            structure = "BOS BEARISH"

            confidence = 90



        # Trend Structure

        else:

            previous_high = highs[-2]

            previous_low = lows[-2]


            if (
                highs[-1] > previous_high
                and lows[-1] > previous_low
            ):

                structure = "HIGHER HIGH + HIGHER LOW"

                signal = "BUY"

                confidence = 75


            elif (

                highs[-1] < previous_high
                and lows[-1] < previous_low

            ):

                structure = "LOWER HIGH + LOWER LOW"

                signal = "SELL"

                confidence = 75



        return {

            "signal": signal,

            "structure": structure,

            "confidence": confidence,

            "last_high": round(float(last_high),2),

            "last_low": round(float(last_low),2)

        }


    except Exception as e:

        print(
            "Market Structure Error:",
            e
        )

        return None
