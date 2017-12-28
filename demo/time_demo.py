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

print "---------------------------------------------"
# Case 1： 计算在某个时间段之内的工作日天数
from business_calendar import Calendar, MO, TU, WE, TH, FR
import datetime
date1 = datetime.datetime(2013,1,10)
# normal calendar, no holidays
cal = Calendar()
date2 = datetime.datetime(2013,3,20)
print('%s days between %s and %s' % (cal.busdaycount(date1, date2), date1, date2))

# Case 2： 计算若干工作日之后的日期
date3 = datetime.datetime(2018, 1, 1)
cal = Calendar()
date4 = cal.addbusdays(date3, 33)
print("The specified date will be %s" % date4)

# Case 3： 结合假期，以及星期的概念，计算工作日，可在holodays 中加入非工作日的日期
date5 = datetime.datetime(2018, 1, 1)
# normal calendar, no holidays
cal = Calendar(holidays=['2018-01-02', '2018-01-03'])
date6 = datetime.datetime(2018, 1, 6)
print('%s business days between %s and %s' % (cal.busdaycount(date5, date6), date5, date6))


