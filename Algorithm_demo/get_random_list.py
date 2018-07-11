# coding=utf-8
# __author__='wujide'

import random


# 随机生成0~100之间的数值
def get_random_list(num):
    lists = []
    for n in range(num):
        lists.append(random.randint(0, 100))
    return lists
