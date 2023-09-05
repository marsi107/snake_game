# class to create and interact with the snake
class Snake:
    snake_size = 15
    snake_pos = 0
    snake_speed_x, snake_speed_y = 2, 0
    opposite_snake_direction = 'l'

    def __init__(self, snake_position, snake_size = 15):
        self.snake_pos = snake_position
        self.snake_size = snake_size

    def change_snake_direction(self, direction):
        # guardian to control that the snake doesn't go backwards
        if direction == self.opposite_snake_direction:
            return
        if direction == 'u':
            self.snake_speed_x = 0
            self.snake_speed_y = -2
            self.opposite_snake_direction = 'd'
        elif direction == 'd':
            self.snake_speed_x = 0
            self.snake_speed_y = 2
            self.opposite_snake_direction = 'u'
        elif direction == 'l':
            self.snake_speed_x = -2
            self.snake_speed_y = 0
            self.opposite_snake_direction = 'r'
        elif direction == 'r':
            self.snake_speed_x = 2
            self.snake_speed_y = 0
            self.opposite_snake_direction = 'l'