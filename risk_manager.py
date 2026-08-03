# ==========================================
# Institutional Trade Engine
# File : risk_manager.py
# Version : 1.0
# ==========================================

def calculate_trade(
    capital,
    entry,
    stop_loss,
    risk_percent=1.0,
    reward_ratio=2.0
):

    try:

        capital = float(capital)
        entry = float(entry)
        stop_loss = float(stop_loss)

        risk_amount = capital * (risk_percent / 100)

        risk_per_share = abs(entry - stop_loss)

        if risk_per_share <= 0:

            return None

        quantity = int(risk_amount / risk_per_share)

        target = round(
            entry + ((entry - stop_loss) * reward_ratio),
            2
        )

        capital_required = round(
            quantity * entry,
            2
        )

        trade_quality = "⭐⭐⭐⭐⭐"

        return {

            "entry": round(entry, 2),

            "stop_loss": round(stop_loss, 2),

            "target": target,

            "quantity": quantity,

            "risk_amount": round(risk_amount, 2),

            "capital_required": capital_required,

            "trade_quality": trade_quality

        }

    except Exception as e:

        print("Risk Manager Error :", e)

        return None


def allow_trade(confidence):

    if confidence >= 95:

        return True

    return False
