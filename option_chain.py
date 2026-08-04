# ==========================================
# Institutional Trade Engine
# File : option_chain.py
# Version : 2.0
# ==========================================

from typing import Dict


# ==========================================
# Put Call Ratio
# ==========================================

def calculate_pcr(call_oi: float, put_oi: float) -> float:

    call_oi = max(float(call_oi), 0.0)
    put_oi = max(float(put_oi), 0.0)

    if call_oi == 0:
        return 0.0

    return round(put_oi / call_oi, 2)


# ==========================================
# OI Bias
# ==========================================

def oi_bias(call_oi: float, put_oi: float) -> str:

    if put_oi > call_oi:
        return "BULLISH"

    if call_oi > put_oi:
        return "BEARISH"

    return "NEUTRAL"


# ==========================================
# Option Chain Signal
# ==========================================

def option_chain_signal(
    call_oi: float,
    put_oi: float,
    call_change: float,
    put_change: float
) -> Dict:

    call_oi = float(call_oi)
    put_oi = float(put_oi)
    call_change = float(call_change)
    put_change = float(put_change)

    pcr = calculate_pcr(call_oi, put_oi)

    signal = "NO TRADE"
    confidence = 50
    reason = "Neutral Option Chain"

    # Strong Bullish

    if pcr >= 1.20 and put_change > call_change:

        signal = "BUY"
        confidence = 95
        reason = "High PCR with strong Put writing"

    # Moderate Bullish

    elif pcr >= 1.00 and put_change > call_change:

        signal = "BUY"
        confidence = 80
        reason = "Positive PCR"

    # Strong Bearish

    elif pcr <= 0.80 and call_change > put_change:

        signal = "SELL"
        confidence = 95
        reason = "Low PCR with Call writing"

    # Moderate Bearish

    elif pcr <= 0.95 and call_change > put_change:

        signal = "SELL"
        confidence = 80
        reason = "Negative PCR"

    return {

        "signal": signal,

        "confidence": confidence,

        "reason": reason,

        "pcr": pcr,

        "bias": oi_bias(call_oi, put_oi),

        "call_oi": round(call_oi, 2),

        "put_oi": round(put_oi, 2),

        "call_change": round(call_change, 2),

        "put_change": round(put_change, 2)

    }


# ==========================================
# Test
# ==========================================

if __name__ == "__main__":

    print(

        option_chain_signal(

            call_oi=120000,

            put_oi=185000,

            call_change=18000,

            put_change=42000

        )

    )
