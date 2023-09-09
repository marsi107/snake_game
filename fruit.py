# class to create and interact with the fruit 

import pygame

import random # to place the fruit randomly

class Apple:
    COLOR = 'green'
    pos_x = 0
    pos_y = 0
    screen = None
    grid = None

    def __init__(self, screen, grid):
        self.screen = screen
        self.grid = grid
        self.generate_new_apple_position()

    def generate_new_apple_position(self):
        # get a random number inside the boundaries of the grid, 
        # and multiply per grid size to calculate the pixel coordinates
        self.pos_x = random.randint(0, self.grid.NUM_COLS - 1)
        self.pos_y = random.randint(0, self.grid.NUM_ROWS - 1)

    def draw(self):
        transformed_pos_x = self.pos_x  * self.grid.cell_width
        transformed_pos_y = self.pos_y * self.grid.cell_height
        apl_obj = pygame.Rect(transformed_pos_x, transformed_pos_y, self.grid.cell_width, self.grid.cell_height)
        pygame.draw.rect(self.screen, self.COLOR, apl_obj)
        apple_collider_box = pygame.Rect(apl_obj)
        return apple_collider_box