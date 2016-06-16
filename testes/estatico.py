import pygame

background_colour = (255,255,255)

(width, height) = (300, 200)

screen = pygame.display.set_mode((width, height))

pygame.display.set_caption('Tutorial 2')

pos = [150, 50]
v = (2,2)

screen.fill(background_colour)
pygame.display.flip()
# Game loop
while 1:
    screen.fill(background_colour)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN: 
            print('Houve clique')
            if(event.key == 273):
                print('CIMA')
                pos[1] -= v[1]
                #pos[0] -= v[0]
                pygame.draw.circle(screen, (0, 0, 255), pos,20, 0)
                print(pos)
                pygame.display.flip()
                
                