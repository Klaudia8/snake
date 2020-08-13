import pygame
import sys
#from snake import *
from random import randint

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
snake_length = 5#50
snake_width = 5
up_arrow = 273 #K_UP
down_arrow = 274 #K_DOWN
right_arrow = 275 #K_RIGHT
left_arrow = 276 #K_LEFT
QUIT = 12


def snake_move(key):
    if key == up_arrow:
        step = (0, -1)
    elif key == down_arrow:
        step = (0, 1)
    elif key == right_arrow:
        step = (1, 0)

    return step


def snake_coordinates(screen_width, screen_height):
    pos_x = randint(0, screen_width - snake_length - 10)
    pos_y = randint(0, screen_height)
    snake_pos = pygame.Rect((pos_x, pos_y, snake_length, snake_width))
    return snake_pos


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

    snake = snake_coordinates(width, height)
    direction = (1, 0)

    while True:
        events = pygame.event.get()
        for event in events:  # what the fuck?! why is that working this way?!
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYUP:
                if event.key in [up_arrow, down_arrow, right_arrow]:
                    direction = snake_move(event.key)

        snake = snake.move(direction)

        screen.fill((60, 65, 44))
        pygame.time.delay(100)
        pygame.draw.rect(screen, BLACK, snake, 0)
        pygame.display.update()
