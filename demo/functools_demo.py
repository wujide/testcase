# coding=utf-8
# __author__='wujide'

import functools


def int2(x, base=2):
    return int(x, base)

int8 = functools.partial(int, base=8)

print int2('1010')
print int8('1010')
