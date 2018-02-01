# coding=utf-8
# __author__='wujide'

import socket

s = socket.socket()
host = socket.gethostname()
port = 9999
print host
s.bind((host, port))

s.listen(5)
while(True):
    c, addr = s.accept()
    print "Got Connection from %s", addr
    c.send('Thank you for connection')
    c.close()