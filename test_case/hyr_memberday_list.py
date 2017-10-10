# coding=utf-8
# __author__='wujide'

from interface_test_class import InterfaceTest
from login import login


def memberday_list():
    para_path = r"../info/hyr_memberday_list_para.txt"
    obj = InterfaceTest(para_path)
    obj.para_get(para_path=para_path, iterface_url='url_hyr_memberday_list')
    values = obj.data_get()
    response = obj.data_post(values)
    data = response.read()  # <type 'str'>
    # print data
    file_save = r"../data/hyr_memberday_list"
    obj.data_save(file_save, data)
    obj.pass_or_fail(file_save)
    return data

if __name__ == '__main__':
    login()
    print memberday_list()
