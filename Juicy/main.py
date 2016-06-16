import pygame
from pygame.locals import *

import random
from vector2 import Vector2 as vec2

from player import player
from floor import floor
from building import building
from orangeBuilding import orange
import math

pygame.init()
pygame.font.init()

font1 = pygame.font.Font(None, 25)

screen_size = 800,600
w,h = screen_size

screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()

whole_surface = pygame.Surface((w+20,h+20))
whole_w,whole_h = w+20,h+20
draw_pos = vec2(-10,-10)

p1 = player((whole_w/2,whole_h-46))
floor_group = pygame.sprite.Group(floor((whole_w/2,whole_h-30)))

gravity = 350

time = 0
distance = 0

shakeTimer = 0.25;
maxShakeTimer = shakeTimer;

slamming = False

lose = False

building_list = []
orange_list = []
to_delete = []
count = 0
for i in range(150):
    building_list.append(building(random.randint(0,whole_w),(random.randint(1,7)),whole_h))

for i in range(150):
    orange_list.append(orange(random.randint(0,whole_w),(random.randint(1,7)),whole_h))

    
def elasticIn(k):
    a,p = 0.1,0.4
    if k==0: return 0
    if k==1: return 1
    if not a or a < 1:a=1;s=p/4
    else: s=p*math.asin(1/a)/(2*math.pi)
    
    return - ( a * math.pow(2, 10 * ( k - 1 ) ) * math.sin( ( k - s ) * ( 2 * math.pi ) / p) )


def elasticOut(k):
    a,p = 0.1,0.4
    if k==0: return 0
    if k==1: return 1
    if not a or a < 1:a=1;s=p/4
    else: s=p*math.asin(1/a)/(2*math.pi)
    return (a* math.pow(2, -10*k) * math.sin((k-s)*(2*math.pi) / p) + 1)


def elasticInOut(k):
    a,p = 0.1,0.4
    if k==0: return 0
    if k==1: return 1
    if not a or a < 1:a=1;s=p/4
    else: s=p*math.asin(1/a)/(2*math.pi)
    
    if k*2<1: return (-0.5 *(a*math.pow(2,10*(k-1))*math.sin((k-s)*(2*math.pi)/p)))
    
    return a* math.pow(2, -10* (k-1)) * math.sin((k-s) * (2*math.pi) /p ) * 0.5 + 1

def shake(k):
    try:
        if k==0:return vec2(-10,-10)
        if k==1:return vec2(random.randint(-20,0), random.randint(-20,0))
        else:return vec2(random.randint(-10-int(10*k),0-int(10*k)), random.randint(-10-int(10*k),0-int(10*k)))
    except ValueError:
        print k

done = False
while not done:
    time_passed = clock.tick(60)
    time_passed_seconds = time_passed/1000.0
    
    if not lose:
        time += time_passed_seconds
    
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
            
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[K_ESCAPE]:
        done = True
        
    if pressed_keys[K_w]:
        p1.jump()
            
    else:
        p1.falling = True
        
    if pressed_keys[K_r]:
        time=0
        distance=0
        p1.pos.y = whole_h-46
        p1.vel.x = 600
        floor_group = pygame.sprite.Group(floor((whole_w/2,whole_h-30)))
        lose = False        
        
    for i in range(count):
        building_list.append(building(whole_w,(random.randint(1,7)), whole_h))
        orange_list.append(orange(whole_w,(random.randint(1,7)), whole_h))
        
    count = 0
    
    building_list = sorted(building_list, key=lambda building: building.z+(building.pos.x/float(w*2)))
    building_list.reverse()
    
    #new_pointlist = sorted(point_list, key=lambda point: point.get_distance(currentPoint))
    sorted_sprites = sorted(floor_group.sprites(), key=lambda floor: floor.pos.x)
    if sorted_sprites[-1].width + sorted_sprites[-1].pos.x < whole_w:
        floor_group.add(floor((sorted_sprites[-1].pos.x+sorted_sprites[-1].width+random.randint(500,750), whole_h-30)))
        #print len(floor_group.sprites())
    
        
    
    p1.update(time_passed_seconds, 0, floor_group, gravity)
    if p1.pos.y > whole_h+16:
        lose = 1
        p1.vel.x,p1.vel.y = 0,0
        
    floor_group.update(p1.vel.x, time_passed_seconds)
    for FLOOR in floor_group.sprites():
        if FLOOR.width + FLOOR.pos.x < 0:
            floor_group.remove(FLOOR)
    
    distance+=int(p1.vel.x*time_passed_seconds)
    
    if p1.slammed or slamming:
        slamming = True
        #print p1.slammed, slamming
        draw_pos = shake(elasticIn(shakeTimer/maxShakeTimer))
        #print elasticIn(shakeTimer/maxShakeTimer)
        shakeTimer-=time_passed_seconds
        if shakeTimer<=0:
            #print "DONE"
            shakeTimer = maxShakeTimer
            draw_pos = (-10,-10)
            p1.slammed=False
            slamming = False
    
    screen.fill((255,0,0))
    
    whole_surface.fill((82,139,139))
    pygame.draw.rect(whole_surface, (120,120,120), (0,whole_h-7*31,whole_w,whole_h/2))
    pygame.draw.rect(whole_surface, (0,0,0), (0,whole_h-7*31,whole_w,whole_h/2), 1)
    for BUILDING in building_list:
        BUILDING.update(p1.vel.x, time_passed_seconds)
        if BUILDING.pos.x + BUILDING.width < 0:
            to_delete.append(BUILDING)
            continue
        BUILDING.render(whole_surface)

    for BUILDING in orange_list:
        BUILDING.update(p1.vel.x, time_passed_seconds)
        if BUILDING.pos.x + BUILDING.width < 0:
            to_delete.append(BUILDING)
            continue
        BUILDING.render(whole_surface)

    for BUILDING in to_delete:
        if BUILDING in building_list:
            building_list.remove(BUILDING)
        else:
            orange_list.remove(BUILDING)
            
        count+=1
        
    del to_delete[:]
    
    floor_group.draw(whole_surface)
    p1.render(whole_surface)
    
    time_render = font1.render(str(time), True, (0,0,0))
    distance_render = font1.render(str(distance), True, (0,0,0))
    
    whole_surface.blit(time_render, (20,20))
    whole_surface.blit(distance_render, (whole_w-distance_render.get_size()[0]-20, 20))
    
    if lose:
        lose_render = font1.render("GAME OVER. press R to retry", True, (0,0,0))
        lose_box = lose_render.get_rect()
        lose_box.center = (whole_w/2, whole_h/3)
        whole_surface.blit(lose_render, lose_box)
    
    #print draw_pos
    screen.blit(whole_surface, draw_pos)
    
    pygame.display.update()
    pygame.display.set_caption(str(clock.get_fps())+ ", " + str(count))
    
pygame.quit()