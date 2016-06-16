import pygame
from pygame.locals import *

from random import randint

from vector2 import Vector2 as vec2
from building import building
pygame.init()
        
screen_size = (800,600)
w,h = screen_size

screen = pygame.display.set_mode(screen_size)

building_list = []
for i in range(100):
    building_list.append(building(randint(0,w),(randint(0,8)),h-100))

clock = pygame.time.Clock()

to_delete = []
count = 0
done = False
while not done:
    time_passed = clock.tick()
    time_passed_seconds = time_passed/1000.0
    
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
    
    for i in range(count):
        building_list.append(building(w,(randint(0,8)), h-100))
    count = 0
    
    #new_pointlist = sorted(point_list, key=lambda point: point.get_distance(currentPoint))
    building_list = sorted(building_list, key=lambda building: building.z+(building.pos.x/float(w*2)))
    building_list.reverse()
    
    screen.fill((255,0,0))
    for BUILDING in building_list:
        BUILDING.update(1024, time_passed_seconds)
        if BUILDING.pos.x + BUILDING.width < 0:
            to_delete.append(BUILDING)
            continue
        BUILDING.render(screen)
        
    for BUILDING in to_delete:
        building_list.remove(BUILDING)
        count+=1
        
    del to_delete[:]
        
    pygame.display.update()
    pygame.display.set_caption(str(clock.get_fps())+ ", " + str(count))
    
pygame.image.save(screen, "buildingTest.png")

pygame.quit()