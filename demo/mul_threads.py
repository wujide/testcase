# coding=utf-8
# __author__='wujide'

import threading
from time import ctime, sleep


def music(func):
    for i in range(2):
        print "I was listening to %s. %s" % (func, ctime())
        sleep(1)


def move(func):
    for i in range(2):
        print "I was at the %s! %s" % ( func, ctime())
        sleep(5)

threads = []
t1 = threading.Thread(target=music, args=(u'爱情买卖',))
threads.append(t1)
t2 = threading.Thread(target=move, args=(u'阿凡达',))
threads.append(t2)

if __name__ == '__main__':
    for t in threads:
        t.setDaemon(True)
        t.start()  # start是启动线程
    t.join()  # join是阻塞当前线程
    print "all over %s" % ctime()
