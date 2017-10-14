# coding=utf-8
# __author__='wujide'
from flask import json
from test_case.interface_test_class import InterfaceTest
from tools.captcha_get import captcha_get
from tools.log_read import log_read
from tools.server_log_get import server_log_get


def verifCode_get(phone_num):
    # 取图形码
    captCode = captcha_get()
    # 去文件中取 captcha
    with open(r"../data/captcha", 'r') as f:
        values = json.dumps(f.read())
        captcha = eval(json.loads(values))
    para_path = r"../info/verifCode_para.txt"
    obj = InterfaceTest(para_path)
    obj.para_get(para_path=para_path, iterface_url='url_getVerifCodeNew')
    # 获取参数
    data = obj.data_get()  # <type 'dict'>
    data['phoneNum'] = phone_num
    data['captcha'] = captCode
    data['captCode'] = captcha['data']['captCode']
    data['isRegisted'] = 1
    response = obj.data_post(data)
    d = response.read()  # <type 'str'>
    file_save = r'../data/verifCode'
    obj.data_save(file_save, d)
    obj.pass_or_fail(file_save)

    # 发送验证码执行完毕phoneNum=[13800138048]verifCode=[9943]
    cmd_verif_code = r'cat /ywdata/tomcat7-appInterface/logs/catalina.out |grep "发送验证码执行完毕"| tail -n 1'
    data_verif_code = server_log_get(cmd_verif_code)
    print "data_verif_code:", data_verif_code
    pattern = r"发送验证码执行完毕phoneNum=\[" + str(phone_num) + r"\]" + r"verifCode=\[(.*?)\]"
    log_data_verif_code = log_read(pattern, data_verif_code)
    print "log_data_verif_code:", log_data_verif_code
    return log_data_verif_code[0]


if __name__ == "__main__":
    print verifCode_get(13800138040)
