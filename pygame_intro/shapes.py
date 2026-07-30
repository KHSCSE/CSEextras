import pygame, sys, random
from pygame.locals import QUIT

# required stuff
w = 600
h = 600
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption('Hello World!')

# TODO initial values for position, size, and velocity
x1 = 100
y1 = 100
size1 = 20
x1vel = random.randint(-3,3)
y1vel = random.randint(-3,3)


# TODO variables for the second bouncy shape




# this time the action happens here
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # fill the background with white (erase previous frame)
    screen.fill((255, 255, 255))
    
    
    # shape 1: draw, bounce, move
    pygame.draw.circle(screen, (255,0,0), (x1, y1), size1)
    # TODO if hit edge, bounce
    # if hit left or right, flip xVelocity
    
    # if hit top or bottom, flip yVelocity
    


    
    # move (add the 'velocity' to the current position)

    
    
    
    
    # TODO second shape: draw, bounce, move
    
    
    
    
    pygame.display.flip() # pushes the screen to the current display
    pygame.time.delay(5) # slow it down a bit


print("the game has ended")