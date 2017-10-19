# coding=utf-8
# __author__='wujide'
from logging import exception

import paramiko
from test_case.interface_test_class import InterfaceTest
from tools.phone_to_customer_id import phone_to_customerid


def cache_refresh(phone_num):
    para_path = r"../info/redis"
    obj = InterfaceTest(para_path)
    d = obj.data_get()
    customer_id = phone_to_customerid(phone_num)
    result = ""
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        print '''------connecting to %s -------- ''' % d['ip']
        ssh.connect(d['ip'], d['port'], d['user'], d['pwd'])
        cmd = 'redis-cli -h 127.0.0.1 -p 6379 -a 123456'
        cmd1 = r'get user_m_uid' + str(customer_id)
        result = {}
        stdin, stdout, stderr = ssh.exec_command(cmd)
        stdin1, stdout1, stderr1 = ssh.exec_command(cmd1)
        result = stdout1.read()  # todo: why no data in resutlt
        print "result:", result
        ssh.close()
    except Exception, e:
        print e
    return result

if __name__ == '__main__':
    cache_refresh('13800138000')
