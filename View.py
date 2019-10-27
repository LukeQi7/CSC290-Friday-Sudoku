<<<<<<< HEAD

=======
from board import Board
>>>>>>> 1c3518085d0112dea8e44579fc08e2aeb4ae406f
import pygame

pygame.font.init()
BLACK = (0, 0, 0)


class GuiBoard:

    def __init__(self, row, col, height, width):
        """"Intializes the board """
        self.row = row
        self.col = col
        self.height = height
        self.width = width
        self.cells = None #will store the cells in an array(2-d), the elements will be taken from the board
        self.GUI_board = None #will store a an array representing board in 2-d
        self.clicked = None #will store the row,col of the cell clicked

    def place_pencil_value(self, temp_value):
        """"Pencils in the temporary value"""

        row_index, col_index = self.clicked
        self.cells[row_index][col_index].set_temp(temp_value)

    def place_final_value(self, final_value):
        """"Enters the number pressed enter on to the cell,
        Returns True - if final_value is a valid
        Returns False - otherwise
        """

        row_index, col_index = self.clicked
        if self.cells[row_index][col_index].get_val(row_index, col_index) == 0:
            self.cells[row_index][col_index].set_value(final_value)
            #update the model

            #check here if the board is valid and solvable
                #return True, if valid
            #else
                #set the cells[row_index][col_index].set_value(0)
                #set the cells[row_index][col_index].set_temp(0)
                #update model
                #return False

    def draw_inner_square(x, y): #change this function to only draw the vertical&horizontal lines, see draw(Board) in link i send you
        """ Recursive rectangle function. """

        length = 450/9
        y = 0
        for i in range(9):
            x = 0
            for j in range(9):
                pygame.draw.rect(win, BLACK, [x, y, length, length], 1)
                win.blit(pygame.font.SysFont('Arial', 25).render('', True, (0, 0, 0)), (x + 20, y + 20))
                if (j+1) % 3 == 0:
                    x += length + 2
                else:
                    x += length
            if (i+1) % 3 == 0:
                y += length + 2
            else:
                y += length
            win.blit(pygame.font.SysFont('Arial', 25).render('input number please: ', True, (0, 0, 0)), (0, 455))
            win.blit(pygame.font.SysFont('Arial', 25).render('input location please: ', True, (0, 0, 0)), (0, 475))


class Cell:
    row = 9
    column = 9

    def __int__(self, value, row, col, height, width):
        """"Initializes cell"""

        self.value = value
        self.temp = 0
        self.row = row
        self.col = col
        self.height = height
        self.width = width
        self.selected = False #Setting the cell to be false by default

    def draw_cells(self, window):
        """Draws the cells in the board"""

        font_of_cell = pygame.font.SysFont("arial", 25)
        gap = self.width/9
        x = gap * self.row
        y = gap * self.col

        if self.temp !=0 and self.value == 0:
            Board.set_penciled(x, y, self.temp, True)
            temp_text = font_of_cell.render(str(self.temp), 1, (81, 81, 81)) #pencil-in the value
            win.blit(temp_text, (x + 5, y + 5)) #inputing pencil-in in display(at corner)
        elif self.value != 0:
            Board.set_value(x, y, self.value)
            value_text = font_of_cell.render(str(self.temp), 1, BLACK)
            win.blit(value_text, (x + (gap/2 - text.get_width()/2), y +
                            (gap/2 - text.get_height()/2))) #inputting value in display
        if self.selected:
            pygame.draw.rect(win, (0,245,255), (x, y, self.width,
                                                self.height), 2) #Show highlighted selected screen

    def set_value(self, value):
        self.value = value

    def set_temp(self, temp):
        self.temp = temp


def main():
    win = pygame.display.set_mode((450, 500))
    pygame.display.set_caption("Friday Sudoku")
    win.fill((255, 255, 255))







run = True
draw_inner_square(0, 0)
pygame.display.flip()
active = False
text = ''
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

