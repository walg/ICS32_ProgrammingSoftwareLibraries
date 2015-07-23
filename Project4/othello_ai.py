# Ford Tang / 46564602

# Project #4: The Width of a Circle (Part 1)

# othello_ai.py

# This module can be used to run an othello game against an AI.

import Othello
import othello_game_logic
import random
import copy

EMPTY = othello_game_logic.EMPTY


def move(game:Othello) -> tuple:
    """
    This function determines what cell the AI would like to play and returns it as a tuple.
    :rtype : tuple
    :param game: Othello
    """
    #print(available_moves)
    return _determine_move(game,_find_moves(game))


def _find_moves(game:Othello) -> list:
    """
    This function finds all available moves on the board for the AI and returns the result as a list of tuples.
    :rtype : list
    :param game: Othello
    """
    result = []
    for row in range(game.rows()):
        for column in range(game.columns()):
            if game.cell(row + 1, column + 1) == EMPTY:
                if othello_game_logic._check_move(row + 1, column + 1, game._game_state):
                    result.append((row + 1, column + 1))
    return result

def _determine_move(game:Othello, moves:list) -> tuple:
    """
    This function will simulate the opponent's move and return the move with the best result.
    :rtype : tuple
    :param game: Othello
    :param moves: list
    """
    computer_ai = game.current_player()
    result = moves[0]
    win_most = game._game_state.win_with_most
    if win_most:
        best_score = 0
    else:
        best_score = 256
    for move in moves:
        score = 0
        test = copy.deepcopy(game)
        test.move(move[0],move[1])
        if computer_ai == Othello.BLACK:
            score += test.black_score()
        else:
            score += test.white_score()
        if test.current_player() != computer_ai:
            opponent_moves = _find_moves(test)
            for opponent_move in opponent_moves:
                test2 = copy.deepcopy(test)
                test2.move(opponent_move[0], opponent_move[1])
                if win_most:
                    if computer_ai == Othello.BLACK:
                        if score + test.black_score() > best_score:
                            best_score = score + test.black_score()
                            result = move
                        elif score + test.black_score() == best_score:
                            choice = [result, move]
                            result = choice[random.randrange(len(choice))]
                    else:
                        if score + test.white_score() > best_score:
                            best_score = score + test.white_score()
                            result = move
                        elif score + test.white_score() == best_score:
                            choice = [result, move]
                            result = choice[random.randrange(len(choice))]
                else:
                    if computer_ai == Othello.BLACK:
                        if score + test.black_score() < best_score:
                            best_score = score + test.black_score()
                            result = move
                        elif score + test.black_score() == best_score:
                            choice = [result, move]
                            result = choice[random.randrange(len(choice))]
                    else:
                        if score + test.white_score() < best_score:
                            best_score = score + test.white_score()
                            result = move
                        elif score + test.white_score() == best_score:
                            choice = [result, move]
                            result = choice[random.randrange(len(choice))]
    return result

