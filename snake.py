# class to create and interact with the snake

import pygame

E_SEGMENT = {
    'dir': 0,
    'x': 1,
    'y': 2,
    'new_dir': 3,
    'last_pos_x_dir_changed': 4,
    'last_pos_y_dir_changed': 5
    
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
            self.body[0][E_SEGMENT['new_dir']] = direction
            self.body[0][E_SEGMENT['last_pos_x_dir_changed']] = self.pos_x
            self.body[0][E_SEGMENT['last_pos_y_dir_changed']] = self.pos_y
        self.dir = direction
        self.opposite_dir = E_DIR_TO_OPOSSITE_DIR[direction]

    def add_segment_to_body(self):
        last_i = len(self.body) - 1
        last_seg_dir = self.body[last_i][E_SEGMENT['dir']]
        last_seg_pos_x = self.body[last_i][E_SEGMENT['x']]
        last_seg_pos_y = self.body[last_i][E_SEGMENT['y']]

        if self.is_debug_mode:
            pass
            #print(f'before Add segment with last_seg_pos_x {last_seg_pos_x} and last_seg_pos_y {last_seg_pos_y}')

        if last_seg_dir == 'u':
            last_seg_pos_y += 1
        if last_seg_dir == 'd':
            last_seg_pos_y -= 1
        if last_seg_dir == 'l':
            last_seg_pos_x += 1
        if last_seg_dir == 'r':
            last_seg_pos_x -= 1

        if self.is_debug_mode:
            pass
            #print(f'after Add segment with last_seg_pos_x {last_seg_pos_x} and last_seg_pos_y {last_seg_pos_y}')

        last_seg_last_dir = self.body[last_i][E_SEGMENT['new_dir']]
        last_seg_last_pos_x = self.body[last_i][E_SEGMENT['last_pos_x_dir_changed']]
        last_seg_last_pos_y = self.body[last_i][E_SEGMENT['last_pos_y_dir_changed']]
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
        
        if self.is_debug_mode:
            print(f'head pos is snake_pos_x {self.pos_x} and snake_pos_y {self.pos_y}')

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

            if segment[E_SEGMENT['dir']] != segment[E_SEGMENT['new_dir']]:
                if (segment[E_SEGMENT['x']] == segment[E_SEGMENT['last_pos_x_dir_changed']]) and (segment[E_SEGMENT['y']] == segment[E_SEGMENT['last_pos_y_dir_changed']]):
                    segment[E_SEGMENT['dir']] = segment[E_SEGMENT['new_dir']]
                    next_elem = i + 1
                    body_lenght = len(self.body) - 1
                    if next_elem <= body_lenght:
                        self.body[next_elem][E_SEGMENT['new_dir']] = segment[E_SEGMENT['new_dir']]
                        self.body[next_elem][E_SEGMENT['last_pos_x_dir_changed']] = segment[E_SEGMENT['last_pos_x_dir_changed']]
                        self.body[next_elem][E_SEGMENT['last_pos_y_dir_changed']] = segment[E_SEGMENT['last_pos_y_dir_changed']]

            if self.is_debug_mode:
                #print(f'segment {i} dir {segment[E_SEGMENT["dir"]]} pos_x {segment[E_SEGMENT["x"]]} and pos_y {segment[E_SEGMENT["y"]]}')
                pass

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