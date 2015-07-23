__author__ = 'Ford Tang / 46564602'

# Project #5: The Width of a Circle (Part 2)

# Project5.py

import Othello
import othello_ai
import tkinter

_DEFAULT_FONT = ('Segoe UI', 20)
_OPTION_FONT = ('Segoe UI', 10)
_BANNER_FONT = ('Segoe UI', 40)
_BOARD_BACKGROUND = '#006000'
_DEFAULT_BACKGROUND = '#808080'

class Othello_GUI:
    def __init__(self) -> None:
        self._game = None
        self._rows = 8
        self._columns = 8
        self._black_plays_first = True
        self._white_in_top_left = True
        self._win_with_most = True
        self._ai_black = False
        self._ai_white = False
        
        self._root_window = tkinter.Tk()

        self._intro()        

    def start(self):
        self._root_window.mainloop()

    def _intro(self):
        self._canvas = tkinter.Canvas(master = self._root_window, width = 550, height = 800, background = _DEFAULT_BACKGROUND)
        self._canvas.grid(row = 0, column = 0, rowspan = 3, sticky = tkinter.N + tkinter.S + tkinter.W + tkinter.E)

        self._start_button = tkinter.Button(master = self._root_window, text = 'Start Game', font = _DEFAULT_FONT, command = self._start_game)
        self._start_button.grid(row = 1, column = 0, padx = 10, pady = 10, sticky = tkinter.S)

        self._option_button = tkinter.Button(master = self._root_window, text = 'Options', font = _DEFAULT_FONT, command = self._options)
        self._option_button.grid(row = 2, column = 0, padx = 10, pady = 10, sticky = tkinter.N)

        self._banner_label = tkinter.Label(master = self._root_window, text = 'The Game of Othello', font = _BANNER_FONT, foreground = 'white', background = _DEFAULT_BACKGROUND)
        self._banner_label.grid(row = 0, padx = 10, pady = 10)

        self._root_window.rowconfigure(0, weight = 1)
        self._root_window.rowconfigure(1, weight = 1)
        self._root_window.rowconfigure(2, weight = 1)
        self._root_window.columnconfigure(0, weight = 1)

    def _options(self) -> None:
        """
        This method draws the option screen.
        """
        self._clear_intro()
        self._canvas.grid(rowspan = 9, columnspan = 2)

        self._option_label = tkinter.Label(master = self._root_window, text = 'Options', font = _BANNER_FONT, foreground = 'white', background = _DEFAULT_BACKGROUND)
        self._option_label.grid(row = 0, columnspan = 2, padx = 10, pady = 10)

        self._number_of_rows_label = tkinter.Label(master = self._root_window, text = 'Number of Rows:  ', font = _OPTION_FONT, foreground = 'white', background = _DEFAULT_BACKGROUND)
        self._number_of_rows_label.grid(row = 1, column = 0, padx = 10, pady = 10, sticky = tkinter.E)

        self._number_of_columns_label = tkinter.Label(master = self._root_window, text = 'Number of Columns:  ', font = _OPTION_FONT, foreground = 'white', background = _DEFAULT_BACKGROUND)
        self._number_of_columns_label.grid(row = 2, column = 0, padx = 10, pady = 10, sticky = tkinter.E)

        self._rows_int = tkinter.IntVar()
        self._rows_int.set(self._rows)

        self._columns_int = tkinter.IntVar()
        self._columns_int.set(self._columns)

        self._rows_menu = tkinter.OptionMenu(self._root_window, self._rows_int, 4, 6, 8, 10, 12, 14, 16)
        self._rows_menu.config(width = 2)
        self._rows_menu.grid(row = 1, column = 1, padx = 10, pady = 10, sticky = tkinter.W)

        self._columns_menu = tkinter.OptionMenu(self._root_window, self._columns_int, 4, 6, 8, 10, 12, 14, 16)
        self._columns_menu.config(width = 2)
        self._columns_menu.grid(row = 2, column = 1, padx = 10, pady = 10, sticky = tkinter.W)

        self._black_plays_first_button = tkinter.Checkbutton(master = self._root_window, background = _DEFAULT_BACKGROUND, borderwidth = 5,font = _OPTION_FONT, indicatoron = 0, offvalue = False, onvalue = True, padx = 10, pady = 10, text = 'Black plays first?', command = self._toggle_black_plays_first)
        if self._black_plays_first:
            self._black_plays_first_button.select()
        self._black_plays_first_button.grid(row = 3, column = 0, columnspan = 2, padx = 10, pady = 10)

        self._white_in_top_left_button = tkinter.Checkbutton(master = self._root_window, background = _DEFAULT_BACKGROUND, borderwidth = 5,font = _OPTION_FONT, indicatoron = 0, offvalue = False, onvalue = True, padx = 10, pady = 10, text = 'White in Top-Left?', command = self._toggle_white_in_top_left)
        if self._white_in_top_left:
            self._white_in_top_left_button.select()
        self._white_in_top_left_button.grid(row = 4, column = 0, columnspan = 2, padx = 10, pady = 10)

        self._win_with_most_button = tkinter.Checkbutton(master = self._root_window, background = _DEFAULT_BACKGROUND, borderwidth = 5,font = _OPTION_FONT, indicatoron = 0, offvalue = False, onvalue = True, padx = 10, pady = 10, text = 'Win with most?', command = self._toggle_win_with_most)
        if self._win_with_most:
            self._win_with_most_button.select()
        self._win_with_most_button.grid(row = 5, column = 0, columnspan = 2,  padx = 10, pady = 10)

        self._ai_black_button = tkinter.Checkbutton(master = self._root_window, background = _DEFAULT_BACKGROUND, borderwidth = 5,font = _OPTION_FONT, indicatoron = 0, offvalue = False, onvalue = True, padx = 10, pady = 10, text = 'Computer controls Black?', command = self._toggle_ai_black)
        if self._ai_black:
            self._ai_black_button.select()
        self._ai_black_button.grid(row = 6, column = 0, columnspan = 2,  padx = 10, pady = 10)

        self._ai_white_button = tkinter.Checkbutton(master = self._root_window, background = _DEFAULT_BACKGROUND, borderwidth = 5,font = _OPTION_FONT, indicatoron = 0, offvalue = False, onvalue = True, padx = 10, pady = 10, text = 'Computer controls White?', command = self._toggle_ai_white)
        if self._ai_white:
            self._ai_white_button.select()
        self._ai_white_button.grid(row = 7, column = 0, columnspan = 2,  padx = 10, pady = 10)

        self._option_back_button = tkinter.Button(master = self._root_window, text = 'Back', font = _DEFAULT_FONT, command = self._back)
        self._option_back_button.grid(row = 8, column = 0, columnspan = 2,  padx = 10, pady = 10)

        self._root_window.rowconfigure(0, weight = 1)
        self._root_window.rowconfigure(1, weight = 1)
        self._root_window.rowconfigure(2, weight = 1)
        self._root_window.rowconfigure(3, weight = 1)
        self._root_window.rowconfigure(4, weight = 1)
        self._root_window.rowconfigure(5, weight = 1)
        self._root_window.rowconfigure(6, weight = 1)
        self._root_window.rowconfigure(7, weight = 1)
        self._root_window.rowconfigure(8, weight = 1)
        self._root_window.columnconfigure(0, weight = 1)
        self._root_window.columnconfigure(1, weight = 1)


    def _toggle_black_plays_first(self) -> None:
        """
        This method toggles self._black_plays_first from True to False or vise versa.
        """
        if self._black_plays_first == True:
            self._black_plays_first = False
        else:
            self._black_plays_first = True

    def _toggle_white_in_top_left(self) -> None:
        """
        This method toggles self._white_in_top_left from True to False or vise versa.
        """
        if self._white_in_top_left == True:
            self._white_in_top_left = False
        else:
            self._white_in_top_left = True

    def _toggle_win_with_most(self) -> None:
        """
        This method toggles self._win_with_most from True to False or vise versa.
        """
        if self._win_with_most == True:
            self._win_with_most = False
        else:
            self._win_with_most = True

    def _toggle_ai_black(self) -> None:
        """
        This method toggles self._ai_black from True to False or vise versa.
        """
        if self._ai_black == True:
            self._ai_black = False
        else:
            self._ai_black = True

    def _toggle_ai_white(self) -> None:
        """
        This method toggles self._ai_black from True to False or vise versa.
        """
        if self._ai_white == True:
            self._ai_white = False
        else:
            self._ai_white = True

    def _back(self) -> None:
        self._rows = self._rows_int.get()
        self._columns = self._columns_int.get()

        self._option_label.grid_remove()
        self._number_of_rows_label.grid_remove()
        self._number_of_columns_label.grid_remove()
        self._rows_menu.grid_remove()
        self._columns_menu.grid_remove()
        self._black_plays_first_button.grid_remove()
        self._white_in_top_left_button.grid_remove()
        self._win_with_most_button.grid_remove()
        self._ai_black_button.grid_remove()
        self._ai_white_button.grid_remove()
        self._option_back_button.grid_remove()

        self._canvas.grid(rowspan = 3, columnspan = 1)

        self._root_window.option_clear()
        self._banner_label.grid()
        self._start_button.grid()
        self._option_button.grid()

        self._root_window.rowconfigure(0, weight = 1)
        self._root_window.rowconfigure(1, weight = 1)
        self._root_window.rowconfigure(2, weight = 1)
        self._root_window.columnconfigure(0, weight = 1)

    def _clear_intro(self) -> None:
        """
        This function clears the intro screen.
        """
        self._banner_label.grid_remove()
        self._start_button.grid_remove()
        self._option_button.grid_remove()
        self._root_window.option_clear()

    def _draw_game(self) -> None:
        """
        This method draws the game layout screen
        """
        self._root_window.rowconfigure(0, weight = 1)
        self._root_window.rowconfigure(1, weight = 10)
        self._root_window.columnconfigure(0, weight = 1)
        self._root_window.columnconfigure(1, weight = 10)
        self._root_window.columnconfigure(2, weight = 1)

        self._canvas.grid(rowspan = 2, columnspan = 3)

        self._black_label = tkinter.Label(master = self._root_window, text = 'Black:', font = _OPTION_FONT, foreground = 'black', background = _DEFAULT_BACKGROUND)
        self._black_label.grid(row = 0, column = 0, pady = 10, sticky = tkinter.N)

        self._white_label = tkinter.Label(master = self._root_window, text = 'White:  ', font = _OPTION_FONT, foreground = 'white', background = _DEFAULT_BACKGROUND)
        self._white_label.grid(row = 0, column = 2, pady = 10, sticky = tkinter.N)

        self._black_score = tkinter.Label(master = self._root_window, text = str(self._game.black_score()), font = _BANNER_FONT, foreground = 'black', background = _DEFAULT_BACKGROUND)
        self._black_score.grid(row = 0, column = 0)

        self._white_score = tkinter.Label(master = self._root_window, text = str(self._game.white_score()), font = _BANNER_FONT, foreground = 'white', background = _DEFAULT_BACKGROUND)
        self._white_score.grid(row = 0, column = 2)

        if self._game.current_player() == Othello.BLACK:
            self._current_player = "Black's Turn"
            self._current_color = 'black'
        else:
            self._current_player = "White's Turn"
            self._current_color = 'white'

        self._current_player_label = tkinter.Label(master = self._root_window, text = self._current_player, font = _BANNER_FONT, foreground = self._current_color, background = _DEFAULT_BACKGROUND)
        self._current_player_label.grid(row = 0, column = 1, padx = 10, pady = 10, sticky = tkinter.N)

        self._game_message_label = tkinter.Label(master = self._root_window, text = self._last_move, font = _DEFAULT_FONT, foreground = self._last_player, background = _DEFAULT_BACKGROUND)
        self._game_message_label.grid(row = 0, column = 1, padx = 10, pady = 10, sticky = tkinter.S)

        self._board_canvas = tkinter.Canvas(master = self._root_window, width = 1, height = 1, background = _BOARD_BACKGROUND)
        self._board_canvas.grid(row = 1, column = 0, rowspan = 1, columnspan = 3, sticky = tkinter.NSEW)

        self._restart_button = tkinter.Button(master = self._root_window, text = 'Play Again', font = _OPTION_FONT, command = self._restart)
        self._restart_button.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = tkinter.SW)

        self._quit_button = tkinter.Button(master = self._root_window, text = 'Quit', font = _OPTION_FONT, command = self._quit)
        self._quit_button.grid(row = 0, column = 2, padx = 10, pady = 10, sticky = tkinter.SE)

        self._board_canvas.bind('<Configure>', self._board_redraw)

        if self._game.win_result() == "":
            if self._game.current_player() == Othello.BLACK and self._ai_black:
                self._ai_move()
            elif self._game.current_player() == Othello.WHITE and self._ai_white:
                self._ai_move()
            else:
                self._board_canvas.bind('<Button-1>', self._on_board_click)

    def _board_draw(self) -> None:
        """
        This method redraws the board to fit into the screen.
        """
        self._board_canvas.delete(tkinter.ALL)
        self._xpad = 10
        self._ypad = 10
        self._board_canvas.create_line(self._xpad, self._ypad, self._board_canvas.winfo_width() - self._xpad, self._ypad)
        self._row_distance = (self._board_canvas.winfo_height() - (2 * self._xpad)) / self._rows
        current_row_height = self._xpad
        for row in range(self._rows):
            current_row_height += self._row_distance
            self._board_canvas.create_line(self._xpad, current_row_height, self._board_canvas.winfo_width() - self._xpad, current_row_height)

        self._board_canvas.create_line(self._xpad, self._ypad, self._xpad, self._board_canvas.winfo_height() - self._ypad)
        self._column_distance = (self._board_canvas.winfo_width() - (2 * self._ypad)) / self._columns
        current_column_width = self._ypad
        for column in range(self._columns):
            current_column_width += self._column_distance
            self._board_canvas.create_line(current_column_width, self._ypad, current_column_width, self._board_canvas.winfo_height() - self._ypad)

        disk_pad = 10

        for row in range(self._rows):
            for column in range(self._columns):
                if self._game.cell(row + 1, column + 1) == Othello.BLACK:
                    self._board_canvas.create_oval(self._xpad + disk_pad + column * self._column_distance, self._ypad + disk_pad + row * self._row_distance, self._xpad + (column + 1) * self._column_distance - disk_pad, self._ypad + (row + 1) * self._row_distance - disk_pad, outline = 'white', fill = 'black')
                elif self._game.cell(row + 1, column + 1) == Othello.WHITE:
                    self._board_canvas.create_oval(self._xpad + disk_pad + column * self._column_distance, self._ypad + disk_pad + row * self._row_distance, self._xpad + (column + 1) * self._column_distance - disk_pad, self._ypad + (row + 1) * self._row_distance - disk_pad, outline = 'black', fill = 'white')

    def _board_redraw(self, event:tkinter.Event) -> None:
        """
        This method redraws the board to fit into the screen.
        """
        self._board_draw()
        
    def _on_board_click(self, event:tkinter.Event) -> None:
        """
        This method registers a mouse click on the board.
        """
        try:
            row = int(((event.y - 10) // self._row_distance) + 1)
            column = int(((event.x - 10) // self._column_distance) + 1)
            current_player = self._game.current_player()
            self._game.move(row, column)
            if current_player == Othello.BLACK:
                self._last_move = "Black played Row {}, Column {}.".format(row, column)
                self._last_player = 'black'
            else:
                self._last_move = "White played Row {}, Column {}.".format(row, column)
                self._last_player = 'white'
            self._check_win()
            
        except Othello.InvalidMove:
            self._game_message_label.grid_remove()
            self._game_message_label = tkinter.Label(master = self._root_window, text = 'Invalid Move!  Try again.', font = _DEFAULT_FONT, foreground = 'red', background = _DEFAULT_BACKGROUND)
            self._game_message_label.grid(row = 0, column = 1, padx = 10, pady = 10, sticky = tkinter.S)
            self._game_message_label.grid()

    def _ai_move(self) -> None:
        """
        This method performs the game move for the ai.
        """
        current_player = self._game.current_player()
        ai_move = othello_ai.move(self._game)
        self._game.move(ai_move[0],ai_move[1])
        if current_player == Othello.BLACK:
                self._last_move = "Black played Row {}, Column {}.".format(ai_move[0], ai_move[1])
                self._last_player = 'black'
        else:
                self._last_move = "White played Row {}, Column {}.".format(ai_move[0], ai_move[1])
                self._last_player = 'white'
        self._check_win()

    def _clear_game_screen(self) -> None:
        """
        This method clears the game screen so it can be updated and redrawn.
        """
        self._restart_button.grid_remove()
        self._quit_button.grid_remove()
        self._canvas.grid_remove()
        self._black_label.grid_remove()
        self._white_label.grid_remove()
        self._black_score.grid_remove()
        self._white_score.grid_remove()
        self._current_player_label.grid_remove()
        self._game_message_label.grid_remove()
        self._board_canvas.grid_remove()
        

    def _check_win(self) -> None:
        """
        This method checks to see if there is a win condition.
        """
        result = self._game.win_result()
        if result == '':
            self._clear_game_screen()
            self._draw_game()
        else:
            self._clear_game_screen()
            self._draw_game()
            self._board_canvas.unbind('<Button-1>')

            if result == Othello.BLACK:
                self._game_message_label.grid_remove()
                self._game_message_label = tkinter.Label(master = self._root_window, text = 'Black is the Winner!', font = _DEFAULT_FONT, foreground = 'black', background = _DEFAULT_BACKGROUND)
                self._game_message_label.grid(row = 0, column = 1, padx = 10, pady = 10, sticky = tkinter.S)
                self._game_message_label.grid()
            elif result == Othello.WHITE:
                self._game_message_label.grid_remove()
                self._game_message_label = tkinter.Label(master = self._root_window, text = 'White is the Winner!', font = _DEFAULT_FONT, foreground = 'white', background = _DEFAULT_BACKGROUND)
                self._game_message_label.grid(row = 0, column = 1, padx = 10, pady = 10, sticky = tkinter.S)
                self._game_message_label.grid()
            else:
                self._game_message_label.grid_remove()
                self._game_message_label = tkinter.Label(master = self._root_window, text = 'Game Tied!', font = _DEFAULT_FONT, foreground = 'gray', background = _DEFAULT_BACKGROUND)
                self._game_message_label.grid(row = 0, column = 1, padx = 10, pady = 10, sticky = tkinter.S)
                self._game_message_label.grid()


    def _restart(self):
        """
        Restart Button
        """
        self._game = None
        self._rows = 8
        self._columns = 8
        self._black_plays_first = True
        self._white_in_top_left = True
        self._win_with_most = True
        self._ai_black = False
        self._ai_white = False
        self._restart_button.grid_remove()
        self._quit_button.grid_remove()
        self._clear_game_screen()
        self._intro()


    def _quit(self):
        """
        Quit Button
        """
        self._root_window.destroy()


    def _start_game(self) -> None:
        """
        This method starts the game.
        """
        self._clear_intro()
        self._game = Othello.Game(self._rows, self._columns, self._black_plays_first, self._white_in_top_left, self._win_with_most)
        self._last_move = ''
        self._last_player = 'black'

        self._draw_game()

if __name__ == '__main__':
    Othello_GUI().start()
