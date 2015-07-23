# Ford Tang / 46564602

# Project #5: The Width of a Circle (Part 2)

# Othello.py

# The othello class creates an object that holds the game state of an othello game.

# othello objects can:
#   * Return the number of rows of a board
#   * Return the number of columns of a board
#   * Return the current player
#   * Return what is in a current cell on the grid
#   * Return a state whether the game is over
#   * Perform a move

# othello objects need the following data to initialize:
#   * The number of Rows
#   * The number of Columns
#   * Who starts first
#   * Order of the initial 4 disc
#   * Rules for winning

from collections import namedtuple
import othello_game_logic


class GameOver(Exception):
    """
    Raised when a move is made but the game is over
    """
    pass


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


BLACK = othello_game_logic.BLACK
WHITE = othello_game_logic.WHITE


class Game:
    def __init__(self, rows:int, columns:int, black_plays_first:bool, white_in_top_left:bool,
                 win_with_most:bool) -> None:
        """
        :rtype : None
        :param rows: int
        :param columns: int
        :param black_plays_first: bool
        :param white_in_top_left: bool
        :param win_with_most: bool
        """
        game = namedtuple('game', 'game_board current_player black_score white_score win_with_most win_result')
        try:
            if black_plays_first == True:
                self._game_state = game(othello_game_logic.create_board(rows, columns, white_in_top_left), BLACK,
                                        0, 0, win_with_most, '')
            else:
                self._game_state = game(othello_game_logic.create_board(rows, columns, white_in_top_left), WHITE,
                                        0, 0, win_with_most, '')
        except othello_game_logic.IncorrectNumberOfRows:
            raise IncorrectNumberOfRows
        except othello_game_logic.IncorrectNumberOfColumns:
            raise IncorrectNumberOfColumns
        self._game_state = othello_game_logic.count_disk(self._game_state)

    def current_player(self) -> str:
        """This method will return the current player
        :rtype : str
        """
        return self._game_state.current_player

    def black_score(self) -> int:
        """
        This method will return the score for the black player
        :rtype : int
        """
        return self._game_state.black_score

    def white_score(self) -> int:
        """
        This method will return the score for the white player
        :rtype : int
        """
        return self._game_state.white_score

    def win_result(self) -> str:
        """
        This method will return the winner result
        :rtype : str
        """
        return self._game_state.win_result

    def cell(self, row:int, column:int) -> str:
        """
        This method will return the item in the given row and column
        :rtype : str
        """
        return self._game_state.game_board[row - 1][column - 1]

    def rows(self) -> int:
        """
        This method will return the number of rows
        :rtype : int
        """
        return len(self._game_state.game_board)

    def columns(self) -> int:
        """
        This method will return the number of columns
        :rtype : int
        """
        return len(self._game_state.game_board[0])

    def move(self, row:int, column:int) -> None:
        """
        This method takes a move and updates the game states accordingly
        :rtype : None
        """
        if self._game_state.win_result != '':
            raise GameOver

        try:
            self._game_state = othello_game_logic.move(row, column, self._game_state)
        except othello_game_logic.InvalidMove:
            raise InvalidMove
