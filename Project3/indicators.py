# Ford Tang / 465646402
# indicators.py

# This module defines two classes called:
#   simple_moving_average_indicator and directional_indicator.

# These indicators:
#   * When indicators are first initialized, they require an integer
#       for the number of days it will be analyzing
#   * Indicators have an execute command that will take a list of
#       stocks and return a dictionary with the values of the
#       indicators belonging to date keys.

class simple_moving_average:
    def __init__(self, days:int) -> None:
        self._days = days
        return None

    def execute(self, stocks:list) -> dict:
        ''' Determines the simple moving average over a range of days
            and returns the result in a dictionary.
        '''
        indicators = {}

        for index in range(len(stocks)):
            if index < self._days - 1:
                indicators[stocks[index].Date] = ''
            else:
                total = 0
                for day in range(self._days):
                    total += float(stocks[index - day].Close)         
                indicators[stocks[index].Date] = "{:.2f}".format((total/self._days))
                
        return indicators
         
class directional:
    def __init__(self, days:int) -> None:
        self._days = days
        return None
    
    def execute(self, stocks:list):
        ''' Determines the directional indicator over a range of days
            and returns the result in a dictionary.
        '''
        indicators = {}

        for index in range(len(stocks)):
            if index == 0:
                indicators[stocks[index].Date] = 0
            else:
                total = 0
                for day in range(self._days):
                    if index - day >= 1:
                        if float(stocks[index - day].Close) > float(stocks[index - day - 1].Close):
                            total += 1                        
                        elif float(stocks[index - day].Close) < float(stocks[index - day - 1].Close):
                            total -= 1
                if total > 0:
                    indicators[stocks[index].Date] = "+{}".format(total)
                else:
                    indicators[stocks[index].Date] = "{}".format(total)

        return indicators
