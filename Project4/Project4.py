# Ford Tang / 46564602

# Project #4: The Width of a Circle (Part 1)

# Project4.py

# This is the main file for Project 4 that will create an othello game on the console.

import Othello
import othello_ai


def play_game() -> None:
    """
    This function runs the othello game on the console.
    :rtype : None
    """
    while True:
        _banner()
        while True:
            try:
                game = Othello.Game(_get_rows(), _get_columns(), _black_plays_first(), _white_in_top_left(),
                                    _win_with_most())
                break

            except Othello.IncorrectNumberOfRows:
                print("\nNumber of rows is incorrect, please try again.")

            except Othello.IncorrectNumberOfColumns:
                print("\nNumber of columns is incorrect, please try again.")

        black_ai = _yes_no_to_bool('Would you like the computer to control Black?  ')
        white_ai = _yes_no_to_bool('Would you like the computer to control White?  ')

        while game.win_result() == "":
            _score_board(game)
            _board(game)
            if black_ai and game.current_player() == Othello.BLACK:
                move = othello_ai.move(game)
                game.move(move[0],move[1])
                print("Black plays Row {}, Column {}.".format(move[0], move[1]))
                
            elif white_ai and game.current_player() == Othello.WHITE:
                move = othello_ai.move(game)
                game.move(move[0],move[1])
                print("White plays Row {}, Column {}.".format(move[0], move[1]))
                
            else:
                try:
                    game.move(_play_row(), _play_column())
                    
                except Othello.InvalidMove:
                    print('\nInvalid selection, please try again.')
                    
        _win_board(game)
        _board(game)
        
        if not _yes_no_to_bool('Would you like to play again?'):
            break


def _banner() -> None:
    """
    This function prints the game banner.
    :rtype : None
    """
    print("""\nThe Game of
     ______     ______   __  __     ______     __         __         ______
    /\  __ \   /\__  _\ /\ \_\ \   /\  ___\   /\ \       /\ \       /\  __ \\
    \ \ \/\ \  \/_/\ \/ \ \  __ \  \ \  __\   \ \ \____  \ \ \____  \ \ \/\ \\
     \ \_____\    \ \_\  \ \_\ \_\  \ \_____\  \ \_____\  \ \_____\  \ \_____\\
      \/_____/     \/_/   \/_/\/_/   \/_____/   \/_____/   \/_____/   \/_____/""")


def _board(game:Othello) -> None:
    """
    This function prints the game board to the console.
    :rtype : None
    :param game: Othello
    """
    rows = game.rows()
    columns = game.columns()
    for column in range(columns):
        if column < 1:
            print('{:>5}'.format(column + 1), end='')

        else:
            print('{:>3}'.format(column + 1), end='')

    print()

    for row in range(rows):
        print('{:>2}'.format(row + 1), end='')
        for column in range(columns):
            print('{:>3}'.format(game.cell(row + 1, column + 1)), end='')
        print()


def _score_board(game:Othello) -> None:
    """
    This function prints out the score board with the current player.
    :rtype : None
    :param game: Othello
    """
    blackscore = 'Black:  ' + str(game.black_score())
    whitescore = "White:  " + str(game.white_score())
    print()
    print(''.center(50, '-'))
    print('|' + blackscore.center(24, ' ') + whitescore.center(24, ' ') + '|')
    if game.current_player() == Othello.BLACK:
        print('|' + "Black's turn".center(48, ' ') + '|')
    else:
        print('|' + "White's turn".center(48, ' ') + '|')
    print(''.center(50, '-'))


def _win_board(game:Othello) -> None:
    """
    This function prints out the winner (or Tie) and the scores.
    :rtype : None
    :param game: Othello
    """
    blackscore = 'Black:  ' + str(game.black_score())
    whitescore = "White:  " + str(game.white_score())
    winner = game.win_result()
    print()
    print(''.center(50, '-'))
    print('|' + blackscore.center(24, ' ') + whitescore.center(24, ' ') + '|')
    if winner == Othello.BLACK:
        print('|' + "Black Won!".center(48, ' ') + '|')
    elif winner == Othello.WHITE:
        print('|' + "White Won!".center(48, ' ') + '|')
    elif winner == 'Tie':
        print('|' + "Tie!".center(48, ' ') + '|')
    print(''.center(50, '-'))


def _get_rows() -> int:
    """
    This function gets the desired rows for the othello game.
    :rtype : int
    """
    while True:
        try:
            return int(input("\nPlease enter the desired number of rows.\nNumber must be even and between 4 and 16:  "))
        except:
            print("Invalid input, please try again.")


def _get_columns() -> int:
    """
    This function gets the desired columns for the othello game.
    :rtype : int
    """
    while True:
        try:
            return int(
                input("\nPlease enter the desired number of columns.\nNumber must be even and between 4 and 16:  "))
        except:
            print("Invalid input, please try again.")


def _play_row() -> int:
    """
    This function ask the player for the row they would like to play.
    :rtype : int
    """
    while True:
        try:
            return int(input("Please enter the row you would like to play:  "))
        except:
            print('\nInvalid input, please try again.')


def _play_column() -> int:
    """
    This function ask the player for the column they would like to play.
    :rtype : int
    """
    while True:
        try:
            return int(input("Please enter the column you would like to play:  "))
        except:
            print('\nInvalid input, please try again.')


def _black_plays_first() -> bool:
    """
    This function determines who should play first.
    :rtype : bool
    """
    while True:
        black_first = input("\nShould [B]lack or [W]hite play first?\n(Default is Black):  ").strip().upper()
        if black_first == '' or black_first == Othello.BLACK:
            return True
        elif black_first == "W":
            return False
        else:
            print("Invalid input, please try again.")


def _white_in_top_left() -> bool:
    """
    This function determines how the board's initial layout should be.
    :rtype : bool
    """
    while True:
        white_top = input(
            "\nFor the initial board layout, Should [W]hite or [B]lack take the upper left corner?\n(Default is White):  ").strip().upper()
        if white_top == '' or white_top == Othello.WHITE:
            return True
        elif white_top == "B":
            return False
        else:
            print("Invalid input, please try again.")


def _win_with_most() -> bool:
    """
    This function determines which rule the game should use for the winning condition.
    :rtype : bool
    """
    while True:
        win_most = input("\nWin with [M]ost points or [L]east?\n(Default is Most):  ").strip().upper()
        if win_most == '' or win_most == 'M':
            return True
        elif win_most == "L":
            return False
        else:
            print("Invalid input, please try again.")

def _yes_no_to_bool(question:str) -> bool:
    """
    This function ask the user a Yes or No question and returns the True or False.
    :rtype : bool
    """
    while True:
        try:
            answer = input("\n" + question + ' (Y/N):  ').strip().upper()
            if answer == 'Y':
                return True
            elif answer == 'N':
                return False
            else:
                print('Invalid choice, please try again.')
        except:
            print('Invalid input, please try again.')


if __name__ == '__main__':
    play_game()
