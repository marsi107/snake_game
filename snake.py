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
                if segment[E_SEGMENT['dir']] == 'u':
                    segment[E_SEGMENT['y']] = self.pos_y + self.grid.cell_height
                    segment[E_SEGMENT['x']] = self.pos_x
                    if (segment[E_SEGMENT['y']] >= self.last_head_pos_y) and (self.raw_dir != segment[E_SEGMENT["dir"]]):
                        print(f'raw dir changed to {self.raw_dir} and segment dir is {segment[E_SEGMENT["dir"]]} from u')
                        segment[E_SEGMENT['dir']] = self.raw_dir
                        segment[E_SEGMENT['last_y']] = segment[E_SEGMENT['y']]
                        #print(f'raw dir changed to {self.raw_dir} and segment dir is {segment[E_SEGMENT["dir"]]}')
                if segment[E_SEGMENT['dir']] == 'd':
                    segment[E_SEGMENT['y']] = self.pos_y - self.grid.cell_height
                    segment[E_SEGMENT['x']] = self.pos_x
                    if (segment[E_SEGMENT['y']] <= self.last_head_pos_y) and (self.raw_dir != segment[E_SEGMENT["dir"]]):
                        print(f'raw dir changed to {self.raw_dir} and segment dir is {segment[E_SEGMENT["dir"]]} from d')
                        segment[E_SEGMENT['dir']] = self.raw_dir
                        segment[E_SEGMENT['last_y']] = segment[E_SEGMENT['y']]
                        #print('raw dir changed', self.raw_dir)
                if segment[E_SEGMENT['dir']] == 'r':
                    segment[E_SEGMENT['x']] = self.pos_x - self.grid.cell_width
                    segment[E_SEGMENT['y']] = self.pos_y
                    if (segment[E_SEGMENT['x']] <= self.last_head_pos_x)  and (self.raw_dir != segment[E_SEGMENT["dir"]]):
                        print(f'raw dir changed to {self.raw_dir} and segment dir is {segment[E_SEGMENT["dir"]]} from r')
                        segment[E_SEGMENT['dir']] = self.raw_dir
                        segment[E_SEGMENT['last_x']] = segment[E_SEGMENT['x']]
                        #print('raw dir changed', self.raw_dir)
                if segment[E_SEGMENT['dir']] == 'l':
                    segment[E_SEGMENT['x']] = self.pos_x + self.grid.cell_width
                    segment[E_SEGMENT['y']] = self.pos_y
                    if (segment[E_SEGMENT['x']] >= self.last_head_pos_x) and (self.raw_dir != segment[E_SEGMENT["dir"]]):
                        print(f'raw dir changed to {self.raw_dir} and segment dir is {segment[E_SEGMENT["dir"]]} from l')
                        segment[E_SEGMENT['dir']] = self.raw_dir
                        segment[E_SEGMENT['last_x']] = segment[E_SEGMENT['x']]
                        #print('raw dir changed', self.raw_dir)
            else:
                prev_elem = i - 1

                if segment[E_SEGMENT['dir']] == 'u':
                    segment[E_SEGMENT['y']] = self.body[prev_elem][E_SEGMENT['y']] + self.grid.cell_height
                    segment[E_SEGMENT['x']] = self.body[prev_elem][E_SEGMENT['x']]
                    if (segment[E_SEGMENT['y']] >= self.body[prev_elem][E_SEGMENT['last_y']]) and (self.body[prev_elem][E_SEGMENT['dir']] != segment[E_SEGMENT["dir"]]):
                        segment[E_SEGMENT['dir']] = self.body[prev_elem][E_SEGMENT['dir']]
                        segment[E_SEGMENT['last_y']] = segment[E_SEGMENT['y']]
                        # * print('raw dir changed', self.raw_dir)
                if segment[E_SEGMENT['dir']] == 'd':
                    segment[E_SEGMENT['y']] = self.body[prev_elem][E_SEGMENT['y']] - self.grid.cell_height
                    segment[E_SEGMENT['x']] = self.body[prev_elem][E_SEGMENT['x']]
                    if (segment[E_SEGMENT['y']] <= self.body[prev_elem][E_SEGMENT['last_y']]) and (self.body[prev_elem][E_SEGMENT['dir']] != segment[E_SEGMENT["dir"]]):
                        segment[E_SEGMENT['dir']] = self.body[prev_elem][E_SEGMENT['dir']]
                        segment[E_SEGMENT['last_y']] = segment[E_SEGMENT['y']]
                        # * print('raw dir changed', self.raw_dir)
                if segment[E_SEGMENT['dir']] == 'r':
                    segment[E_SEGMENT['x']] = self.body[prev_elem][E_SEGMENT['x']] - self.grid.cell_width
                    segment[E_SEGMENT['y']] = self.body[prev_elem][E_SEGMENT['y']]
                    if (segment[E_SEGMENT['x']] <= self.body[prev_elem][E_SEGMENT['last_x']]) and (self.body[prev_elem][E_SEGMENT['dir']] != segment[E_SEGMENT["dir"]]):
                        segment[E_SEGMENT['dir']] = self.body[prev_elem][E_SEGMENT['dir']]
                        segment[E_SEGMENT['last_x']] = segment[E_SEGMENT['x']]
                        # * print('raw dir changed', self.raw_dir)
                if segment[E_SEGMENT['dir']] == 'l':
                    segment[E_SEGMENT['x']] = self.body[prev_elem][E_SEGMENT['x']] + self.grid.cell_width
                    segment[E_SEGMENT['y']] = self.body[prev_elem][E_SEGMENT['y']]
                    if (segment[E_SEGMENT['x']] >= self.body[prev_elem][E_SEGMENT['last_x']]) and (self.body[prev_elem][E_SEGMENT['dir']] != segment[E_SEGMENT["dir"]]):
                        segment[E_SEGMENT['dir']] = self.body[prev_elem][E_SEGMENT['dir']]
                        segment[E_SEGMENT['last_x']] = segment[E_SEGMENT['x']]
                        # * print('raw dir changed', self.raw_dir)
            snake_obj = pygame.Rect(segment[E_SEGMENT['x']], segment[E_SEGMENT['y']], self.grid.cell_width, self.grid.cell_height)
            pygame.draw.rect(self.screen, 'blue', snake_obj)
            #snake_collider_box = pygame.Rect(snake_obj)

    def add_segment_to_body(self):
        last_i = len(self.body) - 1
        last_seg_dir = self.body[last_i][E_SEGMENT['dir']]
        new_segment = [last_seg_dir,0,0,0,0]
        self.body.append(new_segment)

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
            ['r', (self.INTIAL_POS_X-1) * self.grid.cell_width, (self.INTIAL_POS_Y) * self.grid.cell_height, self.INTIAL_POS_X * self.grid.cell_width, (self.INTIAL_POS_Y) * self.grid.cell_height],
            ['r', (self.INTIAL_POS_X-2) * self.grid.cell_width, (self.INTIAL_POS_Y) * self.grid.cell_height, (self.INTIAL_POS_X-1) * self.grid.cell_width, (self.INTIAL_POS_Y) * self.grid.cell_height]
            ]