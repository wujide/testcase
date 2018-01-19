# coding=utf-8
# __author__='wujide'

import random


def conflict(state, nextX):
    # row为行，col为列, state为皇后的状态
    nextY = len(state)    # 目前没冲突的行数
    for i in range(nextY):    # 从1- row行依次检测是否与row+1行皇后冲突
        if abs(state[i] - nextX) in (0, nextY - i):
            return True
    return False


def queens(num=8, state=()):
    # 生成器函数
    for pos in range(num):
        if not conflict(state, pos):
            if len(state) == num - 1:  # 产生当前皇后的位置信息
                yield (pos,)
            else:  # 把当前皇后的位置信息，添加到状态列表里，并传递给下一皇后。
                for result in queens(num, state + (pos,)):
                    yield (pos,) + result


def queen_print(solution):
    # 打印函数
    def line(pos, length=len(solution)):
        return '. ' * (pos) + 'X ' + '. ' * (length - pos - 1)

    for pos in solution:
        print line(pos)


for solution in list(queens(8)):
    print solution

print '  total number is ' + str(len(list(queens())))
print '  one of the range is:\n'
queen_print(random.choice(list(queens())))
