from typing import NamedTuple, Literal

"""
3-8. [5] Tic-tac-toe is a game played on an n × n board (typically n = 3) where two
players take consecutive turns placing “O” and “X” marks onto the board cells.
The game is won if n consecutive “O” or ‘X” marks are placed in a row, column,
or diagonal. Create a data structure with O(n) space that accepts a sequence
of moves, and reports in constant time whether the last move won the game.
"""

class TTTMove(NamedTuple):
    player: Literal['X','O']
    col: int
    row: int
    

class TicTacToe():
    def __init__(self, size: int) -> None:
        self.size = size
        self.o_rows = [0 for _ in range(self.size)]
        self.o_cols = [0 for _ in range(self.size)]
        self.o_diags = [0,0]
        self.x_rows = [0 for _ in range(self.size)]
        self.x_cols = [0 for _ in range(self.size)]
        self.x_diags = [0,0]

    def playMove(self, move: TTTMove) -> None:
        if move.player == "X":
            self.x_cols[move.col] += 1
            self.x_rows[move.row] += 1
            if move.col == move.row:
                self.x_diags[0] += 1
            if move.col + move.row == self.size - 1:
                self.x_diags[1] += 1
            if self.x_cols[move.col] == self.size or self.x_rows[move.row] == self.size or self.x_diags[0] == self.size or self.x_diags[1] == self.size:
                print("X wins!")
        if move.player == "O":
            self.o_cols[move.col] += 1
            self.o_rows[move.row] += 1
            if move.col == move.row:
                self.o_diags[0] += 1
            if move.col + move.row == self.size - 1:
                self.o_diags[1] += 1
            if self.o_cols[move.col] == self.size or self.o_rows[move.row] == self.size or self.o_diags[0] == self.size or self.o_diags[1] == self.size:
                print("O wins!")
    


game = TicTacToe(3)
game.playMove(TTTMove("O",0,0))
game.playMove(TTTMove("O",0,1))
game.playMove(TTTMove("O",0,2))