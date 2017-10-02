# coding=utf-8
# __author__='wujide'
import MySQLdb
from flask import json


def phone_to_customerid(phone_num):
    with open(r"../info/db", 'r') as f:
        values = json.dumps(f.read())  # type(values): <type 'str'>
        d = eval(json.loads(values))  # type(data): <type 'dict'>
    db = MySQLdb.connect(d['db_addr'], d['user'], d['pwd'], d['db_lib'], charset='utf8')
    cursor = db.cursor()
    cmd = "SELECT customer_id FROM tb_customer_login WHERE phoneNum = " + phone_num
    cursor.execute(cmd)
    data = cursor.fetchone()
    return data[0]
    db.close()


if __name__ == "__main__":
    print phone_to_customerid('13800138000')

