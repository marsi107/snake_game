# class to create and interact with the snake

import pygame

import math # to round up and down the raw directions for positioning

class Snake:
    COLOR = 'yellow'
    INTIAL_POS_X = 7
    INTIAL_POS_Y = 17
    SPEED = 1
    INTIAL_DIR_X = 2
    INTIAL_DIR_Y = 0
    screen = None
    grid = None
    raw_dir = 'r'
    pos_x, pos_y = 0, 0
    dir_x, dir_y = 2, 0
    opposite_dir = 'l'
    body = None
    last_head_pos_x = 0
    last_head_pos_y = 0

    def __init__(self, screen, grid):
        self.screen = screen
        self.grid = grid
        self.reset()

    def change_direction(self, direction):
        # guardian to control that the snake doesn't go backwards
        if direction == self.opposite_dir:
            return
        if direction == 'u':
            self._change_snake_pos_based_on_raw_dir(direction)
            self.dir_x = 0
            self.dir_y = -2
            self.opposite_dir = 'd'
            self.raw_dir = 'u'
        elif direction == 'd':
            self._change_snake_pos_based_on_raw_dir(direction)
            self.dir_x = 0
            self.dir_y = 2
            self.opposite_dir = 'u'
            self.raw_dir = 'd'
        elif direction == 'l':
            self._change_snake_pos_based_on_raw_dir(direction)
            self.dir_x = -2
            self.dir_y = 0
            self.opposite_dir = 'r'
            self.raw_dir = 'l'
        elif direction == 'r':
            self._change_snake_pos_based_on_raw_dir(direction)
            self.dir_x = 2
            self.dir_y = 0
            self.opposite_dir = 'l'
            self.raw_dir = 'r'
        elif direction == 'esc':
            self.dir_x = 0
            self.dir_y = 0
        # * print('raw dir', self.raw_dir)

    # transform the position into cells and move the snake there when de direction is changed, 
    # so it could only move from cell to cell.
    # also rounded up and down depending the direction, so it doesn't go backwards
    def _change_snake_pos_based_on_raw_dir(self, direction):
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
            self.last_head_pos_x = self.pos_x
            self.last_head_pos_y = self.pos_y
            self.pos_x = raw_pos_x * self.grid.cell_width
            self.pos_y = raw_pos_y * self.grid.cell_height

    def draw_body(self):
        # * print('last_head_pos_x', self.last_head_pos_x)
        # * print('last_head_pos_y', self.last_head_pos_y)
        for i, segment in enumerate(self.body):
            if i == 0:
                # * print(f'segment0(dir) {segment[0]} segment1(pos_x) {segment[1]} segment2(pos_y) {segment[2]} / last_head_pos_x {self.last_head_pos_x} last_head_pos_y {self.last_head_pos_y}')
                if segment[0] == 'u':
                    segment[2] = self.pos_y - self.grid.cell_height
                    segment[1] = self.pos_x
                    if segment[2] <= self.last_head_pos_y:
                        segment[0] = self.raw_dir
                        # * print('raw dir changed', self.raw_dir)
                if segment[0] == 'd':
                    segment[2] = self.pos_y + self.grid.cell_height
                    segment[1] = self.pos_x
                    if segment[2] >= self.last_head_pos_y:
                        segment[0] = self.raw_dir
                        # * print('raw dir changed', self.raw_dir)
                if segment[0] == 'r':
                    segment[1] = self.pos_x - self.grid.cell_width
                    segment[2] = self.pos_y
                    if segment[1] <= self.last_head_pos_x:
                        segment[0] = self.raw_dir
                        # * print('raw dir changed', self.raw_dir)
                if segment[0] == 'l':
                    segment[1] = self.pos_x + self.grid.cell_width
                    segment[2] = self.pos_y
                    if segment[1] >= self.last_head_pos_x:
                        segment[0] = self.raw_dir
                        # * print('raw dir changed', self.raw_dir)
            else:
                pass
            snake_obj = pygame.Rect(segment[1], segment[2], self.grid.cell_width, self.grid.cell_height)
            pygame.draw.rect(self.screen, self.COLOR, snake_obj)
            #snake_collider_box = pygame.Rect(snake_obj)

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
        self.opposite_dir = 'l'
        self.raw_dir = 'r'
        self.body = [
            ['r', (self.INTIAL_POS_X-1) * self.grid.cell_width, (self.INTIAL_POS_Y) * self.grid.cell_height], 
            ['r', (self.INTIAL_POS_X-2) * self.grid.cell_width, (self.INTIAL_POS_Y) * self.grid.cell_height]
            ]