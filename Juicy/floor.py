import pygame
from vector2 import Vector2 as vec2
import random 

class floor(pygame.sprite.Sprite):
    
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.width = 500 + random.randint(0, 250) + random.randint(0,250)
        
        self.image = pygame.Surface((self.width, 20))
        self.image.fill((255,255,255))
        
        self.rect = self.image.get_rect()
        pygame.draw.rect(self.image, (0,0,0), self.rect, 1)
        
        self.pos = vec2(*pos)
        
        self.rect.topleft = self.pos
        
    def update(self, mov, tp):
        self.pos.x -= mov*tp
        self.rect.topleft = self.pos
        
    #rendering will be done by sprite group (.draw())