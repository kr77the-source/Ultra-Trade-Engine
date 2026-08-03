# ==========================================
# Institutional Trade Engine
# File : option_chain.py
# Version : 1.0
# ==========================================

from typing import Dict


def calculate_pcr(call_oi: float, put_oi: float) -> float:

    if call_oi <= 0:
        return 0.0

    return round(put_oi / call_oi, 2)


def option_chain_signal(
    call_oi: float,
    put_oi: float,
    call_change: float,
    put_change: float
) -> Dict:

    signal = "NO TRADE"
    confidence = 0

    pcr = calculate_pcr(call_oi, put_oi)

    # -----------------------------------
    # Bullish
    # -----------------------------------

    if (
        pcr > 1.10
        and put_change > call_change
    ):

        signal = "BUY"
        confidence = 90

    # -----------------------------------
    # Bearish
    # -----------------------------------

    elif (
        pcr < 0.90
        and call_change > put_change
    ):

        signal = "SELL"
        confidence = 90

    return {

        "signal": signal,

        "confidence": confidence,

        "pcr": pcr,

        "call_oi": call_oi,

        "put_oi": put_oi

    }
