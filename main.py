import pygame # for game features

import random # to place the fruit randomly

# pygame setup
pygame.init()
screen = pygame.display.set_mode((700, 700)) # define the screen size
clock = pygame.time.Clock()
is_running = True
delta_time = 0 # define delta time

snake_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

try:
    while is_running:
        # pygame.QUIT event means the user clicked X to close the window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False

        # visual objects
        screen.fill("purple")
        pygame.draw.circle(screen, "yellow", snake_pos, 15)

        # game mechanics
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            snake_pos.y -= 300 * delta_time
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            snake_pos.y += 300 * delta_time
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            snake_pos.x -= 300 * delta_time
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            snake_pos.x += 300 * delta_time

        snake_pos.x -= 300 * delta_time

        pygame.display.flip() # update the display
        fps = clock.tick(60) # limits FPS to 60
        delta_time = fps / 1000 # converts the time from milliseconds to seconds
except:
    print('Exception occured')
finally:
    pygame.quit()