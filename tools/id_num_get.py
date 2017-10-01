# coding=utf-8
# __author__='wujide'
import random
from flask import json


def get_id_num():
    address_str = ['110108', '120114', '130283', '130304', '130423', '211201', '230702', '330106', '440402', '450305']
    birth_code = ['20000101', '19990101', '19980101', '19970101', '19960101', '19950101', '19940101', '19930101',
                  '19920101', '19910101', '19900101']
    random_code = random.randrange(1000, 9999, 1)
    id_num = random.choice(address_str) + random.choice(birth_code) + str(random_code)
    return id_num_anti_duplicated(id_num)


def id_num_anti_duplicated(id_num):
    with open(r'../data/id_num_list', 'r') as f:
        id_num_list = eval(json.loads(json.dumps(f.read())))
        # print id_num_list
        if id_num in id_num_list:
            print "Duplicated, find another one"
            get_id_num()
        else:
            print "Get a new id_num:", id_num
            id_num_list.append(id_num)
            # print "---id_num_list 2-----", id_num_list
            with open(r'../data/id_num_list', 'w') as ff:
                json.dump(id_num_list, ff)
                return id_num


if __name__ == "__main__":
    get_id_num()
    # id_num_anti_duplicated('130423199901012166')
