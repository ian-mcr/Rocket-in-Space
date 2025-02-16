import pygame
pygame.init()
WIDTH=600
HEIGHT=600
TITLE="rocket in space"
y=250
x=250
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption(TITLE)

rocket=pygame.image.load("rocket.png")
space=pygame.image.load("space+stars.png")

run=True
while run:
    screen.blit(space,(0,0))
    screen.blit(rocket,(x,y))

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False

        # this is when you don't want to hold the keys    
        """
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_w:
                y=y-20
        
            if event.key==pygame.K_a:
                x=x-20

            if event.key==pygame.K_s:
                y=y+20
            
            if event.key==pygame.K_d:
                x=x+20"""
    # this is when you want to hold the keys       
    keyspressd=pygame.key.get_pressed()
    if keyspressd[pygame.K_w]:
        y=y-2
    if keyspressd[pygame.K_a]:
        x=x-2
    if keyspressd[pygame.K_s]:
        y=y+2
    if keyspressd[pygame.K_d]:
        x=x+2
    
    if x<0:
        x=0
    if y<0:
        y=0
    if x>550:
        x=550
    if y>550:
        y=550

    pygame.display.update()
