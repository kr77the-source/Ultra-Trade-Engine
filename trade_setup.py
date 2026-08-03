# ==========================================
# Institutional Trade Engine
# File : trade_setup.py
# Version : 1.0
# ==========================================


def create_trade_setup(
    signal,
    entry,
    atr,
    capital,
    risk_percent=1
):

    try:

        if signal == "NO TRADE":

            return {

                "status": "NO TRADE"

            }


        risk_amount = (
            capital *
            risk_percent /
            100
        )


        # -----------------------------
        # BUY Setup
        # -----------------------------

        if signal == "BUY":


            stop_loss = round(

                entry -
                (atr * 1.5),

                2

            )


            target1 = round(

                entry +
                (atr * 2),

                2

            )


            target2 = round(

                entry +
                (atr * 3),

                2

            )


        # -----------------------------
        # SELL Setup
        # -----------------------------

        elif signal == "SELL":


            stop_loss = round(

                entry +
                (atr * 1.5),

                2

            )


            target1 = round(

                entry -
                (atr * 2),

                2

            )


            target2 = round(

                entry -
                (atr * 3),

                2

            )


        else:

            return None



        risk_per_unit = abs(

            entry -
            stop_loss

        )


        if risk_per_unit == 0:

            quantity = 0

        else:

            quantity = int(

                risk_amount /
                risk_per_unit

            )


        return {


            "status": "TRADE READY",


            "signal": signal,


            "entry": round(
                entry,
                2
            ),


            "stop_loss": stop_loss,


            "target_1": target1,


            "target_2": target2,


            "quantity": quantity,


            "risk_amount": round(
                risk_amount,
                2
            ),


            "risk_reward": "1:2.5"


        }


    except Exception as e:

        print(
            "Trade Setup Error:",
            e
        )

        return None
