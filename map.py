import pygame
from cell import Cell


class Map():
    def __init__(self, player1, player2, screen):
        self.player1 = player1
        self.player2 = player2
        self.p1OffsetX = 0
        self.p1OffsetY = 0
        self.p2OffsetX = -60
        self.p2OffsetY = 0
        self.screen = screen
        self.map = [[Cell(i + 1, j + 1) for i in range(64)] for j in range(36)]
        self.lose = 0

    def update(self, client_socket):
        if self.player1.moving == 1:
                if self.player1.relY - 1 > 0 and self.map[self.player1.relY - 2][self.player1.relX - 1].color != 1 and self.map[self.player1.relY - 2][self.player1.relX - 1].color != 2:
                self.map[self.player1.relY - 1][self.player1.relX - 1].paint(self.player1.trailColor)
                self.player1.relY -= 1
                self.p1OffsetY += 60
            else:
                data = f"lose{self.player1.trailColor}"
                self.lose = self.player1.trailColor
                client_socket.send(data.encode())
        if self.player1.moving == 2:
            if self.player1.relX - 1 > 0 and self.map[self.player1.relY - 1][self.player1.relX - 2].color != 1  and self.map[self.player1.relY - 1][self.player1.relX - 2].color != 2:
                self.map[self.player1.relY - 1][self.player1.relX - 1].paint(self.player1.trailColor)
                self.player1.relX -= 1
                self.p1OffsetX += 60
            else:
                data = f"lose{self.player1.trailColor}"
                self.lose = self.player1.trailColor
                client_socket.send(data.encode())
        if self.player1.moving == 3:
            if self.player1.relY + 1 <= 36 and self.map[self.player1.relY][self.player1.relX - 1].color != 1 and self.map[self.player1.relY][self.player1.relX - 1].color != 2:
                self.map[self.player1.relY - 1][self.player1.relX - 1].paint(self.player1.trailColor)
                self.player1.relY += 1
                self.p1OffsetY += -60
            else:
                data = f"lose{self.player1.trailColor}"
                self.lose = self.player1.trailColor
                client_socket.send(data.encode())
        if self.player1.moving == 4:
            if self.player1.relX + 1 <= 64 and self.map[self.player1.relY - 1][self.player1.relX].color != 1 and self.map[self.player1.relY - 1][self.player1.relX].color != 2:
                self.map[self.player1.relY - 1][self.player1.relX - 1].paint(self.player1.trailColor)
                self.player1.relX += 1
                self.p1OffsetX += -60
            else:
                data = f"lose{self.player1.trailColor}"
                self.lose = self.player1.trailColor
                client_socket.send(data.encode())

        
        if self.player2.moving == 1:
            if self.player2.relY - 1 > 0:
                self.map[self.player2.relY - 1][self.player2.relX - 1].paint(self.player2.trailColor)
                self.player2.relY -= 1
                #  self.player2.rect.y -= 60
                self.p2OffsetY += 60
            else:
                # self.lose = True
                pass
        if self.player2.moving == 2:
            if self.player2.relX - 1 > 0:
                self.map[self.player2.relY - 1][self.player2.relX - 1].paint(self.player2.trailColor)
                self.player2.relX -= 1
                # self.player2.rect.x -= 60
                self.p2OffsetX += 60
            else:
                # self.lose = True
                pass
        if self.player2.moving == 3:
            if self.player2.relY + 1 <= 36:
                self.map[self.player2.relY - 1][self.player2.relX - 1].paint(self.player2.trailColor)
                self.player2.relY += 1
                # self.player2.rect.y += 60
                self.p2OffsetY += -60
            else:
                # self.lose = True
                pass

        if self.player2.moving == 4:
            if self.player2.relX + 1 <= 64:
                self.map[self.player2.relY - 1][self.player2.relX - 1].paint(self.player2.trailColor)
                self.player2.relX += 1
                # self.player2.rect.x += 60
                self.p2OffsetX += -60
            else:
                # self.lose = True
                pass

        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                self.map[i][j].offsetX = self.p1OffsetX
                self.map[i][j].offsetY = self.p1OffsetY
                self.map[i][j].update(self.screen)

        self.player2.coord(self.p1OffsetX, self.p1OffsetY)
        self.drawMap(self.screen)

    def drawMap(self, screen):
        # [pygame.draw.line(screen, (255, 255, 255), (0, i*15+15), (1920, i*15+15)) for i in range(71)]
        # [pygame.draw.line(screen, (255, 255, 255), (i*15+15, 0), (i*15+15, 1920)) for i in range(127)]
        pygame.draw.line(screen, (255, 255, 255), (-60 + self.p1OffsetX, -30 + self.p1OffsetY), (3900 + self.p1OffsetX, -30 + self.p1OffsetY), 60)
        pygame.draw.line(screen, (255, 255, 255), (-30 + self.p1OffsetX, -60 + self.p1OffsetY), (-30 + self.p1OffsetX, 2220 + self.p1OffsetY), 60)
        pygame.draw.line(screen, (255, 255, 255), (3870 + self.p1OffsetX, -60 + self.p1OffsetY), (3870 + self.p1OffsetX, 2220 + self.p1OffsetY), 60)
        pygame.draw.line(screen, (255, 255, 255), (-60 + self.p1OffsetX, 2190 + self.p1OffsetY), (3900 + self.p1OffsetX, 2190 + self.p1OffsetY), 60)