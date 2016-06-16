import pygame
from pygame.locals import *

from random import randint

from vector2 import Vector2 as vec2
from building import building

pygame.init()
class orange(building):
    
    def __init__(self, x, z, h):
        building.__init__(self,x,z,h)
        self.color = (255,140,0)
    def render(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        pygame.draw.rect(surface, (0,0,0), self.rect, 1)
    
        
    #def render(self, surface):
    #    building.render(self, surface)
        
    #def update(self, mov, tp):
    #    building.render(self, mov, tp)