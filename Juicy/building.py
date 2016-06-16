import pygame
from pygame.locals import *

from random import randint

from vector2 import Vector2 as vec2
pygame.init()
class building:
    
    def __init__(self,x,z,h):
        self.z = z
        self.color = (z+2)*10
        self.width,self.height = (10-z)*5,randint((10-z)*15,(10-z)*25)
        self.pos = vec2(x,h-z*30)
        self.rect = pygame.Rect(0,0,self.width, self.height)
        self.rect.bottomleft = self.pos
        
    def render(self, surface):
        pygame.draw.rect(surface, (self.color,self.color,self.color), self.rect)
        pygame.draw.rect(surface, (0,0,0), self.rect, 1)
        
    def update(self, mov, tp):
        self.pos.x -= (10-self.z)*(mov/50.0)*tp
        self.rect.bottomleft = self.pos