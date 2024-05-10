import pygame
from settings import *
from raycasting import ray_casting

class Drawing:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont('Arial', 36, bold=True)

    def background(self):
        pygame.draw.rect(self.screen, SBLUE, (0, 0, WIDTH, HALF_HEIGHT))
        pygame.draw.rect(self.screen, MGREEN, (0, HALF_HEIGHT, WIDTH, HALF_HEIGHT))

    def world(self, player_position, player_angle):
        ray_casting(self.screen, player_position, player_angle)

    def fps(self, clock):
        display_fps = str(int(clock.get_fps()))
        render = self.font.render(display_fps, 0, CRED)
        self.screen.blit(render, FPS_POS)