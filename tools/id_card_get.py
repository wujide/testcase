# coding=utf-8
# __author__='wujide'
import random
from flask import json


def get_id_card():
    address_str = ['110108', '120114', '130283', '130304', '130423', '211201', '230702', '330106', '440402', '450305']
    birth_code = ['20000101', '19990101', '19980101', '19970101', '19960101', '19950101', '19940101', '19930101',
                  '19920101', '19910101', '19900101']
    random_code = random.randrange(1000, 9999, 1)
    id_card = random.choice(address_str) + random.choice(birth_code) + str(random_code)
    # print id_card
    return id_card_anti_duplicated(id_card)


def id_card_anti_duplicated(id_card):
    with open(r'../data/id_card_list', 'r') as f:
        id_card_list = eval(json.loads(json.dumps(f.read())))
        # print id_card_list
        if id_card in id_card_list:
            print "Duplicated, find another one"
            get_id_card()
        else:
            id_card_list.append(id_card)
            # print "---id_card_list 2-----", id_card_list
            with open(r'../data/id_card_list', 'w') as ff:
                json.dump(id_card_list, ff)
                return id_card


if __name__ == "__main__":
    print get_id_card()
    # id_card_anti_duplicated('130423199901012166')
