import pygame
from pygame.locals import *
import random
from vector2 import Vector2 as vec2

pygame.init()
screen_size = (640,480)
w,h = screen_size
screen = pygame.display.set_mode(screen_size)

surf_w, surf_h = (w+20, h+20)
surf_pos = vec2(-10,-10)

def fixCol(col):
    return max(0, min(255, col))

def newRandCol(col):
    random_color_r = fixCol(col[0]+random.randint(0,10))
    random_color_g = fixCol(col[1]+random.randint(0,10))
    random_color_b = fixCol(col[2]+random.randint(0,10))
    return (random_color_r, random_color_g, random_color_b)

surf = pygame.Surface((surf_w, surf_h))
col = (39,134,39)
for i in range(surf_w%32+1):
    for j in range(surf_h%32+1):
        random_color = newRandCol(col)
        pygame.draw.rect(surf, random_color, (i*32,j*32,32,32))

done = False
while not done:
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True

    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[K_ESCAPE]:
        done = True
    if pressed_keys[K_w]:
        surf_pos.x = random.randint(-10,0)
        surf_pos.y = random.randint(-10,0)
    else:
        surf_pos.x = -10
        surf_pos.y = -10

    screen.fill((0,0,0))
    screen.blit(surf, surf_pos)
    pygame.display.flip()

pygame.quit();
