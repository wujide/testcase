# coding=utf-8
# __author__='wujide'
from logging import exception

import paramiko
from test_case.interface_test_class import InterfaceTest


# read the log from the server; output: str
def cache_refresh():
    para_path = r"../info/redis"
    obj = InterfaceTest(para_path)
    d = obj.data_get()
    result = ""
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        print '''------connecting to %s -------- ''' % d['ip']
        ssh.connect(d['ip'], d['port'], d['user'], d['pwd'])
        cmd1 = 'redis-cli'
        cmd2 = 'auth 123456'
        cmd3 = 'get user_m_uid1360000929'
        cmd = r'''redis-cli
                auth 123456
                get user_m_uid1360000929
                '''

        stdin1, stdout1, stderr1 = ssh.exec_command(cmd1)
        stdin2, stdout2, stderr2 = ssh.exec_command(cmd2)
        stdin3, stdout3, stderr3 = ssh.exec_command(cmd3)
        #stdin, stdout, stderr = ssh.exec_command(cmd)
        result = stdout2.read()
        print "result:", result
        ssh.close()
    except Exception, e:
        print e
    return result

if __name__ == '__main__':
    cache_refresh()
