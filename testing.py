import pygame ,os ,sys
from pygame.locals import *

pygame.init()
fps_clock = pygame.time.Clock()
surface = pygame.display.set_mode((800,600))
background = pygame.Color(100,149,237)

while True:
    surface.fill(background)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    print(fps_clock.tick())
    fps_clock.tick(30)