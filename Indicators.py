import pandas as pd
import pandas_ta as ta
import numpy as np

#RSI indicator
def rsi(df, length=None):
    df["RSI"] = df.ta.rsi(length=length)
    return df["RSI"]

#Bollinger Bands
def bbands(df, length=None):
    bbands = df.ta.bbands(length=length)
    bbands.columns = ["lower", "mid", "upper", "broad", "perc"]
    df["lower"] = bbands["lower"]
    df["mid"] = bbands["mid"]
    df["upper"] = bbands["upper"]

    return bbands[["lower", "mid", "upper"]]