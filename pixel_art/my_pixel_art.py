import pygame, random

class My_Pixel_Art:
    def __init__(self, x_param=100, y_param=100, size_param=40):
        # initialize the variables for a 'pixel' object
        # this example is a 3x3 pixel art object
        self.colors = [
                    [(255,255,0), (0,255,255), (255,255,0)],
                    [(150,0,255), (255,0,255), (150,0,255)],
                    [(0,255,255), (0,150,255), (0,255,255)]
        ]
        self.x = x_param
        self.y = y_param
        self.size = size_param
    
    def draw(self, screen):
        gap = self.size/3 # change this for different sizes
        # TODO loops!
    
    
    
    def move(self):
        w, h = pygame.display.get_surface().get_size()
        # maybe TODO check if the object hit a wall, then move
    
    
    
