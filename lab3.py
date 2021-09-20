import pygame
import sys

WIN_WIDTH = 700
WIN_HEIGHT = 570

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 235, 20)

sc = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))


def draw(color):
    sc.fill(WHITE)

    x_top = WIN_WIDTH //2
    pygame.draw.rect(sc, color, pygame.Rect(x_top-10, 0, 20, 10))
    for i in range(11):
        pygame.draw.rect(sc, color, pygame.Rect(x_top+20*i, 10+10*i, 20, 10))
        pygame.draw.rect(sc, color, pygame.Rect(x_top-20-20*i, 10+10*i, 20, 10))

        pygame.draw.rect(sc, color, pygame.Rect(540-20*i, 130+40*i, 20, 40))
        pygame.draw.rect(sc, color, pygame.Rect(140+20*i, 130+40*i, 20, 40))

        if i < 6:
            pygame.draw.rect(sc, color, pygame.Rect(x_top-20+40*i, 550-20*i, 40, 20))
            pygame.draw.rect(sc, color, pygame.Rect(x_top-20-40*i, 550-20*i, 40, 20))

    pygame.draw.rect(sc, WHITE, pygame.Rect(x_top-10, 10, 20, 10))
    pygame.draw.rect(sc, color, pygame.Rect(130, 110, 420, 10))

    pygame.draw.rect(sc, color, pygame.Rect(130, 110, 10, 350))
    pygame.draw.rect(sc, color, pygame.Rect(560, 110, 10, 350))

    pygame.display.update()



if __name__ == '__main__':
    while 1:
        draw(GREEN)
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                sys.exit()
            if i.type == pygame.KEYDOWN:
                draw(GREEN)