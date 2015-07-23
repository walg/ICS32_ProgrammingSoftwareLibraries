# Ford Tang / 465646402
# download_quotes.py

import http.client
import urllib.request
import urllib.error
from collections import namedtuple

def get_quotes(symbol:str, start:str, end:str) -> list:
    ''' Retrieves stock quotes from yahoo and returns the data in the form of a numedtuple, with a date and the
        corresponding closing price
    '''
    start = start.split('-')
    end = end.split('-')
    quotes = urllib.request.urlopen('http://ichart.yahoo.com/table.csv?s=' + symbol
                                    + '&a=' + str(int(start[1]) - 1)
                                    + '&b=' + start[2]
                                    + '&c=' + start[0]
                                    + '&d=' + str(int(end[1]) - 1)
                                    + '&e=' + end[2]
                                    + '&f=' + end[0]
                                    + '&g=d')
    content_bytes = quotes.read()
    content_string = content_bytes.decode(encoding='utf-8')
    content_lines = content_string.splitlines()
    quotes_list = []
    for line in range(len(content_lines)):
        current_line = content_lines[line]
        current_line = current_line.split(',')
        if line == 0:
            stocks = namedtuple('stocks', [current_line[0], current_line[4]])
        else:
            quotes_list.append(stocks(current_line[0], current_line[4]))
            
    quotes_list.reverse()
    
    return quotes_list
