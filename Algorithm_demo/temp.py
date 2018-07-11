# coding=utf-8
# __author__='wujide'


a = [1,2,4,2,4,5,7,10,5,5,7,8,9,0,3]

a.sort()
print(a)
last = a[-1]
for i in range(len(a)-2, -1, -1):
    if last == a[i]:
        del a[i]
    else:
        last = a[i]
print(a)

