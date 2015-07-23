# Ford Tang / 46564602

# Project #5: The Width of a Circle (Part 2)

# othello_game_logic.py

#This module will determine the game logic for othello.

from collections import namedtuple


class IncorrectNumberOfRows(Exception):
    """
    Raised when there is an incorrect number of rows when creating a game board
    """
    pass


class IncorrectNumberOfColumns(Exception):
    """
    Raised when there is an incorrect number of columns when creating a game board
    """
    pass


class InvalidMove(Exception):
    """
    Raised when an invalid move is made.
    """
    pass


BLACK = 'B'
WHITE = 'W'
EMPTY = '.'


def create_board(rows:int, columns:int, white_in_top_left:bool) -> [list]:
    """
    This function will create a game board with the given rows and columns as a list in a list.
    :rtype : [list]
    :param rows: int
    :param columns: int
    :param white_in_top_left: othello namedtuple
    """
    if rows % 2 == 1:
        raise IncorrectNumberOfRows

    if rows < 4 or rows > 16:
        raise IncorrectNumberOfRows

    if columns % 2 == 1:
        raise IncorrectNumberOfColumns

    if columns < 4 or columns > 16:
        raise IncorrectNumberOfColumns

    game_board = []
    for row in range(rows):
        game_board.append([])
        for column in range(columns):
            game_board[-1].append(EMPTY)

    top_x = (rows // 2) - 1
    top_y = (columns // 2) - 1

    if white_in_top_left == True:
        game_board[top_x][top_y] = WHITE
        game_board[top_x + 1][top_y + 1] = WHITE
        game_board[top_x + 1][top_y] = BLACK
        game_board[top_x][top_y + 1] = BLACK

    else:
        game_board[top_x][top_y] = BLACK
        game_board[top_x + 1][top_y + 1] = BLACK
        game_board[top_x + 1][top_y] = WHITE
        game_board[top_x][top_y + 1] = WHITE

    return game_board


def _check_move(row:int, column:int, game_state: namedtuple) -> bool:
    """
    This function will check if a move is valid and returns True if it is, and False if not.
    :rtype : bool
    :param row: int
    :param column: int
    :param game_state: othello namedtuple
    """
    #print('_check_move {},{} = {}'.format(row, column, game_state.game_board[row - 1][column - 1]))
    if game_state.game_board[row - 1][column - 1] == BLACK or game_state.game_board[row - 1][column - 1] == WHITE:
        return False

    if row > 2:
        if _find_north(row, column, game_state) != 0:
            return True

        if column > 2:
            if _find_northwest(row, column, game_state) != 0:
                return True

        if column < len(game_state.game_board[0]) - 1:
            if _find_northeast(row, column, game_state) != 0:
                return True

    if row < len(game_state.game_board) - 1:
        if _find_south(row, column, game_state) != 0:
            return True

        if column > 2:
            if _find_southwest(row, column, game_state) != 0:
                return True

        if column < len(game_state.game_board[0]) - 1:
            if _find_southeast(row, column, game_state) != 0:
                return True

    if column > 2:
        if _find_west(row, column, game_state) != 0:
            return True

    if column < len(game_state.game_board[0]) - 1:
        if _find_east(row, column, game_state) != 0:
            return True

    else:
        return False


def _find_north(row:int, column:int, game_state: namedtuple) -> int:
    """
    This function checks to the north and finds the number of disk that can be captured by the current player.
    :rtype : int
    :param row: int
    :param column: int
    :param game_state: othello namedtuple
    """
    #print('_find_north {},{} = {}'.format(row, column, game_state.game_board[row - 1][column - 1]))
    counter = 0
    row -= 1
    column -= 1
    while row > 0:
        if game_state.game_board[row - 1][column] == game_state.current_player:
            return counter

        elif game_state.game_board[row - 1][column] != game_state.current_player and game_state.game_board[row - 1][
            column] != EMPTY:
            counter += 1

        else:
            return 0

        row -= 1

    return 0


def _find_south(row:int, column:int, game_state: namedtuple) -> int:
    """
    This function checks to the south and finds the number of disk that can be captured by the current player.
    :rtype : int
    :param row: int
    :param column: int
    :param game_state: othello namedtuple
    """
    #print('_find_south {},{} = {}'.format(row, column, game_state.game_board[row - 1][column - 1]))
    counter = 0
    row -= 1
    column -= 1
    while row < len(game_state.game_board) - 1:
        if game_state.game_board[row + 1][column] == game_state.current_player:
            return counter

        elif game_state.game_board[row + 1][column] != game_state.current_player and game_state.game_board[row + 1][
            column] != EMPTY:
            counter += 1

        else:
            return 0

        row += 1

    return 0


def _find_west(row:int, column:int, game_state: namedtuple) -> int:
    """
    This function checks to the west and finds the number of disk that can be captured by the current player.
    :rtype : int
    :param row: int
    :param column: int
    :param game_state: othello namedtuple
    """
    #print('_find_west {},{} = {}'.format(row, column, game_state.game_board[row - 1][column - 1]))
    counter = 0
    row -= 1
    column -= 1
    while column > 0:
        if game_state.game_board[row][column - 1] == game_state.current_player:
            return counter

        elif game_state.game_board[row][column - 1] != game_state.current_player and game_state.game_board[row][
                    column - 1] != EMPTY:
            counter += 1

        else:
            return 0

        column -= 1

    return 0


def _find_east(row:int, column:int, game_state: namedtuple) -> int:
    """
    This function checks to the east and finds the number of disk that can be captured by the current player.
    :rtype : int
    :param row: int
    :param column: int
    :param game_state: othello namedtuple
    """
    #print('_find_east {},{} = {}'.format(row, column, game_state.game_board[row - 1][column - 1]))
    counter = 0
    row -= 1
    column -= 1
    while column < len(game_state.game_board[0]) - 1:
        if game_state.game_board[row][column + 1] == game_state.current_player:
            return counter

        elif game_state.game_board[row][column + 1] != game_state.current_player and game_state.game_board[row][
                    column + 1] != EMPTY:
            counter += 1

        else:
            return 0

        column += 1

    return 0


def _find_northwest(row:int, column:int, game_state: namedtuple) -> int:
    """
    This function checks to the northwest and finds the number of disk that can be captured by the current player.
    :rtype : int
    :param row: int
    :param column: int
    :param game_state: othello namedtuple
    """
    #print('_find_northwest {},{} = {}'.format(row, column, game_state.game_board[row - 1][column - 1]))
    counter = 0
    row -= 1
    column -= 1
    while row > 0 and column > 0:
        if game_state.game_board[row - 1][column - 1] == game_state.current_player:
            return counter

        elif game_state.game_board[row - 1][column - 1] != game_state.current_player and game_state.game_board[row - 1][
                    column - 1] != EMPTY:
            counter += 1

        else:
            return 0

        row -= 1
        column -= 1

    return 0


def _find_northeast(row:int, column:int, game_state: namedtuple) -> int:
    """
    This function checks to the northeast and finds the number of disk that can be captured by the current player.
    :rtype : int
    :param row: int
    :param column: int
    :param game_state: othello namedtuple
    """
    #print('_find_northeast {},{} = {}'.format(row, column, game_state.game_board[row - 1][column - 1]))
    counter = 0
    row -= 1
    column -= 1
    while row > 0 and column < len(game_state.game_board[0]) - 1:
        if game_state.game_board[row - 1][column + 1] == game_state.current_player:
            return counter

        elif game_state.game_board[row - 1][column + 1] != game_state.current_player and game_state.game_board[row - 1][
                    column + 1] != EMPTY:
            counter += 1

        else:
            return 0

        row -= 1
        column += 1

    return 0


def _find_southwest(row:int, column:int, game_state: namedtuple) -> int:
    """
    This function checks to the southwest and finds the number of disk that can be captured by the current player.
    :rtype : int
    :param row: int
    :param column: int
    :param game_state: othello namedtuple
    """
    #print('_find_southwest {},{} = {}'.format(row, column, game_state.game_board[row - 1][column - 1]))
    counter = 0
    row -= 1
    column -= 1
    while row < len(game_state.game_board) - 1 and column > 0:
        if game_state.game_board[row + 1][column - 1] == game_state.current_player:
            return counter

        elif game_state.game_board[row + 1][column - 1] != game_state.current_player and game_state.game_board[row + 1][
                    column - 1] != EMPTY:
            counter += 1

        else:
            return 0

        row += 1
        column -= 1

    return 0


def _find_southeast(row:int, column:int, game_state: namedtuple) -> int:
    """
    This function checks to the south and finds the number of disk that can be captured by the current player.
    :rtype : int
    :param row: int
    :param column: int
    :param game_state: othello namedtuple
    """
    #print('_find_southeast {},{} = {}'.format(row, column, game_state.game_board[row - 1][column - 1]))
    counter = 0
    row -= 1
    column -= 1
    while row < len(game_state.game_board) - 1 and column < len(game_state.game_board[0]) - 1:
        if game_state.game_board[row + 1][column + 1] == game_state.current_player:
            return counter

        elif game_state.game_board[row + 1][column + 1] != game_state.current_player and game_state.game_board[row + 1][
                    column + 1] != EMPTY:
            counter += 1

        else:
            return 0

        row += 1
        column += 1

    return 0


def _check_player(game_state: namedtuple) -> bool:
    """
    This function will check if there are any available moves for the current player and return True if there are any.
    :rtype : bool
    :param game_state: othello namedtuple
    """
    #print('_check_player')
    for row in range(len(game_state.game_board)):
        for column in range(len(game_state.game_board[row])):
            if game_state.game_board[row][column] == EMPTY:
                if _check_move(row + 1, column + 1, game_state):
                    return True
    return False


def move(row:int, column:int, game_state: namedtuple) -> namedtuple:
    """
    This function will perform the given move the for the current player
    :rtype : othello namedtuple
    :param row: int
    :param column: int
    :param game_state: othello namedtuple
    """
    #print('move {},{} = {}'.format(row, column, game_state.game_board[row - 1][column - 1]))
    if row > len(game_state.game_board) or row < 1:
        raise InvalidMove

    if column > len(game_state.game_board[0]) or column < 1:
        raise InvalidMove

    if not _check_move(row, column, game_state):
        raise InvalidMove

    for number in range(_find_north(row, column, game_state)):
        game_state.game_board[(row - 1) - (number + 1)][(column - 1)] = game_state.current_player

    for number in range(_find_south(row, column, game_state)):
        game_state.game_board[(row - 1) + (number + 1)][(column - 1)] = game_state.current_player

    for number in range(_find_west(row, column, game_state)):
        game_state.game_board[(row - 1)][(column - 1) - (number + 1)] = game_state.current_player

    for number in range(_find_east(row, column, game_state)):
        game_state.game_board[(row - 1)][(column - 1) + (number + 1)] = game_state.current_player

    for number in range(_find_northwest(row, column, game_state)):
        game_state.game_board[(row - 1) - (number + 1)][(column - 1) - (number + 1)] = game_state.current_player

    for number in range(_find_northeast(row, column, game_state)):
        game_state.game_board[(row - 1) - (number + 1)][(column - 1) + (number + 1)] = game_state.current_player

    for number in range(_find_southwest(row, column, game_state)):
        game_state.game_board[(row - 1) + (number + 1)][(column - 1) - (number + 1)] = game_state.current_player

    for number in range(_find_southeast(row, column, game_state)):
        game_state.game_board[(row - 1) + (number + 1)][(column - 1) + (number + 1)] = game_state.current_player

    game_state.game_board[row - 1][column - 1] = game_state.current_player

    game_state = count_disk(game_state)

    game_state = _change_player(game_state)

    if not _check_player(game_state):
        game_state = _change_player(game_state)

        if _check_win(game_state):
            game_state = game_state._replace(win_result=_find_winner(game_state))

            return game_state

    return game_state


def _check_win(game_state: namedtuple) -> bool:
    """
    This function checks to see if a win scenario has occurred and returns True if there are no more moves.
    :rtype : bool
    :param game_state: othello namedtuple
    """
    if _check_player(game_state) or _check_player(_change_player(game_state)):
        return False
    return True


def _find_winner(game_state: namedtuple) -> str:
    """
    This function determines the winner of the game (or tie), and returns the result as a string.
    :rtype : str
    :param game_state: othello namedtuple
    """
    if game_state.win_with_most == True:
        if game_state.black_score > game_state.white_score:
            return BLACK

        elif game_state.black_score < game_state.white_score:
            return WHITE

        else:
            return 'Tie'

    else:
        if game_state.black_score > game_state.white_score:
            return WHITE

        elif game_state.black_score < game_state.white_score:
            return BLACK

        else:
            return 'Tie'


def _change_player(game_state: namedtuple) -> namedtuple:
    """
    This function changes the current player in the game state and returns it.
    :rtype : othello namedtuple
    :param game_state: othello namedtuple
    """
    #print('_change_player)')
    if game_state.current_player == BLACK:
        game_state = game_state._replace(current_player=WHITE)

    else:
        game_state = game_state._replace(current_player=BLACK)

    return game_state


def count_disk(game_state: namedtuple) -> namedtuple:
    """
    This function counts the disks on the game board and updates the game state and returns it.
    :rtype : othello namedtuple
    :param game_state: othello namedtuple
    """
    #print('_count_disk')
    black_count = 0
    white_count = 0

    for row in game_state.game_board:
        for cell in row:
            if cell == BLACK:
                black_count += 1

            if cell == WHITE:
                white_count += 1

    game_state = game_state._replace(black_score=black_count)
    game_state = game_state._replace(white_score=white_count)

    return game_state
