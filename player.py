import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((60, 60))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.relX = x
        self.relY = y
        self.rect.x = (self.relX - 1) * 60
        self.rect.y = (self.relY - 1) * 60
        self.moving = 0

    def coord(self):
        # self.rect.x = (self.relX - 1) * 60
        # self.rect.y = (self.relY - 1) * 60
        pass
