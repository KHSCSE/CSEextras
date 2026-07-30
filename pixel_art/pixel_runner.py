
# we will
# 1) complete the function to draw an object
# 2) create an object, draw it
# 3) add mouse interactivity (when mouse.click, add new object to list)


# for more pixel art ideas
# https://pixelartmaker.com/offshoot/6fdfe6df7a38dfa


# convert HEX to RGB
# https://www.rapidtables.com/convert/color/hex-to-rgb.html




import pygame, random
from my_pixel_art import My_Pixel_Art as MPA
# from filename import Classname as alias

# setup
w = 800
h = 600
screen = pygame.display.set_mode([w, h])
screen.fill((255, 255, 255))

# TODO create a 'My_Pixel_Art' object


# TODO create a list of 'My_Pixel_Art' objects
art = []


# stay on screen
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y = event.pos
            # TODO create an object, append to list
    
    # TODO draw the first object
    
    
    
    # fill the background with white (or don't!)
    # screen.fill((255, 255, 255))
    
    # TODO loop through list, draw
    
    
    
    # pushes the screen to the current display
    pygame.display.flip()
    
    # delay a moment
    pygame.time.delay(3)


