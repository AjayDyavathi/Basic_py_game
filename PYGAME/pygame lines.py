import pygame, sys
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((1000,500),0,32)

points = []
color = (125,125,125)

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == MOUSEBUTTONDOWN:
            points.append(event.pos)

    if len(points)>1:
        pygame.draw.lines(screen, color, False, points, 7)

    pygame.display.update()
