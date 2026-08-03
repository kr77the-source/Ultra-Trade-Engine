# ==========================================
# Institutional Trade Engine
# File : indicators.py
# Version : 4.0
# ==========================================

import yfinance as yf


def get_data(symbol, period="30d", interval="15m"):

    try:

        df = yf.download(

            symbol,

            period=period,

            interval=interval,

            progress=False,

            auto_adjust=False

        )

        if df.empty:

            return None


        return df


    except Exception as e:

        print("Data Error:", e)

        return None



# ==========================================
# VWAP
# ==========================================

def get_vwap(symbol):

    try:

        df = get_data(
            symbol,
            "5d",
            "15m"
        )


        if df is None:

            return None


        price = (

            df["High"]
            +
            df["Low"]
            +
            df["Close"]

        ) / 3


        volume = df["Volume"]


        vwap = (

            price * volume

        ).cumsum() / volume.cumsum()


        return round(

            float(vwap.iloc[-1]),

            2

        )


    except Exception as e:

        print("VWAP Error:", e)

        return None



# ==========================================
# EMA
# ==========================================

def get_ema(symbol):

    try:

        df = get_data(
            symbol,
            "30d",
            "15m"
        )


        if df is None:

            return None


        ema20 = (

            df["Close"]

            .ewm(
                span=20
            )

            .mean()

        )


        ema50 = (

            df["Close"]

            .ewm(
                span=50
            )

            .mean()

        )


        return {

            "ema20": round(

                float(ema20.iloc[-1]),

                2

            ),

            "ema50": round(

                float(ema50.iloc[-1]),

                2

            )

        }


    except Exception as e:

        print("EMA Error:", e)

        return None



# ==========================================
# CPR
# ==========================================

def get_cpr(symbol):

    try:

        df = get_data(

            symbol,

            "10d",

            "1d"

        )


        if df is None or len(df)<2:

            return None


        prev = df.iloc[-2]


        high = float(prev["High"])

        low = float(prev["Low"])

        close = float(prev["Close"])


        pivot = (

            high +
            low +
            close

        ) / 3


        bc = (

            high +
            low

        ) / 2


        tc = (

            pivot -
            bc

        ) + pivot


        return {

            "pivot": round(pivot,2),

            "bc": round(bc,2),

            "tc": round(tc,2)

        }


    except Exception as e:

        print("CPR Error:", e)

        return None



# ==========================================
# ATR
# ==========================================

def get_atr(symbol, period=14):

    try:

        df = get_data(

            symbol,

            "30d",

            "15m"

        )


        if df is None:

            return None


        high = df["High"]

        low = df["Low"]

        close = df["Close"]


        prev_close = close.shift(1)


        tr1 = high - low

        tr2 = abs(
            high - prev_close
        )

        tr3 = abs(
            low - prev_close
        )


        tr = tr1.combine(

            tr2,

            max

        ).combine(

            tr3,

            max

        )


        atr = tr.rolling(

            period

        ).mean()



        return round(

            float(atr.iloc[-1]),

            2

        )


    except Exception as e:

        print("ATR Error:", e)

        return None
