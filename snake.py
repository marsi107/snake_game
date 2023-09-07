# class to create and interact with the snake

import math # to round up and down the raw directions for positioning

class Snake:
    COLOR = 'yellow'
    INTIAL_POS_X = 7
    INTIAL_POS_Y = 17
    SPEED = 1
    INTIAL_DIR_X = 2
    INTIAL_DIR_Y = 0
    grid = None
    raw_dir = 'r'
    pos_x, pos_y = 0, 0
    dir_x, dir_y = 2, 0
    opposite_snake_direction = 'l'

    def __init__(self, grid):
        self.grid = grid
        self.pos_x = self.INTIAL_POS_X * grid.cell_width
        self.pos_y = self.INTIAL_POS_Y * grid.cell_height

    def change_snake_direction(self, direction):
        # guardian to control that the snake doesn't go backwards
        if direction == self.opposite_snake_direction:
            return
        if direction == 'u':
            self.change_raw_dir(direction)
            self.dir_x = 0
            self.dir_y = -2
            self.opposite_snake_direction = 'd'
            self.raw_dir = 'u'
        elif direction == 'd':
            self.change_raw_dir(direction)
            self.dir_x = 0
            self.dir_y = 2
            self.opposite_snake_direction = 'u'
            self.raw_dir = 'd'
        elif direction == 'l':
            self.change_raw_dir(direction)
            self.dir_x = -2
            self.dir_y = 0
            self.opposite_snake_direction = 'r'
            self.raw_dir = 'l'
        elif direction == 'r':
            self.change_raw_dir(direction)
            self.dir_x = 2
            self.dir_y = 0
            self.opposite_snake_direction = 'l'
            self.raw_dir = 'r'
        elif direction == 'esc':
            self.dir_x = 0
            self.dir_y = 0

    # transform the position into cells and move the snake there when de direction is changed, 
    # so it could only move from cell to cell.
    # also rounded up and down depending the direction, so it doesn't go backwards
    def change_raw_dir(self, direction):
        raw_pos_x, raw_pos_y = 0, 0
        if direction != self.raw_dir:
            if self.raw_dir == 'u':
                raw_pos_y = math.floor(self.pos_y / self.grid.cell_height)
                if direction == 'r':
                    raw_pos_x = math.ceil(self.pos_x / self.grid.cell_width)
                else:
                    raw_pos_x = math.floor(self.pos_x / self.grid.cell_width)
            if self.raw_dir == 'd':
                raw_pos_y = math.ceil(self.pos_y / self.grid.cell_height)
                if direction == 'r':
                    raw_pos_x = math.ceil(self.pos_x / self.grid.cell_width)
                else:
                    raw_pos_x = math.floor(self.pos_x / self.grid.cell_width)
            if self.raw_dir == 'r':
                raw_pos_x = math.ceil(self.pos_x / self.grid.cell_width)
                if direction == 'u':
                    raw_pos_y = math.floor(self.pos_y / self.grid.cell_height)
                else:
                    raw_pos_y = math.ceil(self.pos_y / self.grid.cell_height)
            if self.raw_dir == 'l':
                raw_pos_x = math.floor(self.pos_x / self.grid.cell_width)
                if direction == 'u':
                    raw_pos_y = math.floor(self.pos_y / self.grid.cell_height)
                else:
                    raw_pos_y = math.ceil(self.pos_y / self.grid.cell_height)
            self.pos_x = raw_pos_x * self.grid.cell_width
            self.pos_y = raw_pos_y * self.grid.cell_height

    # set snake speed constant based on the direction given above
    def move(self):
        self.pos_x += self.dir_x * self.SPEED
        self.pos_y += self.dir_y * self.SPEED

    # reset all parameters
    def reset(self):
        self.pos_x = self.INTIAL_POS_X * self.grid.cell_width
        self.pos_y = self.INTIAL_POS_Y * self.grid.cell_height
        self.dir_x = self.INTIAL_DIR_X
        self.dir_y = self.INTIAL_DIR_Y
        self.opposite_snake_direction = 'l'
        self.raw_dir = 'r'