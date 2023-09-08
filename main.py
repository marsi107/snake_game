import pygame # for game features

import sys
import random

import game_board as gb
from snake import Snake
from fruit import Apple

# pygame setup
pygame.init()
screen = pygame.display.set_mode((gb.DISPLAY_X, gb.DISPLAY_Y)) # define the screen size
clock = pygame.time.Clock()
pygame.display.set_caption('snake_game')
is_running = True
is_game_over = False
score = 0
counter = 0

# game objects setup
game_ctrl = gb.Controller(screen)
grid = gb.Grid(screen)
snk = Snake(screen, grid)
apl = Apple(grid)

def reset_game():
    snk.reset()
    apl.generate_new_apple_position()

try:
    while is_running:
        # pygame.QUIT event means the user clicked X to close the window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False

        # visual objects
        screen.fill('grey')
        grid.draw_grid()
        ## create the snake
        #snake_obj = pygame.Rect(snk.pos_x, snk.pos_y, grid.cell_width, grid.cell_height)
        #pygame.draw.rect(screen, snk.COLOR, snake_obj)
        #snake_collider_box = pygame.Rect(snake_obj)
        # create the apple
        apl_obj = pygame.Rect(apl.pos_x, apl.pos_y, grid.cell_width, grid.cell_height)
        pygame.draw.rect(screen, apl.COLOR, apl_obj)
        apple_collider_box = pygame.Rect(apl_obj)

        # set render time
        counter += 1
        if counter == 10:
            snk.move()
            counter = 0

        # draw snake    
        snake_head_collider_box = pygame.Rect(snk.draw_head())

        # set collisions
        if snake_head_collider_box.colliderect(apple_collider_box):
            apl.generate_new_apple_position()
            snk.add_segment_to_body()
            score += 1

        # Check for collisions with the borders
        if snk.pos_x < 0:
            is_game_over = True
            snk.change_direction('esc')
        if snk.pos_x > gb.DISPLAY_X - grid.cell_height:
            is_game_over = True
            snk.change_direction('esc')
        if snk.pos_y < 0:
            is_game_over = True
            snk.change_direction('esc')
        if snk.pos_y > gb.DISPLAY_Y - grid.cell_width:
            is_game_over = True
            snk.change_direction('esc')

        # behavior when is game over
        game_ctrl.game_over_display(is_game_over, str(score))

        # keyboard reading
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            snk.change_direction('u')
        elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
            snk.change_direction('d')
        elif keys[pygame.K_a] or keys[pygame.K_LEFT]:
            snk.change_direction('l')
        elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            snk.change_direction('r')
        elif keys[pygame.K_SPACE]:
            if is_game_over:
                is_game_over = False
                score = 0
                reset_game()
            else:
                # TODO add resume functions
                pass
        elif keys[pygame.K_ESCAPE]:
            #snk.change_snake_direction('esc')
            # TODO add pause functions
            pass

        # display settings
        pygame.display.flip() # update the display
        clock.tick(60) # limits FPS to 60
except Exception as ex:
    print('Exception occured,', ex)
finally:
    pygame.quit()
    sys.exit()