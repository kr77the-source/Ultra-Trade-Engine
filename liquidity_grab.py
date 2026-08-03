# ==========================================
# Institutional Trade Engine
# File : liquidity_grab.py
# Version : 1.0
# ==========================================


def detect_liquidity_grab(df, lookback=10):

    try:

        if len(df) < lookback + 2:

            return None


        previous_high = max(
            df["High"].iloc[-lookback-1:-1]
        )

        previous_low = min(
            df["Low"].iloc[-lookback-1:-1]
        )


        current = df.iloc[-1]


        signal = "NEUTRAL"

        confidence = 50

        reason = "No Liquidity Event"


        # --------------------------------
        # Bullish Liquidity Sweep
        # Price breaks low but closes back above
        # --------------------------------

        if (

            current["Low"] < previous_low

            and

            current["Close"] > previous_low

        ):

            signal = "BUY"

            confidence = 90

            reason = "Sell Side Liquidity Grab"



        # --------------------------------
        # Bearish Liquidity Sweep
        # Price breaks high but closes below
        # --------------------------------

        elif (

            current["High"] > previous_high

            and

            current["Close"] < previous_high

        ):

            signal = "SELL"

            confidence = 90

            reason = "Buy Side Liquidity Grab"



        return {

            "signal": signal,

            "confidence": confidence,

            "reason": reason,

            "previous_high": round(
                float(previous_high),
                2
            ),

            "previous_low": round(
                float(previous_low),
                2
            )

        }


    except Exception as e:

        print(
            "Liquidity Grab Error:",
            e
        )

        return None
