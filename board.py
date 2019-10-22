from tile import Tile
class Board:
    
    def __init__(self):
        self.board = [[Tile()]*9]*9
        # 9x9 board, list of lists of tiles
    

    def get_val(self, x, y):
        return board[x][y].get_val()

    
    def change_val(self, x, y, val = 0):
        """Changes the value stored in board
        """
        board[x][y].set_val(val)


    def new_game(self, difficulty = 0):
        """Set the board's tiles to a valid starting board
        """
        pass
    
