# coding=utf-8
# __author__='wujide'
from flask import json

'''
def id_card_anti_duplicated(id, list, file):
    with open(file, 'r') as f:
        d = json.dumps(f.read())
        id_num_list = eval(json.loads(d))
        # print id_num_list
        if id in list:
            print "Duplicated, find another one"
            return False
        else:
            id_num_list.append(id)
            # print "---id_num_list 2-----", id_num_list
    with open(file, 'w') as ff:
        json.dump(id_num_list, ff)
    return id_card

'''
