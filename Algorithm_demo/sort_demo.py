# coding=utf-8
# __author__='wujide'

from get_random_list import get_random_list


# 冒泡排序
# 原理是对序列进行遍历，遍历过程中如果发现相邻两个元素，左边的元素大于右边，则进行交换，
# 一次遍历之后最大的元素被移动到对尾，然后进行第二次遍历，直到队列有序。
def bubble_sort(nums):
    for i in range((len(nums)-1)):
        for j in range(len(nums)-1-i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums


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


# 快速排序
# 实现方法是设置两个游标，一个从前往后，一个从后往前，如果左侧游标所指数据大于右侧，两数据进行交换，直到两个游标指向同一数据，则第一趟遍历结束。结束时游标所在数据，左侧都比其小，右侧都比其大。
def quick_sort(lq, start, end):
    i = start
    j = end
    if i >= j:
        return la
    key = lq[i]  # 设置基准数
    while i < j:
        # 如果列表后边的数,比基准数大或相等,则前移一位直到有比基准数小的数出现
        while i < j and lq[j] >= key:
            j = j - 1
        # 如找到,则把第j个元素赋值给元素i,此时表中i,j个元素相等
        lq[i] = lq[j]
        # 同样的方式比较前半区
        while i < j and lq[i] <= key:
            i = i + 1
        lq[j] = lq[i]
    # 做完第一轮比较之后,列表被分成了两个半区,并且i=j,需要将这个数设置回base
    lq[i] = key
    # 递归前后半区
    quick_sort(lq, start, i-1)
    quick_sort(lq, j+1, end)
    return lq


# 实现方法2
def qsort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        return qsort([x for x in arr[1:] if x < pivot]) + \
               [pivot] + \
               qsort([x for x in arr[1:] if x >= pivot])


# 选择排序
# 选择排序的原理是是先找到起始数组中最小的元素，将它交换到i=0；然后寻找剩下元素中最小的元素，将它交换到i=1的位置……
# 直到找到第二大的元素，将它交换到n-2的位置。这时，整个数组的排序完成。
def select_sort(ls):
    for i in range(len(ls)):
        min_index = i
        for j in range(i, len(ls)):
            if ls[j] < ls[min_index]:
                min_index = j
        ls[i], ls[min_index] = ls[min_index], ls[i]

    return ls


if __name__ == '__main__':
    la = get_random_list(10)
    lb = la[:]
    print "排序前：", la
    print "冒泡排序后:", bubble_sort(lb)

    lc = la[:]
    print "插入排序后:", insert_sort(lc)

    ld = la[:]
    ld_cp = la[:]
    print "快速排序后:", quick_sort(ld, 0, len(ld)-1)
    print "快速排序2后:", qsort(ld_cp)

    le = la[:]
    print "选择排序后:", select_sort(le)

