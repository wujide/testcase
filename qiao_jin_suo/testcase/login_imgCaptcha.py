# coding=utf-8
# __author__='wujide'
import urllib2


def imgCaptcha():
    url = 'https://api.gocfae.com/cust/login/imgCaptcha?clientId=41a57a8d493d4b1f969f45413bc26e30&data=1509459281474'
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    data = response.read()
    return '1234'


if __name__ == '__main__':
    print imgCaptcha()