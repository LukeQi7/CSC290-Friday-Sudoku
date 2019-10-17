from tile import Tile
class Board:
    
    def __init__(self):
        self.board = [[tile.Tile()]*9]*9
        # 9x9 board, list of lists of tiles
    

    def get_val(self, x, y):
        return board[x][y]


    def new_game(self, difficulty = 0):
        """Set the board's tiles to a valid starting board
        """
        pass
    
