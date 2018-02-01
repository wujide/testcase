# coding=utf-8
# __author__='wujide'

import socket

s = socket.socket()
host = socket.gethostname()
port = 9999

s.connect((host, port))
print s.recv(1024)

