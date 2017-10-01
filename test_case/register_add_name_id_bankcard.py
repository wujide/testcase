# coding=utf-8
# __author__='wujide'

import MySQLdb
from flask import json
from tools.id_num_get import get_id_num
from tools.name_get import get_name


def db_register_add_name_id_bankcard(phone_num):
    with open(r"../info/db", 'r') as f:
        values = json.dumps(f.read())  # type(values): <type 'str'>
        d = eval(json.loads(values))  # type(data): <type 'dict'>
    db = MySQLdb.connect(d['db_addr'], d['user'], d['pwd'], d['db_lib'], charset='utf8')
    cursor = db.cursor()
    name = "'" + get_name() + "'"
    id_num = "'" + get_id_num() + "'"
    # todo: whot not work?
    cmd = r'set @phone_num=' + phone_num + ';' + r'set @card=' + id_num + ";" \
            r"set @name=" + name + ';' + \
        r'''select customer_id into @v_customer_id from tb_customer_info WHERE mobile_phone= @phone_num;\
            UPDATE tb_customer_info SET customer_name=@name, id_num=@card WHERE customer_id = @v_customer_id;\
            UPDATE tb_customer_login SET phoneNum=@phone_num, card_no=@card, real_name_verify='3' WHERE customer_id = @v_customer_id;
    '''

    cmd1 = r'UPDATE tb_customer_info SET customer_name=' + name + r',id_num=' + id_num + r' WHERE customer_id in (SELECT customer_id from tb_customer_login where phoneNum =' + phone_num + ')'
    cmd2 = r'UPDATE tb_customer_login SET card_no=' + id_num + r',real_name_verify="3" WHERE phoneNum= '+ phone_num

    cursor.execute(cmd1)
    cursor.execute(cmd2)
    db.commit()
    db.close()


if __name__ == "__main__":
    db_register_add_name_id_bankcard('13800138047')
