# coding=utf-8
# __author__='wujide'
import urllib
import urllib2
import interface_test_class


def getInvestInfo():
    # 初始化login接口参数
    getInvestInfo = interface_test_class.InterfaceTest(r"../info/getInvestInfo_para.txt")
    # 获取参数
    values = getInvestInfo.data_get()
    # print values
    data = urllib.urlencode(values)
    req = urllib2.Request(values['url'])
    response = urllib2.urlopen(req, data)
    # print "type(response):", type(response)
    dd = response.read()
    # print "type(dd):", type(dd)
    return dd
    #write_to_file(dd)

if __name__ == "__main__":
    print getInvestInfo()
