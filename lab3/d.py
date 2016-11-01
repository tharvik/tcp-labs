#!/usr/bin/env python3

import socket

HOST_PORT = ('localhost', 5002)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect(HOST_PORT)

message = 'O Romeo, Romeo! wherefore art thou Romeo?'
print('sending:', message)
sock.sendall(message.encode())

received = 0
expected = len(message)

while received < expected:
    data = sock.recv(16).decode()
    received += len(data)
    print('received:', data)
while True:
    pass
