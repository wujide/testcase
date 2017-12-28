# coding=utf-8
# __author__='wujide'

from heapq import *
from random import shuffle

data = range(10)
print data
print shuffle(data)
heap = []
for n in data:
    heappush(heap, n)
print "heap:", heap
