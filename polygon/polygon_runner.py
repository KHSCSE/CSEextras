import pygame, sys, random
from pygame.locals import QUIT

# required stuff
w = 600
h = 600
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption('Hello World!')

# TODO initial values for points (that form a triangle or other polygon)
# TODO initial values for color, and velocity



# this time the action happens here
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # fill the background with white (erase previous frame)
    screen.fill((255, 255, 255))
    
    
    # TODO draw the polygon
    
    
    
    
    # TODO find the center of the polygon
    # (find average x value, average y value)
    
    
    # TODO if hit edge, bounce
    # if hit left or right, flip xVelocity

    
    # if hit top or bottom, flip yVelocity
    


    
    # move (add the 'velocity' to the current points)


    
    
    
    
    pygame.display.flip() # pushes the screen to the current display
    pygame.time.delay(5) # slow it down a bit


print("the game has ended")