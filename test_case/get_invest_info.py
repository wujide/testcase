# coding=utf-8
# __author__='wujide'

from flask import json
from interface_test_class import InterfaceTest


def getInvestInfo():
    # para_get()
    para_path = r"../info/getInvestInfo_para.txt"
    obj = InterfaceTest(para_path)
    # get the latest loginToken and update to the para file
    obj.para_get(para_path=para_path, iterface_url='url_getInvestInfo')
    values = obj.data_get()
    response = obj.data_post(values)
    data = response.read()  # <type 'str'>
    file_save = r"../data/getInvestInfo"
    obj.data_save(file_save, data)
    obj.pass_or_fail(file_save)
    return data


def para_get():
    # get interface url: getInvestInfo
    with open(r"../info/url", 'r') as f:
        values = json.dumps(f.read())
        d = eval(json.loads(values))
    # get the loginToken
    with open(r"../data/login", 'r') as f:
        values = json.dumps(f.read())
        dd = eval(json.loads(values))
    with open(r"../info/getInvestInfo_para.txt", 'r') as f:
        values = json.dumps(f.read())
        data = eval(json.loads(values))
        data['loginToken'] = dd['data']['loginToken']
        data['url'] = d['url_getInvestInfo']
    # write to a file
    with open(r'../info/getInvestInfo_para.txt', 'wb+') as f:
        json.dump(data, f)

if __name__ == "__main__":
    print getInvestInfo()
