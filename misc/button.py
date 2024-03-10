import pygame


class Button():
    def __init__(self, x, y, w, h, text, color=(0,255,0), tcolor=(0, 200, 0)):
        self.font = pygame.font.SysFont('Comic Sans MS', 60)
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.text = text
        self.color = color
        self.tcolor = tcolor

        self.targeted = False

    def update(self, screen, mouse):
        if self.x < mouse[0] < self.x + self.w and self.y < mouse[1] < self.y + self.h:
            self.targeted = True
        else:
            self.targeted = False

        if not self.targeted:
            pygame.draw.rect(screen, self.color, [self.x, self.y, self.w, self.h])
        else:
            pygame.draw.rect(screen, self.tcolor, [self.x, self.y, self.w, self.h])
        text = self.font.render(self.text, False, (0, 0, 0))

        screen.blit(text, (self.x, self.y))

    def setPosition(self, x, y):
        self.x = x
        self.y = y
