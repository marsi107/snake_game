import pygame # for game features

import random # to place the fruit randomly

from snake import Snake

# pygame setup
pygame.init()
display_x = 700
display_y = 700
screen = pygame.display.set_mode((display_x, display_y)) # define the screen size
clock = pygame.time.Clock()
is_running = True
delta_time = 0 # define delta time

snake_initial_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
pygame.display.set_caption("Snake Game")
snk = Snake(snake_initial_pos)


try:
    while is_running:
        # pygame.QUIT event means the user clicked X to close the window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False

        # visual objects
        screen.fill("grey")
        pygame.draw.circle(screen, "yellow", snk.snake_pos, snk.snake_size)

        # game mechanics
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            snk.change_snake_direction('u')
        elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
            snk.change_snake_direction('d')
        elif keys[pygame.K_a] or keys[pygame.K_LEFT]:
            snk.change_snake_direction('l')
        elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            snk.change_snake_direction('r')

        # If snake reaches the end, enter from the other side
        if snk.snake_pos.x + snk.snake_speed_x > display_x:
            snk.snake_pos.x = 0
        elif snk.snake_pos.x + snk.snake_speed_x < 0:
            snk.snake_pos.x = 700
        else:
            snk.snake_pos.x += snk.snake_speed_x

        if snk.snake_pos.y + snk.snake_speed_y > display_y:
            snk.snake_pos.y = 0
        elif snk.snake_pos.y + snk.snake_speed_y < 0:
            snk.snake_pos.y = 700
        else:
            snk.snake_pos.y += snk.snake_speed_y

        pygame.display.flip()  # update the display
        clock.tick(60)  # limits FPS to 60
except:
    raise Exception('Exception occurred')
finally:
    pygame.quit()
