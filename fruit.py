# class to create and interact with the fruit

import pygame 

import random # to place the fruit randomly

class Apple:
    APPLE_COLOR = 'green'
    APPLE_SIZE = 10
    apple_pos = 0
    max_x, max_y = 0, 0

    def __init__(self, max_x, max_y):
        self.max_x = max_x
        self.max_y = max_y
        self.generate_new_apple_position()

    def generate_new_apple_position(self):
        x = random.randint(0, self.max_x)
        y = random.randint(0, self.max_y)
        self.apple_pos = pygame.Vector2(x, y)