# coding=utf-8
# __author__='wujide'

import paramiko
from flask import json

with open(r"../info/server", 'r') as f:
    values = json.dumps(f.read())  # type(values): <type 'str'>
    d = eval(json.loads(values))  # type(data): <type 'dict'>
    ip1 = d['ip']
    port1 = d['port']
    user1 = d['user']
    pwd1 = d['pwd']
    cmd1 = r"tail /ywdata/tomcat7-appInterface/logs/catalina.out|grep 13800138048"

print '''------connecting to %s -------- ''' % ip1


def ssh_cmd(ip, port, cmd, user, pwd):
    result = ""
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, port, user, pwd)
        stdin, stdout, stderr = ssh.exec_command(cmd)
        result = stdout.read()
        print "result:", result
        ssh.close()
    except:
        print "ssh_cmd err."
    return result


if __name__ == '__main__':
    ssh_cmd(ip1, port1, cmd1, user1, pwd1)
