# Ford Tang / 465646402
# Project3.py

import download_quotes
import indicators
import signals
from datetime import date

def menu() -> None:
    '''Menu for program
    '''
    while True:
        symbol = _get_symbol()
        start_date = _get_start_date()
        end_date = _get_end_date(start_date)
        strategy = _strategy_choice()
        days =_get_days()
        buy = 0
        sell = 0
        try:
            stocks = download_quotes.get_quotes(symbol, start_date, end_date)
            break
        except:
            print('Could not download stock quotes!')
    indicator = ''
    signal = ''
    indicator_result = ''
    signal_result = ''
    if strategy == 'Directional':
        print('Buy threshold')
        buy = _get_threshold()
        print('Sell threshold')
        sell = _get_threshold()
        indicator = indicators.directional(days)
        signal = signals.directional(days, buy, sell)
        indicator_result = indicator.execute(stocks)
        signal_result = signal.execute(stocks)
    else:
        indicator = indicators.simple_moving_average(days)
        signal = signals.simple_moving_average(days)
        indicator_result = indicator.execute(stocks)
        signal_result = signal.execute(stocks)
    _print_report(symbol, strategy, days, buy, sell, stocks, indicator_result, signal_result)
    return None

def _get_symbol() -> str:
    '''Function gets ticker symbol and returns it as a string
    '''
    return input('Please enter the ticker symbol:  ').strip().upper()

def _get_start_date() -> str:
    '''Function gets the start date and checks if it is valid
    '''
    while True:
        try:
            entered_date = (input('Please enter the start date in the format yyyy-mm-dd:  ')).strip()
            check_date = entered_date.split('-')
            if date(int(check_date[0]), int(check_date[1]), int(check_date[2])) <= date.today() and len(check_date[0]) == 4 and len(check_date[1]) == 2 and len(check_date[2]) == 2:
                return entered_date
            else:
                print('Date is invalid, please try again.')
        except:
            print('Date is invalid, please try again.')

def _get_end_date(start_date:str) -> str:
    '''Function gets the end date and checks if it is valid
    '''
    while True:
        try:
            entered_date = (input('Please enter the end date in the format yyyy-mm-dd:  ')).strip()
            check_end_date = entered_date.split('-')           
            check_start_date = start_date.split('-')
            if date(int(check_end_date[0]), int(check_end_date[1]), int(check_end_date[2])) <= date.today() and date(int(check_end_date[0]), int(check_end_date[1]), int(check_end_date[2])) >= date(int(check_start_date[0]), int(check_start_date[1]), int(check_start_date[2])) and len(check_end_date[0]) == 4 and len(check_end_date[1]) == 2 and len(check_end_date[2]) == 2:
                return entered_date
            else:
                print('Date is invalid, please try again.')
        except:
            print('Date is invalid, please try again.')

def _get_threshold() -> int:
    '''Function gets the threshold value and returns it as an integer.
    '''
    while True:
        try:
            threshold = int(input('Please enter the threshold:  '))
            return threshold
        except:
            print('Invalid input, please try again.')

def _get_days() -> int:
    '''Function gets the days to run the strategy and returns it as an
        integer
    '''
    try:
        days = int(input('Please enter the number of days for the strategy:  '))
        return days
    except:
        print('Invalid input, please try again.')

def _strategy_choice() -> str:
    '''Function returns the desired strategy choice as either
    'Directional' or 'Simple Moving Average'
    '''
    while True:
        choice = input('Signal Strategy Option:\n[S]imple Moving Average\nor\n[D]irectional\n').lower()
        if choice == 's':
            return 'Simple Moving Average'
        elif choice == 'd':
            return 'Directional'
        else:
            print('invalid input, please try again.')

def _print_report(symbol:str, strategy:str, days:int, buy:int, sell:int, stocks:list, indicator_result:dict, signal_result:dict) -> None:
    '''Function prints out the result of the analysis
    '''
    print('\nSYMBOL:  ' + symbol)
    if strategy == 'Directional':
        if buy > 0:
            buy = "+" + str(buy)
        else:
            buy = str(buy)
        if sell > 0:
            sell = "+" + str(sell)
        else:
            sell = str(sell)
        print('STRATEGY:  ' + strategy + ' (' + str(days) + '-day), buy above ' + buy +', sell below ' + sell + '\n')        
    else:
        print('STRATEGY:  ' + strategy + ' (' + str(days) + '-day)\n')
    print('{}\t\t{}\t\t{}\t{}'.format('DATE', 'CLOSE', 'INDICATOR', 'SIGNAL'))
    for index in range(len(stocks)):
        print('{}\t{}\t\t{}\t\t{}'.format(stocks[index].Date, stocks[index].Close, indicator_result[stocks[index].Date], signal_result[stocks[index].Date]))
        
    return None

if __name__=='__main__':
    menu()
