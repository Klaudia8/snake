import pygame, sys
from pygame.locals import *
from snake import *

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)


def input(events):
   for event in events:
      if event.type == QUIT:
         sys.exit(0)
      else:
         print(event)


if __name__ == '__main__':
    # display window
    width = 500
    height = 500

    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Snake 2D')
    # screen information
    screen = pygame.display.get_surface()

    screen.fill((60, 65, 44))
    pygame.init()

    snake = Snake(width, height)
    apple = Apple(width, height)

    while True:
        input(pygame.event.get())
        snake.draw_rect(screen)
        snake.draw_rect(screen)
        apple.draw(screen)
        snake.move(screen, width)
        pygame.display.update()