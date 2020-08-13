import pygame, sys
from pygame.locals import *
from random import randint

BLACK = (0, 0, 0)
snake_length = 50
snake_width = 5


class Snake:
   def __init__(self, pos_x, pos_y):
      self.pos_x = randint(0, pos_x - snake_length - 10)
      self.pos_y = randint(0, pos_y)
      self.snake = pygame.Rect((self.pos_x, self.pos_y, snake_length, snake_width))

   def draw_rect(self, area):
      pygame.draw.rect(area, BLACK, (self.pos_x, self.pos_y, snake_length, snake_width))

   def move(self, area, width):
      for x_move in range(0, 100):
         self.snake.move(x_move, 0)
        # self.rect.move(area, BLACK, (self.pos_x + x_move, self.pos_y, snake_length, snake_width))
        # pygame.time.delay(100)
         print(self.pos_x, self.pos_y)


class Apple:
   def __init__(self, pos_x, pos_y):
      self.pos_x = randint(0, pos_x)
      self.pos_y = randint(0, pos_y)

   def draw(self, area):
      pygame.draw.circle(area, BLACK, [self.pos_x, self.pos_y], 3, 3)





