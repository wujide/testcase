# coding=utf-8
# author__= 'wujide'

# 找出两个有序数组中想同的数，并输出到一个新的数组中


def find_same_num_from_two_list(la, lb):
    lc = []
    for i in range(len(la)):
        for j in range(len(lb)):
            if la[i] == lb[j]:
                lc.append(la[i])
    return lc


if __name__ == '__main__':
    a = [1, 2, 3, 4]
    b = [3, 4, 5, 6]
    print find_same_num_from_two_list(a, b)
