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
pygame.display.set_caption('Snake Game')
is_running = True
is_game_over = False
score = 0

# game objects setup
game_ctrl = gb.Controller(screen)
grid = gb.Grid()
snake_initial_pos = pygame.Vector2(200, gb.DISPLAY_Y / 2)
snk = Snake(snake_initial_pos)
apl = Apple(gb.DISPLAY_X, gb.DISPLAY_Y)

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
        # create the snake
        snake_obj = pygame.draw.circle(screen, snk.SNAKE_COLOR, snk.snake_pos, snk.SNAKE_SIZE)
        snake_collider_box = pygame.Rect(snake_obj)
        # create the apple
        apl_obj = pygame.draw.circle(screen, apl.APPLE_COLOR, apl.apple_pos, apl.APPLE_SIZE)
        apple_collider_box = pygame.Rect(apl_obj)

        # set collisions
        if snake_collider_box.colliderect(apple_collider_box):
            apl.generate_new_apple_position()
            score += 1

        # Check for collisions with the borders
        if snk.snake_pos.x < snk.SNAKE_SIZE:
            is_game_over = True
            snk.change_snake_direction('esc')
        if snk.snake_pos.x > gb.DISPLAY_X - snk.SNAKE_SIZE:
            is_game_over = True
            snk.change_snake_direction('esc')
        if snk.snake_pos.y < snk.SNAKE_SIZE:
            is_game_over = True
            snk.change_snake_direction('esc')
        if snk.snake_pos.y > gb.DISPLAY_Y - snk.SNAKE_SIZE:
            is_game_over = True
            snk.change_snake_direction('esc')

        # behavior when is game over
        game_ctrl.game_over_display(is_game_over, str(score))

        # keyboard reading
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            snk.change_snake_direction('u')
        elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
            snk.change_snake_direction('d')
        elif keys[pygame.K_a] or keys[pygame.K_LEFT]:
            snk.change_snake_direction('l')
        elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            snk.change_snake_direction('r')
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

        # set snake speed constant based on the direction given above
        snk.snake_pos.x += snk.snake_speed_x
        snk.snake_pos.y += snk.snake_speed_y

        # display settings
        pygame.display.flip() # update the display
        clock.tick(60) # limits FPS to 60
except Exception as ex:
    print('Exception occured,', ex)
finally:
    pygame.quit()
    sys.exit()