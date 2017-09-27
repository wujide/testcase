# coding=utf-8
# __author__='wujide'

from interface_test_class import InterfaceTest


def productInfo():
    # para_get()
    para_path = r"../info/productInfo_para.txt"
    obj = InterfaceTest(para_path)
    obj.para_get(para_path=para_path, iterface_url='url_productInfo')
    values = obj.data_get()
    response = obj.data_post(values)
    data = response.read()  # <type 'str'>
    file_save = r"../data/productInfo"
    obj.data_save(file_save, data)
    obj.pass_or_fail(file_save)
    return data


if __name__ == '__main__':
    print productInfo()