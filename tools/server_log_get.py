# coding=utf-8
# __author__='wujide'
from logging import exception
import paramiko
from test_case.interface_test_class import InterfaceTest
from tools.log_read import log_read


# read the log from the server; output: str
def server_log_get(cmd):
    para_path = r"../info/server"
    obj = InterfaceTest(para_path)
    d = obj.data_get()
    result = ""
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        print '''------connecting to %s -------- ''' % d['ip']
        ssh.connect(d['ip'], d['port'], d['user'], d['pwd'])
        stdin, stdout, stderr = ssh.exec_command(cmd)
        result = stdout.read()
        print "result:", result
        ssh.close()
    except exception, e:
        print e
    return result

if __name__ == '__main__':
    cmd = r'cat /ywdata/tomcat7-appInterface/logs/catalina.out |tail -n 1'
    server_log_get(cmd)
