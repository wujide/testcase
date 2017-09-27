# coding=utf-8
# __author__='wujide'
import paramiko
from test_case.interface_test_class import InterfaceTest
from tools.log_read import log_read


# read the log from the server, str
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
        # cmd = r"cat /ywdata/tomcat7-appInterface/logs/catalina.out  | grep phoneNum=" + phone_num + "|tail -n 1"
        stdin, stdout, stderr = ssh.exec_command(cmd)
        result = stdout.read()
        print "result:", result
        '''
        # pattern = r'&captcha=(.*?)&captCode=(.*?)&isRegisted=(\d)'
        log_data = log_read(pattern, result)
        data = {
            "phoneNum": phone_num,
            "captcha": log_data[0][0],
            "captCode": log_data[0][1],
            "isRegisted": log_data[0][2]
        }
        '''
        ssh.close()
    except:
        print "ssh_cmd err."
    return result

if __name__ == '__main__':
    server_log_get('13800138048')