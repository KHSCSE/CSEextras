import pygame, random
from enemy import Enemy

# setup
w = 600
h = 600
screen = pygame.display.set_mode([w, h])
screen.fill((255, 255, 255))

# TODO create list of enemies using randomization here
# enemies = []
# for i in range(10):
#     x = random.randint(0, w)
#     y = random.randint(0, h)
#     size = random.randint(5, 20)
#     xv = random.randint(-6, 6)
#     yv = random.randint(-6,6)
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     col = (r,g,b)
#     temp = Enemy(x, y, size, xv, yv, col)
#     enemies.append(temp)
    
    



# what if we want to have the *same* enemies every time we play?
# TODO create list of enemies using text file
# text file data is:
# x, y, size, xv, yv, red, green, blue
enemies = []
f = open("enemy_data.txt", "r")
for line in f:
    line = line.strip()
    temp = line.split(",")
    # print(temp)
    x = int(temp[0])
    y = int(temp[1])
    size = int(temp[2])
    xv = int(temp[3])
    yv = int(temp[4])
    r = int(temp[5])
    g = int(temp[6])
    b = int(temp[7])
    col = (r,g,b)
    e = Enemy(x, y, size, xv, yv, col)
    enemies.append(e)





# stay on screen
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # fill the background with white (or don't!)
    screen.fill((255, 255, 255))
    
    # TODO draw and move here
    for e in enemies:
        e.draw(screen)
        e.move()


    
    
    # pushes the screen to the current display
    pygame.display.flip()
    
    # delay a moment
    pygame.time.delay(500)


