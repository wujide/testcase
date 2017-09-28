# coding=utf-8
# __author__='wujide'
from flask import json
from interface_test_class import InterfaceTest


def login():
    # 初始化login 实例
    login_obj = InterfaceTest(r"../info/login_para.txt")
    # 获取参数
    values = login_obj.data_get()  # <type 'dict'>
    response = login_obj.data_post(values)
    data = response.read()  # <type 'str'>
    file_save = r'../data/login'
    login_obj.data_save(file_save, data)
    login_obj.pass_or_fail(file_save)
    return data

if __name__ == "__main__":
    print login()
