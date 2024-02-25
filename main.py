import pygame
import socket
import threading

from map import Map
from player import Player


def listen(server, player):
    while 1:
        data = server.recv(1024).decode()
        print(f"data from server: {data}")
        cmd = data.split("=")
        if cmd[0] == "moving":
            player.moving = int(cmd[1])


FPS = 30

# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((1920, 1080), pygame.SCALED + pygame.NOFRAME + pygame.FULLSCREEN, 32, vsync=1)
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

ip = ""
port = 5000

client_socket = socket.socket()
client_socket.connect((ip, port))

all_sprites = pygame.sprite.Group()
player1 = Player(16, 9)
player2 = Player(17, 9)
all_sprites.add(player1, player2)

gameMap = Map(player1, player1, screen)

data = client_socket.recv(1024).decode()
if data == "start":
    running = True

t1 = threading.Thread(target=listen, args=(client_socket, player2), daemon=False)
t1.start()

# Цикл игры
while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    # Ввод процесса (события)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False
            if event.key == pygame.K_w and player1.moving != 3:
                player1.moving = 1
                client_socket.send("moving=1".encode())
            if event.key == pygame.K_a and player1.moving != 4:
                player1.moving = 2
                client_socket.send("moving=2".encode())
            if event.key == pygame.K_s and player1.moving != 1:
                player1.moving = 3
                client_socket.send("moving=3".encode())
            if event.key == pygame.K_d and player1.moving != 2:
                player1.moving = 4
                client_socket.send("moving=4".encode())

    # Обновление


    # Рендеринг
    screen.fill((0, 0, 0))

    gameMap.update()
    if gameMap.lose:
        running = False
    all_sprites.draw(screen)
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()

pygame.quit()
client_socket.close()
