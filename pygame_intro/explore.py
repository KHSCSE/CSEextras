import pygame, sys
from pygame.locals import QUIT

# required stuff
w = 600
h = 600
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption('Hello World!')
screen.fill((255, 255, 255))

# a line
# parameters are: surface, (red, green, blue), (startx, starty), (endx, endy)
pygame.draw.line(screen, (255,0,0), (50, 50), (300, 200))


# a box
# parameters are: surface, (red, green, blue), (topleft_x, topleft_y, width, height)
pygame.draw.rect(screen, (0,255,0), (200, 100, 100, 50))


# a circle
# parameters are: surface, (red, green, blue), (center_x, center_y), radius
pygame.draw.circle(screen, (0,0,255), (100, 200), 20)



pygame.display.update()
# stay on screen
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()