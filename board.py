from tile import Tile
class Board:
    
    DIMENSION = 9

    def __init__(self):
        self.board = []
        for i in range(self.DIMENSION):
            self.board.append([])
            for j in range(self.DIMENSION):
                self.board[i].append(Tile())
        # 9x9 board, list of lists of tiles
    

    def get_val(self, x, y):
        return self.board[x][y].get_val()

    
    def change_val(self, x, y, val = 0):
        """Changes the value stored in board
        """
        self.board[x][y].set_val(val)

    def is_won(self):
        """Return true iff the board is filled in completely and follows all rules of sudoku (all rows/columns have no repeated digits)
        """
        if not self.is_full:
            return False
        matr = self.get_int_matrix()
        for i in range(len(matr)):
            row_lst = []
            col_lst = []
            for j in range(len(matr[i])):
                row_lst.append(matr[j][i])
                col_lst.append(matr[i][j])
            if len(set(row_lst)) != len(row_lst):
                return False
            if len(set(col_lst)) != len(col_lst):
                return False
        return True
    
    def get_int_matrix(self):
        """Returns a List of Lists of Integers, where every element is the corresponding value in the board
        """
        outer_lst = []
        for i in range(0, self.DIMENSION):
            int_lst = []
            for j in range(0, self.DIMENSION):
                int_lst.append(self.get_val(i, j))
            outer_lst.append(int_lst)
        return outer_lst

    def is_full(self):
        for i in range(self.DIMENSION):
            for j in range(self.DIMENSION):
                if self.get_val(i, j) == 0:
                    return False
        return True

    def new_game(self, difficulty = 0):
        """Set the board's tiles to a valid starting board
        """
        pass
    
    def nice_string(self):
        """Returns a string representation of the board that is easily human readable
        """
        out = ""
        for i in range(self.DIMENSION):
            for j in range(self.DIMENSION):
                out = out + " " + str(self.get_val(i, j)) + " "
                if j == 2 or j == 5:
                    out = out + "|"
            if i == 2 or i == 5:
                out = out + "\n" + " -  -  - + -  -  - + -  -  -"
            out = out + "\n"
        return out
            


import random
s = Board()
while(not s.is_won()):
    s = Board()
    for i in range(0, 9):
        for j in range(0, 9):
            x = random.randint(1,9)
            s.change_val(i, j, x)
    print(s.nice_string())

# print(s.get_int_matrix())
print(s.nice_string())
