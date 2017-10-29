# coding=utf-8
# __author__='wujide'
import urllib2
import json
from interface_test_class import InterfaceTest


def initInvest():
    para_path = r"../info/trans_initInvest_para.txt"
    obj = InterfaceTest(para_path)
    values = eval(json.loads(obj.data_get()))
    print "----values---", values

    # req = urllib2.Request(values['url'], headers=values['headers'])
    # req = urllib2.Request(values['url'], headers=values['headers'])
    response = obj.data_post_qjs(values)
    data = response.read()  # <type 'str'>
    file_save = r"../data/trans_initInvest"
    obj.data_save(file_save, data)
    obj.pass_or_fail(file_save)
    return data


if __name__ == '__main__':
    print initInvest()
