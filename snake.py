# class to create and interact with the snake

import pygame

import math # to round up and down the raw directions for positioning

E_SEGMENT = {
    'dir': 0,
    'x': 1,
    'y': 2,
    'last_x': 3,
    'last_y': 4
}
E_DIR_TO_OPOSSITE_DIR = {
    'u': 'd',
    'd': 'u',
    'l': 'r',
    'r': 'l'
}

class Snake:
    HEAD_COLOR = 'blue'
    BODY_COLOR = 'yellow'
    INTIAL_POS_X = 7
    INTIAL_POS_Y = 17
    INITIAL_DIR = 'r'
    
    screen = None
    grid = None
    pos_x, pos_y = 0, 0
    dir = INITIAL_DIR
    opposite_dir = 'l'
    body = None

    def __init__(self, screen, grid):
        self.screen = screen
        self.grid = grid
        self.reset()

    def change_direction(self, direction):
        # guardian to control that the snake doesn't go backwards
        if direction == self.opposite_dir:
            return
        self.dir = direction
        self.opposite_dir = E_DIR_TO_OPOSSITE_DIR[direction]

    def add_segment_to_body(self):
        last_i = len(self.body) - 1
        last_seg_dir = self.body[last_i][E_SEGMENT['dir']]
        new_segment = [last_seg_dir,0,0,0,0]
        self.body.append(new_segment)

    # set snake speed constant based on the direction given above
    def move(self):
        if self.dir == 'u':
            self.pos_y -= 1
        if self.dir == 'd':
            self.pos_y += 1
        if self.dir == 'l':
            self.pos_x -= 1
        if self.dir == 'r':
            self.pos_x += 1
        print('snake_pos_x', self.pos_x)
        print('snake_pos_y', self.pos_y)

    def draw_head(self):
        transformed_pos_x = self.pos_x * self.grid.cell_width
        transformed_pos_y = self.pos_y * self.grid.cell_height
        snake_obj = pygame.Rect(transformed_pos_x, transformed_pos_y, self.grid.cell_width, self.grid.cell_height)
        pygame.draw.rect(self.screen, self.HEAD_COLOR, snake_obj)
        snake_collider_box = pygame.Rect(snake_obj)
        return snake_collider_box

    # reset all parameters
    def reset(self):
        self.pos_x = self.INTIAL_POS_X
        self.pos_y = self.INTIAL_POS_Y
        self.dir = self.INITIAL_DIR
        self.opposite_dir = 'l'
        self.body = [
            [self.INITIAL_DIR, (self.INTIAL_POS_X-1), self.INTIAL_POS_Y, self.INTIAL_POS_X, self.INTIAL_POS_Y],
            [self.INITIAL_DIR, (self.INTIAL_POS_X-2), self.INTIAL_POS_Y, self.INTIAL_POS_X-1, self.INTIAL_POS_Y]
            ]