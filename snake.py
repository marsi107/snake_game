# class to create and interact with the snake
class Snake:
    COLOR = 'yellow'
    INTIAL_POS_X = 7
    INTIAL_POS_Y = 17
    SPEED = 1
    INTIAL_DIR_X = 2
    INTIAL_DIR_Y = 0
    grid = None
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
            self.dir_x = 0
            self.dir_y = -2
            self.opposite_snake_direction = 'd'
        elif direction == 'd':
            self.dir_x = 0
            self.dir_y = 2
            self.opposite_snake_direction = 'u'
        elif direction == 'l':
            self.dir_x = -2
            self.dir_y = 0
            self.opposite_snake_direction = 'r'
        elif direction == 'r':
            self.dir_x = 2
            self.dir_y = 0
            self.opposite_snake_direction = 'l'
        elif direction == 'esc':
            self.dir_x = 0
            self.dir_y = 0

    # set snake speed constant based on the direction given above
    def move(self):
        self.pos_x += self.dir_x * self.SPEED
        self.pos_y += self.dir_y * self.SPEED

    def reset(self):
        self.pos_x = self.INTIAL_POS_X * self.grid.cell_width
        self.pos_y = self.INTIAL_POS_Y * self.grid.cell_height
        self.dir_x = self.INTIAL_DIR_X
        self.dir_y = self.INTIAL_DIR_Y
        self.opposite_snake_direction = 'l'