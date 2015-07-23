# Ford Tang / 465646402
# signals.py

# This module defines two classes called:
#   simple_moving_average_signal and directional_signal

# These signals:
#   * When signals are first initialized, they require an integer for
#       the number of days to analyze.  Also, for directional_signal,
#       two floats for the buy and sell thresholds will be required.
#   * Signals have an execute command that will take a list of stocks
#       and return a dictionary with the values of the signals
#       belonging to date keys.

import indicators

class simple_moving_average:
    def __init__(self, days:int) -> None:
        self._days = days
        return None

    def execute(self, stocks:list) -> dict:
        ''' Generates a BUY or SELL signal and returns the result in
            a dictionary.
        '''
        sma_indicator = indicators.simple_moving_average(self._days)
        stock_indicators = sma_indicator.execute(stocks)
        signals = {}
        for index in range(len(stocks)):
            if index < self._days:
                signals[stocks[index].Date] = ''
            elif stock_indicators[stocks[index - 1].Date] != '':
                if (float(stocks[index].Close) > float(stock_indicators[stocks[index].Date])) and (float(stocks[index - 1].Close) < float(stock_indicators[stocks[index - 1].Date])):
                    signals[stocks[index].Date] = 'BUY'
                elif (float(stocks[index].Close) < float(stock_indicators[stocks[index].Date])) and (float(stocks[index - 1].Close) > float(stock_indicators[stocks[index - 1].Date])):
                    signals[stocks[index].Date] = 'SELL'
                else:
                    signals[stocks[index].Date] = ''
            else:
                signals[stocks[index].Date] = ''
        return signals

class directional:
    def __init__(self, days:int, buy:float, sell:float) -> None:
        self._days = days
        self._buy = buy
        self._sell = sell
        return None

    def execute(self, stocks:list) -> dict:
        ''' Generates a BUY or SELL signal and returns the result in
            a dictionary.
        '''
        dir_indicator = indicators.directional(self._days)
        stock_indicators = dir_indicator.execute(stocks)
        signals = {}
        for index in range(len(stocks)):
            if index <= self._days:
                signals[stocks[index].Date] = ''
            elif int(stock_indicators[stocks[index].Date]) > self._buy:
                if int(stock_indicators[stocks[index - 1].Date]) < self._buy:
                    signals[stocks[index].Date] = 'BUY'
                else:
                    signals[stocks[index].Date] = ''
            elif int(stock_indicators[stocks[index].Date]) < self._sell:
                if int(stock_indicators[stocks[index - 1].Date]) > self._sell:
                    signals[stocks[index].Date] = 'SELL'
                else:
                    signals[stocks[index].Date] = ''
            else:
                signals[stocks[index].Date] = ''
        return signals
