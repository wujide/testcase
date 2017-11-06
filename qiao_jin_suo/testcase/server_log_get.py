# coding=utf-8
# __author__='wujide'
from logging import exception
import paramiko
from test_case.interface_test_class import InterfaceTest
from tools.log_read import log_read
from time import ctime


# read the log from the server; output: str
def server_log_get():
    para_path = r"../info/server"
    obj = InterfaceTest(para_path)
    d = obj.data_get()
    result = ""
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        print '''------connecting to %s -------- ''' % d['ip']
        ssh.connect(d['ip'], d['port'], d['user'], d['pwd'])
        print ctime()
        cmd = r'16; 1; echo hello'
        stdin, stdout, stderr = ssh.exec_command(cmd, get_pty=True)
        result = stdout.read(), stderr.read()
        # print "out = :", stdout.readlines()
        print "result:", result
        print '%s\tOK on %s\n' % (d['ip'], ctime())
        ssh.close()
    except exception, e:
        print e
    return result

if __name__ == '__main__':
    # cmd = r'zbqjs02-ecs-srv06'
    server_log_get()
