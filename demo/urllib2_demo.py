# coding=utf-8
# __author__='wujide'

import urllib2
import urllib
import requests
from requests.auth import HTTPBasicAuth


def simple_demo():
    req = urllib2.Request('http://www.baidu.com')
    response = urllib2.urlopen(req)
    page = response.read()
    print page

    response = urllib.urlopen('http://www.douban.com')
    html = response.read()
    print html

simple_demo()

'''
    with open(r'../info/user_pwd_urllib2', 'r') as f:
        lines = f.readline()
        lines_strip = lines.split()
        user = lines_strip[0].split('=')[1]
        pwd = lines_strip[1].split('=')[1]


    github_url = 'https://api.github.com/user/repos'
    password_manager = urllib2.HTTPPasswordMgrWithDefaultRealm()
    password_manager.add_password(None, github_url, user, pwd)
    auth = urllib2.HTTPBasicAuthHandler(password_manager) # create an authentication handler
    opener = urllib2.build_opener(auth) # create an opener with the authentication handler
    urllib2.install_opener(opener) # install the opener...
    # request = urllib2.Request(github_url, urllib.urlencode({'name':'Test repo', 'description': 'Some test repository'})) # Manual encoding required
    # handler = urllib2.urlopen(request).read()
    req = requests.get(github_url, auth=HTTPBasicAuth(user, pwd))
    print req.text
    # handler = urllib2.urlopen(req).read()
    # print handler
'''