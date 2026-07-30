import pygame
from ball import Ball

# setup
w = 600
h = 600
screen = pygame.display.set_mode([w, h])
screen.fill((255, 255, 255))


# initialize the ball, the blocks (list), and the player





# stay on screen
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEMOTION:
            mx, my = event.pos
    
    # fill the background with white (or don't!)
    screen.fill((255, 255, 255))
    
    # TODO draw and move here, also check for collision

    
    
    # pushes the screen to the current display
    pygame.display.flip()
    
    # delay a moment
    pygame.time.delay(10)


