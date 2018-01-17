# coding=utf-8
# __author__='wujide'


def count():
    fs = []
    for i in range(1, 4):
       def f(j):
            def g():
               return j*j
            return g
       fs.append(f(i))
    return fs

f1, f2, f3 = count()
print f1(), f2(), f3()


def count_contrast():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i
        fs.append(f)
    return fs


f4, f5, f6 = count_contrast()
print f4(), f5(), f6()
