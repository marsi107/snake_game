# class to create and interact with the fruit

import pygame 

import random # to place the fruit randomly

class Apple:
    APPLE_COLOR = 'green'
    APPLE_SIZE = 10
    apple_pos = 0
    max_x, max_y = 0, 0

    def __init__(self, max_x, max_y):
        # set limit minus apple_size so it doesn't appear outside
        self.max_x = max_x - self.APPLE_SIZE
        self.max_y = max_y - self.APPLE_SIZE
        self.generate_new_apple_position()

    def generate_new_apple_position(self):
        # set first limit as apple_size so it doesn't appear outside
        x = random.randint(self.APPLE_SIZE, self.max_x)
        y = random.randint(self.APPLE_SIZE, self.max_y)
        self.apple_pos = pygame.Vector2(x, y)