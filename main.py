import pygame
import sys
from settings import *
pygame.init()

class Player:
    def __init__(self):
        self.x, self.y = player_position
        self.angle = player_angle

    @property
    def move(self):
        return self.x, self.y

    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.y -= player_speed
        if keys[pygame.K_s]:
            self.y += player_speed
        if keys[pygame.K_a]:
            self.x -= player_speed
        if keys[pygame.K_d]:
            self.x += player_speed
        if keys[pygame.K_LEFT]:
            self.angle -= 0.02
        if keys[pygame.K_RIGHT]:
            self.angle += 0.02

        # Update player_position globally
        global player_position
        player_position = [self.x, self.y]

pygame.display.set_caption('Raycasting')
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
player = Player()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    player.movement()
    screen.fill(BLACK)

    pygame.draw.circle(screen, MGREEN, player_position, 12)

    pygame.display.flip()
    clock.tick(FPS)
