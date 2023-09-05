import pygame # for game features
import random # to place the fruit randomly

# pygame setup
pygame.init()
# define the screen size
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
is_running = True

try:
    while is_running:
        # pygame.QUIT event means the user clicked X to close the window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False

        screen.fill("purple")
        pygame.display.flip() # update the display
        clock.tick(60) # limits FPS to 60
except:
    print('Exception occured')
finally:
    pygame.quit()