import pygame, random, math

# setup
w = 800
h = 600
screen = pygame.display.set_mode([w, h])
screen.fill((255, 255, 255))

# TODO variables for paddle



# TODO variables for ball



# TODO variables for mouse



# stay on screen
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # TODO get mouse position

    
    # erase previous frame
    screen.fill((255, 255, 255))
    
    
        
    # TODO draw paddle and ball

  

    # TODO move paddle
   
   
    
    
    
    
    # TODO check ball hits wall

    
    
    # TODO check ball hits paddle



    # TODO move ball  



    
    # pushes the screen to the current display
    pygame.display.flip()
    
    # delay a moment
    pygame.time.delay(10)


