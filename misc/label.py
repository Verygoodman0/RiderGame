import pygame


class Label():
    def __init__(self, x, y, text, fSize = 60):
        self.x = x
        self.y = y
        self.text = text
        self.fSize = fSize
        self.font = pygame.font.SysFont('Comic Sans MS', 60)

    def update(self, screen):
        text = self.font.render(self.text, False, (255, 255, 255))
        screen.blit(text, (self.x, self.y))

    def setText(self, text):
        self.text = text
