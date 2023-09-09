# class to create and interact with the snake

import pygame

import math # to round up and down the raw directions for positioning

E_SEGMENT = {
    'dir': 0,
    'x': 1,
    'y': 2,
    'last_dir': 3,
    'last_x': 4,
    'last_y': 5
    
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
        if direction != self.dir:
            #self.body[0][E_SEGMENT['dir']] = direction
            self.body[0][E_SEGMENT['last_dir']] = direction
            self.body[0][E_SEGMENT['last_x']] = self.pos_x
            self.body[0][E_SEGMENT['last_y']] = self.pos_y
        self.dir = direction
        self.opposite_dir = E_DIR_TO_OPOSSITE_DIR[direction]

    def add_segment_to_body(self):
        last_i = len(self.body) - 1
        last_seg_dir = self.body[last_i][E_SEGMENT['dir']]
        last_seg_pos_x = self.body[last_i][E_SEGMENT['x']]
        last_seg_pos_y = self.body[last_i][E_SEGMENT['y']]
        last_seg_last_dir = self.body[last_i][E_SEGMENT['last_dir']]
        last_seg_last_pos_x = self.body[last_i][E_SEGMENT['last_x']]
        last_seg_last_pos_y = self.body[last_i][E_SEGMENT['last_y']]
        new_segment = [last_seg_dir, last_seg_pos_x, last_seg_pos_y, last_seg_last_dir, last_seg_last_pos_x, last_seg_last_pos_y]
        self.body.append(new_segment)

    def move(self):
        # update head pos
        if self.dir == 'u':
            self.pos_y -= 1
        if self.dir == 'd':
            self.pos_y += 1
        if self.dir == 'l':
            self.pos_x -= 1
        if self.dir == 'r':
            self.pos_x += 1

        # update body pos
        for i, segment in enumerate(self.body):
            if segment[E_SEGMENT['dir']] == 'u':
                segment[E_SEGMENT['y']] -= 1
            if segment[E_SEGMENT['dir']] == 'd':
                segment[E_SEGMENT['y']] += 1
            if segment[E_SEGMENT['dir']] == 'l':
                segment[E_SEGMENT['x']] -= 1
            if segment[E_SEGMENT['dir']] == 'r':
                segment[E_SEGMENT['x']] += 1

            if i == 0:
                segment[E_SEGMENT['dir']] = self.dir
            else:
                prev_elem = i - 1
                # TODO save the last direction changed with the postion to just change the direction there
                # TODO instead of always
                if (segment[E_SEGMENT['x']] == segment[E_SEGMENT['last_x']]) or (segment[E_SEGMENT['y']] == segment[E_SEGMENT['last_y']]):
                    segment[E_SEGMENT['dir']] = segment[E_SEGMENT['last_dir']]
                    segment[E_SEGMENT['last_dir']] = self.body[prev_elem][E_SEGMENT['last_dir']]
                    segment[E_SEGMENT['last_x']] = self.body[prev_elem][E_SEGMENT['last_x']]
                    segment[E_SEGMENT['last_y']] = self.body[prev_elem][E_SEGMENT['last_y']]


                    
            print(f'segment {i} dir {segment[E_SEGMENT["dir"]]}')
        #print('snake_pos_x', self.pos_x)
        #print('snake_pos_y', self.pos_y)

    def draw_head(self):
        transformed_pos_x = self.pos_x * self.grid.cell_width
        transformed_pos_y = self.pos_y * self.grid.cell_height
        snake_obj = pygame.Rect(transformed_pos_x, transformed_pos_y, self.grid.cell_width, self.grid.cell_height)
        pygame.draw.rect(self.screen, self.HEAD_COLOR, snake_obj)
        snake_collider_box = pygame.Rect(snake_obj)
        return snake_collider_box
    
    def draw_body(self):
        for segment in self.body:
            transformed_pos_x = segment[E_SEGMENT['x']] * self.grid.cell_width
            transformed_pos_y = segment[E_SEGMENT['y']] * self.grid.cell_height
            snake_obj = pygame.Rect(transformed_pos_x, transformed_pos_y, self.grid.cell_width, self.grid.cell_height)
            pygame.draw.rect(self.screen, self.BODY_COLOR, snake_obj)
            snake_collider_box = pygame.Rect(snake_obj)

    # reset all parameters
    def reset(self):
        self.pos_x = self.INTIAL_POS_X
        self.pos_y = self.INTIAL_POS_Y
        self.dir = self.INITIAL_DIR
        self.opposite_dir = 'l'
        self.body = [
            [self.INITIAL_DIR, (self.INTIAL_POS_X-1), self.INTIAL_POS_Y, self.INITIAL_DIR, self.INTIAL_POS_X, self.INTIAL_POS_Y],
            [self.INITIAL_DIR, (self.INTIAL_POS_X-2), self.INTIAL_POS_Y, self.INITIAL_DIR, self.INTIAL_POS_X-1, self.INTIAL_POS_Y]
            ]