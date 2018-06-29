# coding=utf-8
# __author__='wujide'


import random


# 随机生成0~100之间的数值
def get_random_number(num):
    lists = []
    i = 0
    while i < num:
        lists.append(random.randint(0, 100))
        i += 1
    return lists


# 冒泡排序
# 原理是对序列进行遍历，遍历过程中如果发现相邻两个元素，左边的元素大于右边，则进行交换，
# 一次遍历之后最大的元素被移动到对尾，然后进行第二次遍历，直到队列有序。


def bubble_sort(nums):
    for i in range((len(nums)-1)):
        for j in range(len(nums)-1-i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums


if __name__ == '__main__':
    la = get_random_number(10)
    lb = la[:]
    print "排序前：", la
    print "冒泡排序后：", bubble_sort(lb)


# 插入排序
# 主要思想是每次取一个列表元素与列表中已经排序好的列表段进行比较，然后插入从而得到新的排序好的列表段，最终获得排序好的列表。


def insert_sort(lists):
    count = len(lists)
    for post in range(1, count):
        key = lists[post]
        pre = post - 1
        while pre >= 0:
            if lists[pre] > key:
                lists[pre], lists[pre + 1] = key, lists[pre]
            pre -= 1
    return lists


a = get_random_number(10)
b = a[:]
print "排序之前:", a
print "插入排序之后:", insert_sort(b)
