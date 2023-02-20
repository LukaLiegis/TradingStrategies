"""
Building a trading strategy that uses bollinger bands and RSI to trade.  And include a backtest.
"""

#from dataset import *
from
from
from Indicators import *
from Functions import *

def crossover(series, value):
    """
    Returns true if series crosses the value
    """
    return True if series.iloc[-1] > value and series.iloc[-2] < value else False

class BollingerRSI(Strategy):

    tp_perc = 20 # Take profit percentage
    sl_perc = 5 # Stop loss percentage

    rsi_exits = [25, 75]

    def __int__(self):
        self.rsi = self.I(rsi, self.data.df)
        self.bb = self.I(bbands, self.data.df)

    def __next__(self):
        index = len(self.rsi) - 1

        """if not in a position"""
        if not self.position:
            """Check long"""
            if self.rsi < 30 and touching("bottom", self.data.df.iloc[:index]):
                self.buy(tp = self.data.Close + (self.data.Close * (self.tp_perc/100)),
                         sl = self.data.Close - (self.data.Close * (self.sl_perc/100)))

            """Check short"""
            if self.rsi > 70 and touching("top", self.data.df.iloc[:index]):
                self.sell(tp = self.data.Close - (self.data.Close * (self.tp_perc/100)),
                         sl = self.data.Close + self.data.Close * (self.sl_perc/100)))

            """If in a position already"""
            if self.positions:

                """Check long"""
                if self.position.is_long:
                    if crossover(self.rsi, self.rsi_exits[0]):
                        self.position.close()

                """Check short"""
                if self.position.is_long:
                    if crossover(self.rsi_exits[1], self.rsi):\
                        self.position.close()
