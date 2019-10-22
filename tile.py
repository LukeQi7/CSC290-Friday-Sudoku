class Tile:

    def __init__(self):
        self.value = 0
        self.penciled = {}
        for i in range(1,9):
            self.penciled[i] = False

    def get_val(self):
        return self.value
    
    def set_val(self, val):
        self.value = val

    def get_penciled(self, num):
        return self.penciled[num]
    
    def set_penciled(self, num, val = False):
        """Changes the boolean penciled value of the given number to the boolean val
        """
        self.penciled[num] = val

    def switch_penciled(self, num):
        """Switches the boolean (False->True/True->False) penciled value of the given number for this tile
        """
        self.penciled[num] = not self.penciled[num]
