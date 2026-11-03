import pygame, sys, random
from pygame.locals import QUIT

# required stuff
w = 600
h = 600
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption('Hello World!')








# this time the action happens here
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

