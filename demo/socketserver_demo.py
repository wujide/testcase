# coding=utf-8
# __author__='wujide'

from SocketServer import TCPServer, StreamRequestHandler


class Handle(StreamRequestHandler):
    def handle(self):
        addr = self.request.getpeername()
        print "Got connection from ", addr
        self.wfile.write('Thank you for connection')

server = TCPServer(('', 9999), Handle)
server.serve_forever()
