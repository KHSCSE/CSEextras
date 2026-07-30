import pygame, sys, random
from pygame.locals import QUIT

# required stuff
w = 600
h = 600
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption('Hello World!')

# TODO initial values for shape1
# position, size, and velocity
# this shape will move with the mouse



# TODO variables for shape2
# this shape will move with the arrow keys




# YOUR TURN
# the options (do as many as you can)
# shape 2 should *not* be allowed to move off screen 
#      hint: think about the conditional statements we used to 'bounce'
# shape 3 is a 'bouncy' shape
# shape 4 freestyle something cool








# this time the action happens here
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        # TODO shape 1 moves with the mouse

    # fill the background with white (erase previous frame)
    screen.fill((255, 255, 255))
    
    
    # TODO another option for moving shape 1
    
    # TODO draw shape 1

    
    
    
    # TODO shape 2: move with keyboard, draw






    
    pygame.display.flip() # pushes the screen to the current display
    pygame.time.delay(5) # slow it down a bit


print("the game has ended")