# coding=utf-8
# __author__='wujide'

from tools.getVerifCodeNew_get import verifCode_get
from tools.captcha_get import captcha_get
from interface_test_class import InterfaceTest


def register(phone_num):
    # use regression to get captcha（图形码）
    captcha_get()
    # post the getVerifCodeNew() to get verifcode(验证码）
    verifCode = verifCode_get(phone_num)
    # para_get()
    para_path = r"../info/register_para.txt"
    obj = InterfaceTest(para_path)
    obj.para_get(para_path=para_path, iterface_url='url_register')
    values = obj.data_get()
    values['phoneNum'] = str(phone_num)
    values['verifCode'] = verifCode
    values['appId'] = str(phone_num)
    print values
    response = obj.data_post(values)
    data = response.read()  # <type 'str'>

    file_save = r"../data/register"
    obj.data_save(file_save, data)
    obj.pass_or_fail(file_save)
    return data


if __name__ == '__main__':
    print register(13800138047)


