# coding=utf-8
# __author__='wujide'

from interface_test_class import InterfaceTest


def initInvest():
    para_path = r"../info/trans_initInvest_para.txt"
    obj = InterfaceTest(para_path)
    values = obj.data_get()
    response = obj.data_post(values)
    data = response.read()  # <type 'str'>
    file_save = r"../data/trans_initInvest"
    obj.data_save(file_save, data)
    obj.pass_or_fail(file_save)
    return data


if __name__ == '__main__':
    print initInvest()
