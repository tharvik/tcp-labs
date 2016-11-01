#!/usr/bin/env python3

import socket

HOST_PORT = ('localhost', 5001)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.sendto(b'Hello, Romeo', HOST_PORT)
s.close()

print('Message sent')
