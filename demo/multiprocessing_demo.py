# coding=utf-8
# __author__='wujide'
from multiprocessing import Pool
import os, time, random


def long_time_task(name):
    print 'Run task %s (%s)...' % (name, os.getpid())
    start = time.time()
    sum = 0
    for num in range(1000):
        sum += num
    end = time.time()
    print 'Task %s runs %0.2f seconds.' % (name, (end - start))


if __name__ == '__main__':
    print "start at :", time.ctime()
    print 'Parent process %s.' % os.getpid()
    start = time.time()
    p = Pool()
    print "Pool start at :", time.ctime()
    for i in range(100):
        p.apply_async(long_time_task, args=(i,))
    #print 'Waiting for all subprocesses done...'
    print "after for:", time.ctime()
    # print "start:", time.ctime()
    p.close()
    p.join()
    print 'All subprocesses done.'
    end = time.time()
    print "end:", time.ctime()
    print 'All Task runs %0.2f seconds.' % (end - start)
