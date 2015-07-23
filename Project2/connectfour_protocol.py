#Ray Chou 67255516 and Ford Tang 46564602
# ICS 32 Winter 2014
# Project #2.2: Send Me On My Way (Network version)

#connectfour_protocol

import socket
import collections

connectFourConnection = collections.namedtuple('connectFourConnection', ['socket', 'socket_input', 'socket_output'])

#connectFourMessage = collections.namedtuple('connectFourMessage', ['command'])

class ConnectFourServerNotReadyError(Exception):
    '''Raised when server is not ready'''
    pass

def connect(host: str, port: int) -> connectFourConnection:
    'Connects to a connect four server, returns a connectFourConnection'
    connectFour_socket = socket.socket()

    connectFour_socket.connect((host, port))

    connectFour_socket_input = connectFour_socket.makefile('r')
    connectFour_socket_output = connectFour_socket.makefile('w')

    return connectFourConnection(socket = connectFour_socket, socket_input = connectFour_socket_input, socket_output = connectFour_socket_output)

def login(connection: connectFourConnection, username: str) -> bool:
    'Logs a user into the connect four server and returns true if successful and false if not.'
    _sendCommand(connection, 'I32CFSP_HELLO ' + username)
    return _checkReceive(connection, 'WELCOME ' + username)

def sendMove(connection: connectFourConnection, command: str, column: int) -> None:
    'Sends a command to the connect four server and returns the server status.'
    _sendCommand(connection, command + ' ' + str(column))
    return None

def serverStatus(connection: connectFourConnection) -> str:
    'Returns the server status after a game move.'
    check = _receive_line(connection)
    status = ''
    if check == 'OKAY':
        status = _receive_line(connection)
        check = _receive_line(connection)        
        if check == 'WINNER_YELLOW' or check == 'WINNER_RED':
            status = status + '\n' + check
        elif check != 'READY':
            raise ConnectFourServerNotReadyError()
    elif check == 'INVALID':
        status = check
        check = _receive_line(connection)
        if check != 'READY':
            raise ConnectFourServerNotReadyError()
    else:
        status = check
    return status

def startGame(connection: connectFourConnection) -> bool:
    'Starts a game on the server and returns true if successful and false if not.'
    _sendCommand(connection, 'AI_GAME')
    return _checkReceive(connection, 'READY')

def close(connection: connectFourConnection) -> None:
    'Closes the connection to the connectFourServer.'
    connection.socket_input.close()
    connection.socket_output.close()
    connection.socket.close()

def _receive_line(connection: connectFourConnection) -> [str]:
    'Reads a line of text from the server and returns it without the newline on the end of it.'
    return connection.socket_input.readline()[:-1]    

def _sendCommand(connection: connectFourConnection, command: str) -> None:
    'Sends a command to the server, including the appropriate newline sequences.'
    connection.socket_output.write(command + '\r\n')
    connection.socket_output.flush()

def _checkReceive(connection: connectFourConnection, expectedLine: str) -> bool:
    "Reads a line from the server and checks it against the expected line.  Returns true if they match and false if they don't."
    return _receive_line(connection) == expectedLine
