import pygame
import socket
import threading

from map import Map
from player import Player
from misc.button import Button
from misc.label import Label


def listen(server, player):
    global player1, player2, gameMap, state

    while 1:
        try:
            data = server.recv(1024).decode()
            if data != "":
                # print(f"data from server: {data}")
                cmd = data.split("=")
                if cmd[0] == "moving":
                    player.moving = int(cmd[1])
                if "lose" in cmd[0]:
                    lose(int(cmd[0][-1]))
                if "start" in cmd[0]:
                    if cmd.split("=")[1] == "1":
                        player1 = Player(16, 9, (0, 0, 255), 1)
                        player2 = Player(17, 9, (255, 0, 0), 2)
                    else:
                        player2 = Player(16, 9, (0, 0, 255), 1)
                        player1 = Player(17, 9, (255, 0, 0), 2)

                all_sprites = pygame.sprite.Group()
                all_sprites.add(player1, player2)

                gameMap = Map(player1, player2, screen)
                state = 1

        except Exception:
            pass


def lose(color):
    global state

    state = 2
    if color == 1:
        labelLose.setText("lose blue")
    else:
        labelLose.setText("lose purple")

    gameMap.lose = 0
    client_socket.close()
    player1.start()
    player2.start()     

FPS = 60

# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((1920, 1080), pygame.SCALED + pygame.NOFRAME + pygame.FULLSCREEN, 32, vsync=1)
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

ip = "0.tcp.eu.ngrok.io"
port = 15678

state = 0
buttonPlay = Button(810, 540, 300, 100, "Play")
buttonExit = Button(810, 740, 300, 100, "Exit")
buttonRestart = Button(810, 540, 300, 100, "Restart")
labelLose = Label(885, 300, "Ya ghoul😈")


running = True
# Цикл игры
while running:
    if state == 0:  # main menu
        clock.tick(FPS)
        screen.fill((0, 0, 0))

        buttonPlay.update(screen, pygame.mouse.get_pos())
        buttonExit.update(screen, pygame.mouse.get_pos())

        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if buttonPlay.targeted:
                    FPS = 30
                    state = 1
                    client_socket = socket.socket()
                    client_socket.connect((ip, port))
                    data = client_socket.recv(1024).decode()
                    if data.split("=")[0] == "start":
                        if data.split("=")[1] == "1":
                            player1 = Player(16, 9, (0, 0, 255), 1)
                            player2 = Player(17, 9, (255, 0, 0), 2)
                            running = True
                        else:
                            player2 = Player(16, 9, (0, 0, 255), 1)
                            player1 = Player(17, 9, (255, 0, 0), 2)
                            running = True

                    all_sprites = pygame.sprite.Group()
                    all_sprites.add(player1, player2)

                    gameMap = Map(player1, player2, screen)

                    t1 = threading.Thread(target=listen, args=(client_socket, player2), daemon=False)
                    t1.start()

                if buttonExit.targeted:
                    running = False

        pygame.display.flip()
    elif state == 1:
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
                elif event.key == pygame.K_a and player1.moving != 4:
                    player1.moving = 2
                    client_socket.send("moving=2".encode())
                elif event.key == pygame.K_s and player1.moving != 1:
                    player1.moving = 3
                    client_socket.send("moving=3".encode())
                elif event.key == pygame.K_d and player1.moving != 2:
                    player1.moving = 4
                    client_socket.send("moving=4".encode())

        # Обновление

        # Рендеринг
        screen.fill((0, 0, 0))

        gameMap.update(client_socket)
        if gameMap.lose != 0:
            lose(gameMap.lose)
        all_sprites.draw(screen)
        # После отрисовки всего, переворачиваем экран
        pygame.display.flip()
    elif state == 2:
        clock.tick(FPS)
        screen.fill((0, 0, 0))

        buttonRestart.update(screen, pygame.mouse.get_pos())
        buttonExit.update(screen, pygame.mouse.get_pos())
        labelLose.update(screen)

        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if buttonRestart.targeted:
                    client_socket.send("restart".encode())


                if buttonExit.targeted:
                    running = False

        pygame.display.flip()


pygame.quit()
client_socket.close()
