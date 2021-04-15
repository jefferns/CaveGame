import pygame


class Background:
    def __init__(self, x, y, height, width, path=""):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        if path:
            self.image = pygame.image.load(path)