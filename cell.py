import pygame


class Cell():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.offsetX = 0
        self.offsetY = 0
        self.color = 0

    def paint(self, color):
        self.color = color

    def update(self, screen):
        if self.color == 1:
            pygame.draw.rect(screen, (0, 155, 255), ((self.x - 1) * 60 + self.offsetX, (self.y - 1) * 60 + self.offsetY, 60, 60))
        if self.color == 2:
            pygame.draw.rect(screen, (155, 0, 255), ((self.x - 1) * 60 + self.offsetX, (self.y - 1) * 60 + self.offsetY, 60, 60))
