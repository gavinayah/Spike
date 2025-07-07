def is_valid_signal(rsi4, rsi6, cci, rsi_m5, asset):
    if "Boom" in asset:
        return rsi4 < 8 and rsi6 < 10 and cci < -120 and rsi_m5 < 30
    elif "Crash" in asset:
        return rsi4 > 95 and rsi6 > 90 and cci > 120 and rsi_m5 > 70
    return False
