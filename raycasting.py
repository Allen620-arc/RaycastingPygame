import pygame
from settings import *
from map import world_map

def ray_casting(screen, player_position, player_angle):
    current_angle = player_angle - HALF_FOV
    x0, y0 = player_position
    for ray in range(NUM_RAYS):
        sin_angle = math.sin(current_angle)
        cos_angle = math.cos(current_angle)
        for depth in range(MAX_DEPTH):
            x = x0 + depth * cos_angle
            y = y0 + depth * sin_angle
            if (x // TILE * TILE, y // TILE * TILE) in world_map:
                depth *= math.cos(player_angle - current_angle)
                projection_height = PROJECTION_COEFFICIENT / depth
                c = 255 / (1 + depth * depth)
                color = (63 * c // 2, 63 * c // 2, 63 * c // 2)
                pygame.draw.rect(screen, color, (ray * SCALE, HALF_HEIGHT - projection_height // 2,
                                                 SCALE, projection_height))
                break
        current_angle += DELTA_ANGLE