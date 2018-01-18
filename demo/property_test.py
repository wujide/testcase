# coding=utf-8
# __author__='wujide'


class Students(object):
    def __init__(self):
        self._score = None

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        # return 2014 - self._birth
        return self._age

    @age.setter
    def age(self, value):
        self._age = value

s = Students()
s.score = 99
print "s.score:", s.score

''''
s.birth = 2000
print "s.age:", s.age

'''

s.age = 23
print "s.age:", s.age
