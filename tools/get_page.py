# coding=utf-8
# __author__='wujide'
import re
import urllib2


class GetPage:
    def __init__(self, url, para_name, pageIndex):
        self.total_url = url + "?" + str(para_name) + "=" + str(pageIndex)

    def getpage(self):
        request = urllib2.Request(self.total_url)
        response = urllib2.urlopen(request)
        # print response.read().decode('gbk')
        return response.read().decode('gbk')


url = 'http://mm.taobao.com/json/request_top_list.htm'
gt = GetPage(url, 'page', 1)
page = gt.getpage()


def getContents():

    pattern = re.compile(
        '<div class="list-item".*?pic-word.*?<a href="(.*?)".*?<img src="(.*?)".*?<a class="lady-name.*?>(.*?)</a>.*?<strong>(.*?)</strong>.*?<span>(.*?)</span>',
        re.S)
    items = re.findall(pattern, page)
    contents = []
    for item in items:
        contents.append([item[0], item[1], item[2], item[3], item[4]])
    print contents
    return contents

getContents()