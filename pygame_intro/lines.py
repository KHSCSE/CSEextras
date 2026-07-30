import pygame, sys, random
from pygame.locals import QUIT

# required stuff
w = 600
h = 600
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption('Hello World!')
screen.fill((255, 255, 255))

# use a loop to draw a bunch of lines  
for i in range(100):
    # TODO set a random position x1, y1, x2, y2
    x1 = random.randint(0,w)
    
    
    # TODO set a random color
    r = random.randint(0,255)
    
    
    
    # TODO draw a line
    
    
    
    # TODO challenge draw circles on the ends of your line
    
    
    
    pygame.display.flip() # pushes the screen to the current display
    pygame.time.delay(50) # slow it down a bit








# stay on screen
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()