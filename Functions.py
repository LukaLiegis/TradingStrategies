from datetime import time
import pandas as pd

def touching(side, candles):
    """
    Returns true if the price is in close proximity to the bband side
    side parameter is either the top ot bottom, indicating which bband to check against
    """

    lower = candles["lower"].iloc[-1] # bottom bollinger band line
    upper = candles["upper"].iloc[-1] # top bollinger band

    high = candles["High"].iloc[-1] # current high
    low = candles["Low"].iloc[-1] # current low

    """Return true if the last candle crossed the bollinger band line"""
    if side == "top":
        if high > upper and low < upper:
            return True
        else:
            if high > lower and low < lower:
                return False