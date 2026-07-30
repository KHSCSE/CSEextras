import pygame, random

class Ball:
    def __init__(self):
        w, h = pygame.display.get_surface().get_size()
        self.size = 10
        self.x = w//2
        self.y = h//2
        self.xvel = random.choice([-5, -4, -3, 3, 4, 5])
        self.yvel = random.choice([-3, -4, -5, -6])
        self.col = (255,0,0)
    
    def draw(self, screen):
        pygame.draw.circle(screen, self.col, (self.x, self.y), self.size)
        # optional, outline with black
        pygame.draw.circle(screen, (0,0,0), (self.x, self.y), self.size, width=3)
    
    def move(self):
        w, h = pygame.display.get_surface().get_size()
        # if the object hits left or right, flip x velocity
        if self.x < 0 or self.x > w:
            self.xvel = -1*self.xvel
        
        # if the object hits top or bottom, flip y velocity
        if self.y < 0 or self.y > h:
            self.yvel = -1*self.yvel
        
        # move
        self.x = self.x + self.xvel
        self.y = self.y + self.yvel
    
    
