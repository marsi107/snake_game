import pygame # for game features

import sys
import random

from snake import Snake
from fruit import Apple

# pygame setup
pygame.init()
display_x = 700
display_y = 700
font_size = 36
font = pygame.font.Font(None, font_size) # set font to None  to use system default font
screen = pygame.display.set_mode((display_x, display_y)) # define the screen size
clock = pygame.time.Clock()
pygame.display.set_caption('Snake Game')
is_running = True
is_game_over = False
score = 0

# game objects setup
snake_initial_pos = pygame.Vector2(200, display_y / 2)
snk = Snake(snake_initial_pos)
apl = Apple(display_x, display_y)

def reset_game():
    snk.reset()
    apl.generate_new_apple_position()

def display_text_on_screen(txt, pos_x, pos_y):
    txt = font.render(txt, True, (255, 255, 255))
    txt_rect = txt.get_rect()
    txt_rect.center = (pos_x, pos_y)
    screen.blit(txt, txt_rect)

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
        if snk.snake_pos.x > display_x - snk.SNAKE_SIZE:
            is_game_over = True
            snk.change_snake_direction('esc')
        if snk.snake_pos.y < snk.SNAKE_SIZE:
            is_game_over = True
            snk.change_snake_direction('esc')
        if snk.snake_pos.y > display_y - snk.SNAKE_SIZE:
            is_game_over = True
            snk.change_snake_direction('esc')

        # behavior when is game over
        if is_game_over:
            display_text_on_screen('Game Over.', display_x / 2, (display_y / 2) - font_size)
            display_text_on_screen(('Your score is ' + str(score)), display_x / 2, display_y / 2)
            display_text_on_screen('Press space to play again...', display_x / 2, (display_y / 2) + font_size)


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