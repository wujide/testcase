# coding=utf-8
# __author__='wujide'

import urllib
import urllib2

url = 'https://www.baidu.com/s'
values = {'wd': 'TEST'}
data = urllib.urlencode(values)
url2 = url + '?' + data
res = urllib2.urlopen(url2)
the_page = res.read()
print the_page
