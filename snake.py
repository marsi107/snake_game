# class to create and interact with the snake

import pygame

E_SEGMENT = {
    'x': 0,
    'y': 1,
    'x_to_pass': 2,
    'y_to_pass': 3
    
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
    is_debug_mode = False
    pos_x, pos_y = 0, 0
    dir = INITIAL_DIR
    opposite_dir = 'l'
    is_moving = True
    body = None

    def __init__(self, screen, grid, is_debug_mode = False):
        self.screen = screen
        self.grid = grid
        self.is_debug_mode = is_debug_mode
        self.reset()

    def change_direction(self, direction):
        # guardian to control that the snake doesn't go backwards
        if direction == self.opposite_dir:
            return
        if direction != self.dir:
            if self.is_debug_mode:
                print(f'changed direction from {self.dir} to {direction}')
            self.dir = direction
            self.opposite_dir = E_DIR_TO_OPOSSITE_DIR[direction]

    def add_segment_to_body(self):
        last_i = len(self.body) - 1
        last_seg_pos_x = self.body[last_i][E_SEGMENT['x_to_pass']]
        last_seg_pos_y = self.body[last_i][E_SEGMENT['y_to_pass']]
        new_segment = [last_seg_pos_x, last_seg_pos_y, 0, 0]
        self.body.append(new_segment)

    def move(self):
        if not self.is_moving:
            return
        # update body pos
        for i, segment in enumerate(self.body):
            segment[E_SEGMENT['x_to_pass']] = segment[E_SEGMENT['x']]
            segment[E_SEGMENT['y_to_pass']] = segment[E_SEGMENT['y']]
            prev_elem = i - 1
            if i == 0:
                segment[E_SEGMENT['x']] = self.pos_x
                segment[E_SEGMENT['y']] = self.pos_y
            else:
                segment[E_SEGMENT['x']] = self.body[prev_elem][E_SEGMENT['x_to_pass']]
                segment[E_SEGMENT['y']] = self.body[prev_elem][E_SEGMENT['y_to_pass']]

        # update head pos
        if self.dir == 'u':
            self.pos_y -= 1
        if self.dir == 'd':
            self.pos_y += 1
        if self.dir == 'l':
            self.pos_x -= 1
        if self.dir == 'r':
            self.pos_x += 1

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
        self.opposite_dir = E_DIR_TO_OPOSSITE_DIR[self.INITIAL_DIR]
        self.is_moving = True
        self.body = [
            [(self.INTIAL_POS_X-1), self.INTIAL_POS_Y, 0, 0],
            [(self.INTIAL_POS_X-2), self.INTIAL_POS_Y, 0, 0]
            ]