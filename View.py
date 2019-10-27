
import pygame

pygame.init()
pygame.display.set_caption("Friday Sudoku")
win = pygame.display.set_mode((450, 500))
win.fill((255, 255, 255))
BLACK = (0, 0, 0)


def draw_inner_square(x, y):
    """ Recursive rectangle function. """
    length = 450/9
    y = 0
    for i in range(9):
        x = 0
        for j in range(9):
            pygame.draw.rect(win, BLACK, [x, y, length, length], 1)
            win.blit(pygame.font.SysFont('Arial', 25).render('1', True, (0, 0, 0)), (x + 20, y + 20))
            if (j+1)%3 == 0:
                x += length + 2
            else:
                x += length
        if (i+1)%3 == 0:
            y += length + 2
        else:
            y += length
    win.blit(pygame.font.SysFont('Arial', 25).render('input number please: ', True, (0, 0, 0)), (0, 455))
    win.blit(pygame.font.SysFont('Arial', 25).render('input location please: ', True, (0, 0, 0)), (0, 475))


run = True
draw_inner_square(0, 0)
pygame.display.flip()
active = False
text = ''
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

