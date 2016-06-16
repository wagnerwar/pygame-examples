import pygame
from vector2 import Vector2 as vec2

class player(pygame.sprite.Sprite):
    
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((32,32))
        self.rect = self.image.get_rect()
        self.pos = vec2(*pos)
        self.vel = vec2(600, 0)
        
        self.rect.center = self.pos
        self.grounded = False
        self.falling = True
        self.slammed = False
        
        self.image.fill((255,255,255))
        pygame.draw.rect(self.image, (0,0,0), (0,0,32,32), 1)
        
        
    def update(self, tp, mov, group, gravity):
        self.pos.y += self.vel.y*tp
        
        self.vel.x += tp*5
        #print self.vel.x
        self.vel.y += gravity * tp
        #print self.vel  
        
        self.rect.center = self.pos
        
        test = False
        for SPRITE in group.sprites():
            if pygame.sprite.collide_rect(self, SPRITE):
                
                self.pos.y = SPRITE.rect.topleft[1]-15
                self.vel.y = 0
                if not self.grounded:
                    self.slammed = True
                    self.image.fill((255,0,0))
                else:
                    self.image.fill((255,255,255))
                    self.slammed = False
                self.grounded = True
                self.falling = False
                test = True
                break
        if test == False:
            self.grounded = False
            
        
        
        self.rect.center = self.pos
        
    def jump(self):
        if self.grounded:
            self.vel.y -= 50
            self.grounded = False
        if not self.falling:
            self.vel.y -= 50
            if self.vel.y < -300:
                self.falling = True
            
        
    def render(self, surface):
        surface.blit(self.image, self.rect)