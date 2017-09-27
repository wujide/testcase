# coding=utf-8
# __author__='wujide'

import os


def rm(filename):
    if os.path.isfile(filename):
        os.remove(filename)
