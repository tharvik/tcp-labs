#!/usr/bin/env python3

import socket

HOST_PORT = ('localhost', 5002)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

sock.bind(HOST_PORT)
sock.listen(1)

while True:
    connection, addr = sock.accept()

    while True:
        data = connection.recv(32).decode()
        print('received:', data)

        if data:
            connection.sendall(data.encode())
        else:
            print('No more data from', addr)
            break

    connection.close()

