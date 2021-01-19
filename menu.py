
import pygame


class Button:
    def __init__(self, x, y, height, width, name, path):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.name = name
        self.path = path
        self.image = pygame.image.load(self.path + self.name + '.png')
        self.selected = False
    
    def select(self):
        self.selected = True
        self.image = pygame.image.load(self.path + self.name + '_selected.png')

    def unselect(self):
        self.selected = False
        self.image = pygame.image.load(self.path + self.name + '.png')
