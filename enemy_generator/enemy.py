import pygame, random

class Enemy:
    # ints for x, y, size, xv, yv
    # tuple (_,_,_) for col
    def __init__(self, x, y, size, xv, yv, col):
        self.x = x
        self.y = y
        self.size = size
        self.xv = xv
        self.yv = yv
        self.col = col
    
    def draw(self, screen):
        pygame.draw.circle(screen, self.col, (self.x, self.y), self.size)
        # optional, outline with black
        pygame.draw.circle(screen, (0,0,0), (self.x, self.y), self.size, width=3)
    
    def move(self):
        w, h = pygame.display.get_surface().get_size()
        # if the object hits left or right, flip x velocity
        if self.x < 0 or self.x > w:
            self.xv = -1*self.xv
        
        # if the object hits top or bottom, flip y velocity
        if self.y < 0 or self.y > h:
            self.yv = -1*self.yv
        
        # move
        self.x += self.xv
        self.y += self.yv

