import pygame
pygame.init()
WIDTH=600
HEIGHT=600
TITLE="rocket in space"
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption(TITLE)

rocket=pygame.image.load("rocket.png")
space=pygame.image.load("space+stars.png")

run=True
while run:

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False

    pygame.display.update()
