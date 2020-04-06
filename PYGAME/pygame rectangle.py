import pygame, sys
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((1000, 400), 0, 32)

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.lock()

    pygame.draw.rect(screen, (122,213,56), Rect((100,100),(700,150)))
        
    screen.unlock()

    pygame.display.update()
