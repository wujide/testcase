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
        cmd1 = r'redis-cli'
        cmd2 = r'auth 123456'
        cmd3 = r'get user_m_uid' + str(customer_id)
        cmd = [r'redis-cli', 'auth 123456', 'get user_m_uid1360000929']
        result = {}
        for key in cmd:
            stdin, stdout, stderr = ssh.exec_command(key)
            result[key] = stdout.read(), stderr.read()
        #stdin, stdout, stderr = ssh.exec_command(r'redis-cli; auth 123456; get user_m_uid1360000929', get_pty=True)
        stdin, stdout, stderr = ssh.exec_command(r'redis-cli')
        result = stdout.read()  # todo: why no data in resutlt
        print "result:", result
        ssh.close()
    except Exception, e:
        print e
    return result

if __name__ == '__main__':
    cache_refresh('13800138000')
