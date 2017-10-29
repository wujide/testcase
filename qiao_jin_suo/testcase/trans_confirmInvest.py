# coding=utf-8
# __author__='wujide'
from interface_test_class import InterfaceTest
from trans_initInvest import initInvest


def confirmInvest():
    initInvest()
    para_path = r"../info/trans_confirmInvest_para.txt"
    obj = InterfaceTest(para_path)
    obj.para_get_for_qjs(para_path=para_path, get_para=r"../data/trans_initInvest")
    values = obj.data_get()
    # print (type(values), values)
    response = obj.data_post(values)
    data = response.read()  # <type 'str'>
    file_save = r"../data/trans_confirmInvest"
    obj.data_save(file_save, data)
    obj.pass_or_fail(file_save)
    return data


if __name__ == '__main__':
    print confirmInvest()
