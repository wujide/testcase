# coding=utf-8
# __author__='wujide'

import paramiko
from flask import json


def para_get():
    with open(r"../info/server", 'r') as f:
        values = json.dumps(f.read())  # type(values): <type 'str'>
        para = eval(json.loads(values))  # type(data): <type 'dict'>
        # cmd1 = r"tail /ywdata/tomcat7-appInterface/logs/catalina.out|grep 13800138048"
        # cmd1 = r"echo hello;echo hellooo"
        para['cmd1'] = r"ls; cd /ywdata; ls"
        return para


def connect():
    # use the paramiko connect the host,return conn
    para = para_get()
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print '''------connecting to %s -------- ''' % para['ip']
    try:
        ssh.connect(para['ip'], para['port'], para['user'], para['pwd'])
        return ssh
    except:
        return None


def ssh_cmd():
    cmd = r"ls; cd /ywdata; ls"
    result = ""
    ssh = connect()
    if not ssh:
        print "no server connected "
    try:
        stdin, stdout, stderr = ssh.exec_command(cmd, get_pty=True)
        result = stdout.read()
        print "result:", result
        ssh.close()
    except:
        print "ssh_cmd err."
    return result



if __name__ == '__main__':
    ssh_cmd()


