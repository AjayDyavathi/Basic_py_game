import pygame, sys
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((1000, 400), 0, 32)

points =[(20,120),(140,140),(110,30)]
color = (255,120,120)
color2 = (125,125,125)
position = (500, 200)
radius = 100
rectangle = (700,150,200,100)
pos1 = (20,20)
pos2 = (600,250)


while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.lock()

    pygame.draw.polygon(screen, color, points)
    pygame.draw.circle(screen, color2, position, radius)
    pygame.draw.ellipse(screen, color, rectangle)
    pygame.draw.line(screen, color, pos1, pos2, 10)
        
    screen.unlock()

    pygame.display.update()
