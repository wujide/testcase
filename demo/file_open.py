# coding=utf-8
# __author__='Administrator'

import fileinput


for line in fileinput.input(r'test_file'):
    print line
