# coding=utf-8
# __author__='wujide'

import httplib
import json

httpClient = None
try:
    httpClient = httplib.HTTPConnection('www.baidu.com', 80, timeout=30)  # 注意，此处域名不要带http://
    headers = {'Accept': 'application/xml', 'cookie': 'BAIDUID=A49722ED1DEB8291B5CF5DDC3B7A6053:FG=1'}  # 如果有headers的话就带上。没有则不用
    httpClient.request(method='GET', url='/main/?r=get/student', headers=headers)
    response = httpClient.getresponse()
    data = json.load(response, encoding='utf-8')  # 将获取到的内容转换为json类型数据
except Exception, e:
    raise e
finally:
    if httpClient:
        httpClient.close()
