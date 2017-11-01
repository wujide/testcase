# coding=utf-8
# __author__='wujide'
from test_case.interface_test_class import InterfaceTest
from tools.log_read import log_read
from tools.server_log_get import server_log_get


def captcha_get():
    return '1234'
    para_path = r"../info/captcha_para.txt"
    obj = InterfaceTest(para_path)
    values = obj.data_get()  # <type 'dict'>
    response = obj.data_post(values)

    cmd = r'cat /ywdata/tomcat7-appInterface/logs/catalina.out  | grep "图形验证码生成成功"|tail -n 1'
    pattern = r'图形验证码生成成功【(\d*?)】'
    data = server_log_get(cmd)
    log_data = log_read(pattern, data)
    print log_data[0], type(log_data)

    data = response.read()  # <type 'str'>
    file_save = r'../data/captcha'
    obj.data_save(file_save, data)
    obj.pass_or_fail(file_save)
    return log_data[0]


if __name__ == "__main__":
    print captcha_get()
