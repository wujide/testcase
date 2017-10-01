# coding=utf-8
# __author__='wujide'

import MySQLdb
from flask import json

with open(r"../info/db", 'r') as f:
    values = json.dumps(f.read())  # type(values): <type 'str'>
    d = eval(json.loads(values))  # type(data): <type 'dict'>
db = MySQLdb.connect(d['db_addr'], d['user'], d['pwd'], d['db_lib'])
cursor = db.cursor()
cmd = "SELECT * FROM tb_customer_login WHERE invit_Customer_id = '1360000929'"
cursor.execute(cmd)
data = cursor.fetchone()
print data
db.close()