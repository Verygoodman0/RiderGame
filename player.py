import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, color, trailColor):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((60, 60))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.trailColor = trailColor
        self.startX = x
        self.startY = y
        self.moving = 0

        self.start()

    def coord(self, ox, oy):
        self.rect.x = (self.relX - 1) * 60 + ox
        self.rect.y = (self.relY - 1) * 60 + oy

    def start(self):
        self.relX = self.startX
        self.relY = self.startY
        self.rect.x = (self.relX - 1) * 60
        self.rect.y = (self.relY - 1) * 60
