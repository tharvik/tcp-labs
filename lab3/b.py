#!/usr/bin/env python3

import socket

HOST_PORT = ('', 5001)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(HOST_PORT)

while True:
    data, addr = s.recvfrom(1024)
    print('Received data: ', data.decode())
    print('From Address: ', addr)
