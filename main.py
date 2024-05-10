import pygame
import sys
from settings import *
import math
from drawing import Drawing

pygame.init()

class Player:
    def __init__(self):
        self.x, self.y = player_position
        self.angle = player_angle

    @property
    def move(self):
        return self.x, self.y

    def movement(self):
        sin_angle = math.sin(self.angle)
        cos_angle = math.cos(self.angle)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.x += player_speed * cos_angle
            self.y += player_speed * sin_angle
            print('W')
        if keys[pygame.K_s]:
            self.x += -player_speed * cos_angle
            self.y += -player_speed * sin_angle
            print('S')
        if keys[pygame.K_a]:
            self.x += player_speed * cos_angle
            self.y += -player_speed * sin_angle
            print('A')
        if keys[pygame.K_d]:
            self.x += -player_speed * cos_angle
            self.y += player_speed * sin_angle
            print('D')
        if keys[pygame.K_LEFT]:
            self.angle -= 0.02
        if keys[pygame.K_RIGHT]:
            self.angle += 0.02

        # Update player_position globally
        global player_position, player_angle
        player_position = [self.x, self.y]
        player_angle = self.angle

pygame.display.set_caption('Raycasting')
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
player = Player()
drawing = Drawing(screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    player.movement()
    screen.fill(BLACK)

    drawing.background()
    drawing.world(player_position, player_angle)
    drawing.fps(clock)

    pygame.display.flip()
    clock.tick(FPS)
