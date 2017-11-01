# coding=utf-8
# __author__='wujide'
from time import ctime

from flask import json
from interface_test_class import InterfaceTest


def register(phone_num):
    print "started at %s" % ctime()
    # use regression to get captcha（图形码）
    # captcha_get()
    # post the getVerifCodeNew() to get verifcode(验证码）
    # verifCode = verifCode_get(phone_num)
    # para_get()

    para_path = r"../info/login_para.txt"
    obj = InterfaceTest(para_path)
    values = obj.data_get()
    values['phoneNum'] = str(phone_num)
    values['verifCode'] = '1234'
    values['codeKaptcha'] = '123456'
    print values
    response = obj.data_post(values)
    data = response.read()  # <type 'str'>
    file_save = r"../data/login"
    obj.data_save(file_save, data)
    # obj.pass_or_fail(file_save)
    return data


if __name__ == '__main__':
    print register(13800138006)
