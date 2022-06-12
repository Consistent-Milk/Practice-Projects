from tkinter import *
import numpy as np

board_size = 600
symbol_size = ((board_size / 3) - (board_size / 8)) / 2
symbol_thickness = 50
symbol_X_color = '#EE4035'
symbol_O_color = '#0492CF'
Green_color = '#7BC043'


class Tic_Tac_Toe():

    def __init__(self):
        self.window = Tk()
        self.window.title('Tic-Tac-Toe')
        self.canvas = Canvas(self.window, width=board_size, height=board_size)
        self.canvas.pack()

        self.window.bind('<Button-1>', self.click)

        self.initialize_board()

        self.player_X_turns = True
        self.board_status = np.zeros(shape=(3, 3))

        self.player_X_starts = True
        self.reset_board = False
        self.gameover = False
        self.tie = False
        self.X_wins = False
        self.O_wins = False

        self.X_score = 0
        self.O_score = 0
        self.tie_score = 0

    def mainloop(self):
        self.window.mainloop()
    
    def initialize_board(self):
        for i in range(2):
            self.canvas.create_line(
                ((i + 1) * board_size) / 3, 
                0,
                ((i + 1) * board_size) / 3,
                board_size
            )
        
        for i in range(2):
            self.canvas.create_line(
                0, 
                ((i + 1) * board_size) / 3, 
                board_size, 
                ((i + 1) * board_size) / 3
            )
