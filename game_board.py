# class to create and interact with the snake
import pygame

DISPLAY_X = 700
DISPLAY_Y = 700

# helper class to add main functionalities
class Controller:
    FONT_SIZE = 42
    screen = None
    font = None

    def __init__(self, screen) -> None:
        self.screen = screen
        self.font = pygame.font.Font(None, self.FONT_SIZE) # set font to None  to use system default font

    def display_text_on_screen(self, text, pos_x, pos_y):
        txt = self.font.render(text, True, (255, 255, 255))
        txt_rect = txt.get_rect()
        txt_rect.center = (pos_x, pos_y)
        self.screen.blit(txt, txt_rect)

    # behavior when teh game is over
    def game_over_display(self, is_game_over, score):
        if is_game_over:
            self.display_text_on_screen('Game Over.', DISPLAY_X / 2, (DISPLAY_Y / 2) - self.FONT_SIZE)
            self.display_text_on_screen(('Your score is ' + str(score)), DISPLAY_X / 2, DISPLAY_Y / 2)
            self.display_text_on_screen('Press space to play again...', DISPLAY_X / 2, (DISPLAY_Y / 2) + self.FONT_SIZE)

# define the grid where the game elements will be
class Grid:
    NUM_COLS = 35
    NUM_ROWS = 35
    screen = None
    cell_width = 0
    cell_height = 0

    def __init__(self, screen) -> None:
        self.screen = screen
        # Calculate the size of each grid cell
        self.cell_width = DISPLAY_X // self.NUM_COLS
        self.cell_height = DISPLAY_Y // self.NUM_ROWS

    def draw_grid(self):
        for row in range(self.NUM_ROWS):
            for column in range(self.NUM_COLS):
                cell_x = column * self.cell_width
                cell_y = row * self.cell_height
                pygame.draw.rect(self.screen, 'white', pygame.Rect(cell_x, cell_y, self.cell_width, self.cell_height), 1)
