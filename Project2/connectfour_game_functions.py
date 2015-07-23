#Ray Chou 67255516 and Ford Tang 46564602
# ICS 32 Winter 2014
# Project #2: Send Me On My Way

#connectfour_game_functions

import connectfour
import connectfour_protocol

def printBoard(gameState: connectfour.ConnectFourGameState) -> None:
    'This function prints out the game board.'
    print()
    for column in range(connectfour.BOARD_COLUMNS):
        print(str(column + 1), end = '  ')
    print()
    for row in range(connectfour.BOARD_ROWS):
        for column in range(connectfour.BOARD_COLUMNS):
            if gameState.board[column][row] == connectfour.NONE:
                print('.  ', end = '')
            else:
                print(gameState.board[column][row], end = '  ')
        print()
    print()

def directions_console(gameState: connectfour.ConnectFourGameState) -> connectfour.ConnectFourGameState:
    'This function prints out the directions to the current player and returns the updated game.'
    choice = ''
    column = 0
    print('Current player is:  ', end = '')
    if gameState.turn == connectfour.RED:
        print('Red')
    else:
        print('Yellow')
    while True:
        choice = input('To Drop type D, To Pop type P:  ').upper()
        if choice == 'D' or choice == 'P':
            gameState = _move(gameState, choice)
            break
        else:
            print('Incorrect choice, please try again.')
    return gameState

def _move(gameState: connectfour.ConnectFourGameState, move: str) -> connectfour.ConnectFourGameState:
    'This function determines what move the current player would like to do'
    while True:
        try:
            column = int(input('Which column (1 - ' + str(connectfour.BOARD_COLUMNS) + '):  '))
            if  column > 0 and column <= connectfour.BOARD_COLUMNS:
                if move == 'D':
                    gameState = connectfour.drop_piece(gameState,column - 1)
                    break
                else:
                    gameState = connectfour.pop_piece(gameState,column - 1)
                    break
            else:
                print('Invalid column, please try again.\n')
        except:
            print('Invalid input, please try again.')
            break
    return gameState

def directions_network(gameState: connectfour.ConnectFourGameState, username: str, connection: connectfour_protocol.connectFourConnection) -> connectfour.ConnectFourGameState:
    'This function prints out the directions to the current player and returns the updated game.'
    choice = ''
    column = 0
    print('Current player is:  ' + username + ' (Red)')   
    while True:
        choice = input('To Drop type D, To Pop type P:  ').upper()
        if choice == 'D' or choice == 'P':
            gameState = _move_network(gameState, choice, connection)
            break
        else:
            print('Incorrect choice, please try again.')
    return gameState

def _move_network(gameState: connectfour.ConnectFourGameState, move: str, connection: connectfour_protocol.connectFourConnection) -> connectfour.ConnectFourGameState:
    'This function determines what move the current player would like to do'
    while True:
        try:
            column = int(input('Which column (1 - ' + str(connectfour.BOARD_COLUMNS) + '):  '))
            if  column > 0 and column <= connectfour.BOARD_COLUMNS:
                if move == 'D':
                    gameState = connectfour.drop_piece(gameState,column - 1)
                    connectfour_protocol.sendMove(connection, 'DROP' , column)
                    break
                elif move == 'P':
                    gameState = connectfour.pop_piece(gameState,column - 1)
                    connectfour_protocol.sendMove(connection, 'POP', column)
                    break
            else:
                print('Invalid column, please try again.\n')
        except:
            print('Invalid input, please try again.')
            break
    return gameState

def move_network_ai(gameState: connectfour.ConnectFourGameState, connection: connectfour_protocol.connectFourConnection) -> connectfour.ConnectFourGameState:
    'This function receives the status of the network AI and updates the gameState accordingly.'
    status = connectfour_protocol.serverStatus(connection)
    status = status.split( )
    print('Current player is:  AI (Yellow)')
    if status[0] == 'DROP':
        print('AI drops in column ' + status[1])
        gameState = connectfour.drop_piece(gameState,int(status[1]) - 1)
    elif status[0] == 'POP':
        print('AI pops column ' + status[1])
        gameState = connectfour.pop_piece(gameState,int(status[1]) - 1)
    else:
        print('Move was invalid. Try again.')
    return gameState
