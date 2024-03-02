import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, color, trailColor):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((60, 60))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.trailColor = trailColor
        self.relX = x
        self.relY = y
        self.rect.x = (self.relX - 1) * 60
        self.rect.y = (self.relY - 1) * 60
        self.moving = 3

    def coord(self, ox, oy):
        self.rect.x = (self.relX - 1) * 60 + ox
        self.rect.y = (self.relY - 1) * 60 + oy
