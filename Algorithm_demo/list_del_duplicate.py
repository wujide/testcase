# coding=utf-8
# __author__='wujide'

#  请写出一段Python代码实现删除一个list里面的重复元素

a = [1, 2, 4, 2, 4, 5, 6, 5, 7, 8, 9, 0]

# 方法1
b = set(a)
print list(b)

# 方法2
c = {}
c = c.fromkeys(a)
d = list(c.keys())
print d


# 冒泡排序

def bubbleSort(nums):
    for i in range(len(nums)-1):    # 这个循环负责设置冒泡排序进行的次数
        for j in range(len(nums)-i-1):  # ｊ为列表下标
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums

nums = [5,2,45,6,8,2,1]

print bubbleSort(nums)