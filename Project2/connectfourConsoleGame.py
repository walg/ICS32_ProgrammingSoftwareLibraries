#Ray Chou 67255516 and Ford Tang 46564602
# ICS 32 Winter 2014
# Project #2: Send Me On My Way

#connectfourConsoleGame

import connectfour
import connectfour_game_functions

def menu() -> None:
    'This function is the main menu of the connect four console game'
    game = connectfour.new_game_state()
    winner = connectfour.NONE
    while winner == connectfour.NONE:  
        connectfour_game_functions.printBoard(game)
        game = connectfour_game_functions.directions_console(game)
        winner = connectfour.winning_player(game)
    connectfour_game_functions.printBoard(game)
    if winner == connectfour.RED:
        print('The winner is Red!')
    else:
        print('The winner is Yellow!')

if __name__ == '__main__':
    menu()
