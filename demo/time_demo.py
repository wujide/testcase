# coding=utf-8
# __author__='Administrator'

import time
import datetime

print "time.time:", time.time()
print "time.asctime:", time.asctime()
print "time.localtime:", time.localtime()
print "time.mktime:", time.mktime(time.localtime())
print "time.strptime:", time.strptime(time.asctime())
print "time.strftime:", time.strftime(time.asctime())

print '---------------------------------------------'


print datetime.datetime(2017, 12, 26)   # 2017-12-26 00:00:00
print datetime.date(2017, 12, 26)  # 2017-12-26
print datetime.time(17, 12, 26)     # 17:12:26
