import socket
import threading
import sys

# get the hostname
host = "localhost"
port = 5000

r1 = False
r2 = False

print("Server started!")


def listen1(_from, _to):
    global r1, r2
    while 1:
        data = _from.recv(1024).decode()
        if data != "":
            if data == "restart":
                r1 = True
                if r1 and r2:
                    r1 = False
                    r2 = False

                    _from.send("start=1".encode())
                    _to.send("start=2".encode())
            else:
                print(f"data from client1: {data}")
                _to.send(data.encode())


def listen2(_from, _to):
    global r2, r1
    while 1:
        data = _from.recv(1024).decode()
        if data != "":
            if data == "restart":
                r2 = True
                if r1 and r2:
                    r1 = False
                    r2 = False

                    _from.send("start=1".encode())
                    _to.send("start=2".encode())
            else:
                print(f"data from client2: {data}")
                _to.send(data.encode())


server_socket = socket.socket()
server_socket.bind((host, port))

server_socket.listen(2)
conn, address = server_socket.accept()
print("Connection from: " + str(address))
conn2, address2 = server_socket.accept()
print("Connection from: " + str(address2))

conn.send("start=1".encode())
conn2.send("start=2".encode())


t1 = threading.Thread(target=listen1, args=(conn, conn2), daemon=True)
t2 = threading.Thread(target=listen2, args=(conn2, conn), daemon=True)
t1.start()
t2.start()
t1.join()
t2.join()

while 1:
    s = input()
    if s == "stop" or s == "exit":
        sys.exit(0)
