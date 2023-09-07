# class to create and interact with the fruit 

import random # to place the fruit randomly

class Apple:
    APPLE_COLOR = 'green'
    pos_x = 0
    pos_y = 0
    grid = None

    def __init__(self, grid):
        self.grid = grid
        self.generate_new_apple_position()

    def generate_new_apple_position(self):
        # get a random number inside the boundaries of the grid, 
        # and multiply per grid size to calculate the pixel coordinates
        self.pos_x = random.randint(0, self.grid.NUM_COLS - 1) * self.grid.cell_width
        self.pos_y = random.randint(0, self.grid.NUM_ROWS - 1) * self.grid.cell_height