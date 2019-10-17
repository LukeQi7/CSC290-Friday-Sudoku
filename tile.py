class Tile:

    def __init__(self):
        self.value = 0
        self.penciled = {}
        for i in range(1,9):
            self.penciled[i] = False

    def get_val(self):
        return self.value

    def get_penciled(self, num):
        return self.penciled[num]