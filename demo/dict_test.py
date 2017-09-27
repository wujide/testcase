# coding=utf-8
# __author__ = 'Administrator'
dict1 = {1: [1,11,111],2: [2,22,222]}
dict2 = {3: [3,33,333],4: [4,44,444]}


# 合并两个字典得到类似 {1: [1,11,111],2: [2,22,222],3: [3,33,333],4: [4,44,444]}
# 方法1：
dictMerged1 = dict(dict1.items()+dict2.items())
print "dictMerged1: ", dictMerged1

# 方法2：
dictMerged2 = dict(dict1, **dict2)
print "dictMerged2: ", dictMerged2

# 方法2等同于：
dictMerged = dict1.copy()
dictMerged.update(dict2)
print "dictMerged：", dictMerged

# 或者
dictMerged = dict(dict1)
dictMerged.update(dict2)


