# coding=utf-8
# __author__='wujide'

import json

# dumps, loads
dic = {'age': 23, 'job': 'student'}
dic_str = json.dumps(dic)
print(type(dic_str), dic_str)

dic_obj = json.loads(dic_str)
print(type(dic_obj), dic_obj)


# dump, load
class Person:
    def __init__(self, name, age, job):
        self.name = name
        self.age = age
        self.job = job

    def work(self):
        print(self.name, 'is working...')


def dict2person(dic):
    return Person(dic['name'], dic['age'], dic['job'])

aa = Person('Bob', 23, 'Student')
# print aa.__dict__
with open(r'../data/abc.json', 'w') as f:
    json.dump(aa, f, default=lambda obj: obj.__dict__)

with open('../data/abc.json', 'rb') as f:
    obj = json.load(f, object_hook=dict2person)
    print(obj.name, obj.age, obj.job)
    obj.work()