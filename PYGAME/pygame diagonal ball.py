bif = "bgimg.jpg"
mif = "move.png"

import pygame, sys
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((1000, 400), 0, 32)

background = pygame.image.load(bif).convert()
ball = pygame.image.load(mif).convert_alpha()

speedx = 250
speedy = 300
clock = pygame.time.Clock()

x=0
y=0

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


    screen.blit(background, (0,0))
    screen.blit(ball, (x,y))

    milli = clock.tick()
    seconds = milli/1000.
    dmx = seconds*speedx
    dmy = seconds*speedy
    x+=dmx
    y+=dmy

    if x>900:
       x=0

    if y>300:
        y=0



    pygame.display.update()
