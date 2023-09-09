import pygame

import unittest

import game_board as gb
from snake import Snake

class SnakeTests(unittest.TestCase):
    def test_fast_dir_change(self):
        # set the environment
        screen = pygame.display.set_mode((gb.DISPLAY_X, gb.DISPLAY_Y))
        grid = gb.Grid(screen)
        snk = Snake(screen, grid)
        # check that the snake is moving as expected at the beginning
        self.assertTrue(snk.is_moving)
        self.assertEqual('r', snk.dir)
        # draw snake    
        snake_head_collider_box = snk.draw_head()
        snake_body_collider_box_list = snk.draw_body()
        # check collision head to body
        for segment_collider in snake_body_collider_box_list:
            if snake_head_collider_box.colliderect(segment_collider):
                snk.is_moving = False
        #change directions fast
        snk.change_direction('u')
        # draw snake    
        snake_head_collider_box = snk.draw_head()
        snake_body_collider_box_list = snk.draw_body()
        # check collision head to body
        for segment_collider in snake_body_collider_box_list:
            if snake_head_collider_box.colliderect(segment_collider):
                snk.is_moving = False
        snk.change_direction('l')
        snk.move()
        # draw snake    
        snake_head_collider_box = snk.draw_head()
        snake_body_collider_box_list = snk.draw_body()
        # check collision head to body
        for segment_collider in snake_body_collider_box_list:
            if snake_head_collider_box.colliderect(segment_collider):
                snk.is_moving = False
        # check that the snake is still moving as expected
        self.assertTrue(snk.is_moving)