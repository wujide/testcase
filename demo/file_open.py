# coding=utf-8
# __author__='Administrator'





with open(r'../info/url', 'r') as f_url:
    lines = f_url.readline()
    print lines
    lines_strip = lines.split('=')
    url = lines_strip[1]
    print url

