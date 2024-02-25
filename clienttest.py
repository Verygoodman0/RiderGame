import socket
import threading

host = "0.tcp.eu.ngrok.io"  # as both code is running on same pc
port = 17105  # socket server port number

client_socket = socket.socket()  # instantiate
client_socket.connect((host, port))  # connect to the server

def listen(socket):
    while 1:
        print(client_socket.recv(1024).decode())


t1 = threading.Thread(target=listen, args=(client_socket,), daemon=False)
t1.start()


while 1:
    message = input(" -> ")  # again take input
    client_socket.send(message.encode())  # send message
    print("msg sent")

client_socket.close()  # close the connection