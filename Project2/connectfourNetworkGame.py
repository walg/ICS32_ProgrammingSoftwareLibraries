#Ray Chou 67255516 and Ford Tang 46564602
# ICS 32 Winter 2014
# Project #2: Send Me On My Way

#connectfourNetworkGame

import connectfour
import connectfour_protocol
import connectfour_game_functions

def menu() -> None:
    'This function is the main menu of the connect four console game'
    game = connectfour.new_game_state()
    winner = connectfour.NONE
    while True:
        while True:
            username = input('Please enter a username (no spaces!):  ').strip()
            if username.find(' ') < 0:
                break
            else:
                print('Invalid input.  Please try a username without spaces.\n')

        host = input('Please enter the host name:  ')
        

        while True:
            try:
                port = int(input('Please enter the port:  '))
                break
            except:
                print('Invalid input, please enter a number.\n')

        print('Trying to connect...')
        try:
            connection = connectfour_protocol.connect(host, port)
            print('Connected Successfully!')        
            if connectfour_protocol.login(connection, username) == True:
                print('Login Successful!')
                if connectfour_protocol.startGame(connection) == True:
                    print('Game Started!')
                    break
                else:
                    print('Could not Start Game!  Try again.\n')
                    connectfour_protocol.close(connection)
            else:
                print('Could not log in!  Try again.\n')
                connectfour_protocol.close(connection)
        except:
            print('Connection Failed!  Try again.\n')

    try:
        while winner == connectfour.NONE:
            while game.turn == connectfour.RED:
                connectfour_game_functions.printBoard(game)
                game = connectfour_game_functions.directions_network(game, username, connection)
                winner = connectfour.winning_player(game)
            if winner == connectfour.RED:
                    break
            connectfour_game_functions.printBoard(game)
            game = connectfour_game_functions.move_network_ai(game, connection)
            winner = connectfour.winning_player(game)
        connectfour_game_functions.printBoard(game)
        if winner == connectfour.RED:
            print('The winner is ' + username + '!')
        else:
            print('The winner is AI!')
    finally:
        connectfour_protocol.close(connection)

if __name__ == '__main__':
    menu()
