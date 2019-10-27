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

    def set_penciled(self, x, y, val, penciled_boolean):
        self.board[x][y].set_penciled(val, penciled_boolean)

    def set_value(self, x, y, val):
        self.board[x][y] = val

    def get_val(self, x, y):
        return self.board[x][y].get_val()

    def get_penciled(self, x, y, num):
        """Return the dictionary of booleans that represents the penciled values for the specified tile
        """
        return self.board[x][y].get_penciled(num)

    def change_val(self, x, y, val=0):
        """Changes the value stored in board, and sets all penciled values to false
        """
        self.board[x][y].set_val(val)
        for i in range(1, 10):
            self.board[x][y].set_penciled(i, False)

    def is_won(self):
        """Return true iff the board is filled in completely and follows all rules of sudoku (all rows/columns and 3x3 sub-squares have no repeated digits)
        """
        if not self.is_full:
            return False
        matr = self.get_int_matrix()

        # Check rows and columns
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

        # Check 3x3 squares
        squares = []
        for i in range(3):
            for j in range(3):
                rows = matr[(3 * j):(3 * j) + 3]
                for x in range(len(rows)):
                    rows[x] = rows[x][(3 * i):(3 * i) + 3]
                squares.append(rows)
        for i in squares:
            square_lst = []
            for col in i:
                square_lst.extend(col)
            if len(set(square_lst)) != len(square_lst):
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

    def new_game(self, difficulty=0):
        """Set the board's tiles to a valid starting board
        """
        pass

    def get_user_input(self):
        """Asks the user for a location, as well as a value. Checks if the location is valid, then returns as a list.
        """
        x = int(input("Row: "))
        y = int(input("Column: "))
        if (x > 8 or y > 8) or (x < 0 or y < 0):
            print("Invalid placement")
            self.get_user_input()
        else:
            value = int(input("Number: "))
            return [x, y, value]

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
