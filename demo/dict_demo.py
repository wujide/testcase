# coding=utf-8
# __author__='Administrator'

d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

L = [1, 2, 3, 4]

dd = {}
for key in dd.fromkeys(L).keys():
    dd[key] = 'default'

print dd
