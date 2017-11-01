# coding=utf-8
# __author__='wujide'
import json
import urllib
from interface_test_class import InterfaceTest


def smsCaptcha(mobile):
    para_path = r"../info/login_smsCaptcha_para.txt"
    obj = InterfaceTest(para_path)
    values = obj.data_get()
    v1 = eval(json.loads(values))
    # print "v1:", v1
    v1['mobile'] = str(mobile)
    with open(para_path, 'wb+') as f:
        json.dump(v1, f)
    v2 = obj.data_get()  # get the value one more time
    # print "v2:", (type(v2), v2)
    response = obj.data_post(v2)
    data = response.read()  # <type 'str'>
    print data
    file_save = r"../data/login_smsCaptcha"
    obj.data_save(file_save, data)
    # obj.pass_or_fail(file_save)
    return data


if __name__ == '__main__':
    print smsCaptcha(13800138005)
