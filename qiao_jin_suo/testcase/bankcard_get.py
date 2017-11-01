# coding=utf-8
# __author__='wujide'

# coding=utf-8
# __author__='wujide'
import random
from flask import json


def get_bankcard_num():
    address_code_pre = '6225881234'  # 招行前6位
    random_code = random.randrange(100000, 999999, 1)
    while True:
        id_num = address_code_pre + str(random_code)
        if id_num_anti_duplicated(id_num):
            continue
        else:
            break
    return id_num


def id_num_anti_duplicated(id_num):
    with open(r'../data/get_bankcard_num', 'r') as f:
        id_num_list = eval(json.loads(json.dumps(f.read())))
        # print id_num_list
        if id_num in id_num_list:
            print "Duplicated, find another one"
            return True
        else:
            print "Get a new id_num:", id_num
            id_num_list.append(id_num)
            # print "---id_num_list 2-----", id_num_list
            with open(r'../data/get_bankcard_num', 'w') as ff:
                json.dump(id_num_list, ff)
            return False


if __name__ == "__main__":
    print get_bankcard_num()
    # id_num_anti_duplicated('130423199901012166')