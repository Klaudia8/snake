import pygame
import sys
from random import randint
import time

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
global snake_length
snake_length = 54
snake_width = 6
apple_size = 3
up_arrow = 273  # K_UP
down_arrow = 274  # K_DOWN
right_arrow = 275  # K_RIGHT
left_arrow = 276  # K_LEFT
QUIT = 12


def snake_move(old_move, key):
    if key == up_arrow:
        if old_move != (0, snake_width):
            step = (0, -snake_width)
    elif key == down_arrow:
        if old_move != (0, -snake_width):
            step = (0, snake_width)
    elif key == right_arrow:
        if old_move != (-snake_width, 0):
            step = (snake_width, 0)
    elif key == left_arrow:
        if old_move != (snake_width, 0):
            step = (-snake_width, 0)
    else:
        step = old_move

    return step


def snake_init_coordinates(screen_width, screen_height):
    pos_x = randint(0, screen_width - snake_length - 10)
    pos_y = randint(0, screen_height)
    snake_parts = [pygame.Rect((pos_x+i, pos_y, snake_width, snake_width)) for i in range(0, snake_length, snake_width)]
    return snake_parts


def new_position(snake_parts, arrow):
    new_snake = snake_parts[:-1]
    head = snake_parts[0]
    snake_head = pygame.Rect((head[0] + arrow[0], head[1] + arrow[1], snake_width, snake_width))
    new_snake.insert(0, snake_head)
    return new_snake


def put_apple(screen_width, screen_height):
    pos_x = randint(0, screen_width)
    pos_y = randint(0, screen_height)
    return [pos_x, pos_y]


# checks whether snake ate an apple
def check_apple_eaten(apple_pos, snake_parts, points):
    global snake_length, score
    for snake_part in snake_parts:
        eaten = snake_part.collidepoint(apple_pos[0], apple_pos[1])
        if eaten:
            break

    if eaten:
        snake_parts.append(pygame.Rect((snake_part[0], snake_part[1], snake_width, snake_width)))
        points += 1

    return points


if __name__ == '__main__':
    # display window
    WIDTH = 500
    HEIGHT = 500

    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Snake 2D')
    # screen information
    screen = pygame.display.get_surface()

    screen.fill((60, 65, 44))
    pygame.init()

    score = 0
    snake = snake_init_coordinates(WIDTH, HEIGHT)
    direction = (5, 0)
    start_time = time.time()
    apple = put_apple(WIDTH, HEIGHT)
    apple_time = randint(5, 15)  # apple is on the screen between 5s and 15s

    while True:
        events = pygame.event.get()
        for event in events:  # what the fuck?! why is that working this way?!
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYUP:
                if event.key in [up_arrow, down_arrow, right_arrow, left_arrow]:
                    direction = snake_move(direction, event.key)

        snake = new_position(snake, direction)

        screen.fill((60, 65, 44))
        pygame.time.delay(100)
        for part in snake:
            pygame.draw.rect(screen, BLACK, part, 0)

        elapsed_time = round((time.time() - start_time)*10)  # rounded time in seconds multiplied by 10

        if elapsed_time % 120 == 0:
            apple = put_apple(WIDTH, HEIGHT)

        if apple:
            pygame.draw.circle(screen, BLACK, apple, apple_size)

        new_score = check_apple_eaten(apple, snake, score)
        if new_score - score == 1:
            print('new score: {}'.format(new_score))
            apple = []
            apple = put_apple(WIDTH, HEIGHT)
        score = new_score

        pygame.display.update()
