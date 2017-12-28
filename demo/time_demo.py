# coding=utf-8
# __author__='Administrator'

import time
import datetime
t1 = time.clock()
t11 = time.time()
print time.time()   # 1514424932.0
print time.localtime()    # time.struct_time(tm_year=2017, tm_mon=12, tm_mday=28, tm_hour=9, tm_min=35, tm_sec=31, tm_wday=3, tm_yday=362, tm_isdst=0)
print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())    # 2017-12-28 09:35:32

print time.asctime()    # Thu Dec 28 09:35:31 2017
print time.mktime(time.localtime())    # 1514424931.0
print time.strptime(time.asctime())    # time.struct_time(tm_year=2017, tm_mon=12, tm_mday=28, tm_hour=9, tm_min=35, tm_sec=31, tm_wday=3, tm_yday=362, tm_isdst=-1)

print '---------------------------------------------'


print datetime.datetime(2017, 12, 26)   # 2017-12-26 00:00:00
print datetime.date(2017, 12, 26)  # 2017-12-26
print datetime.time(17, 12, 26)     # 17:12:26
print datetime.datetime.now()   # 2017-12-28 15:56:47.214000
print datetime.datetime.now().date()   # 2017-12-28

t2 = time.clock()
t22 = time.time()
print t2 -t1
print t22 -t11
