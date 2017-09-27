# coding=utf-8
# __author__='wujide'
import cookielib
import urllib2

url = 'https://www.baidu.com'
filename = 'cookie.txt'
cookie = cookielib.MozillaCookieJar(filename)
handle = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handle)
response = opener.open(url)
cookie.save(ignore_discard=True, ignore_expires=True)
for item in cookie:
    print "Name = " + item.name
    print "value = " + item.value

#从文件中读取cookie内容到变量
cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
#创建请求的request
req = urllib2.Request(url)
#利用urllib2的build_opener方法创建一个opener
opener_file = urllib2.build_opener(handle)
response_file = opener_file.open(req)
print response_file.read()


