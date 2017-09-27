# coding=utf-8
# __author__='wujide'

import urllib
import urllib2
url = 'https://www.baidu.com/s'
values = {'wd': 'D_in'}
data = urllib.urlencode(values)
req = urllib2.Request(url, data)
response = urllib2.urlopen(req)
the_page = response.read()
# print the_page


import cookielib
url_cookie_test = r'http://www.renren.com/ajaxLogin'
# 创建一个cj的cookie的容器
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
# 将要POST出去的数据进行编码
data = urllib.urlencode({"email": 'email', "password": 'pass'})
r = opener.open(url_cookie_test, data)
print cj
