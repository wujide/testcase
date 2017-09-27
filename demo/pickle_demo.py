# coding=utf-8
# __author__='wujide'
import pickle


class Person:
    def __init__(self, name, age, job):
        self.name = name
        self.age = age
        self.job = job

    def work(self):
        print(self.name, 'is working...')

# 将实例存储在变量中，当然也能存在文件中
a_person = Person('abc', 22, 'waiter')
person_abc = pickle.dumps(a_person)
p = pickle.loads(person_abc)
p.work()
# 将类本身存储在变量中，loads的时候返回类本身，而非它的一个实例
class_Person = pickle.dumps(Person)
Person = pickle.loads(class_Person)
p = Person('Bob', 23, 'Student')
p.work()

# 下面这个例子演示的就是将类存储在文件中
# 序列化
with open('../data/person.pkl', 'wb') as f:
    pickle.dump(Person, f)
# 反序列化
with open('../data/person.pkl', 'rb') as f:
    Person = pickle.load(f)
    aa = Person('gg', 23, '6')
    aa.work()