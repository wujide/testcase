# coding=utf-8
# __author__='Administrator'


class Students(object):
    def get_score(self):
        print self._score

    def set_score(self, score):
        if not isinstance(score, int):
            raise ValueError('score must be integer')
        if score > 100 or score < 0:
            raise ValueError('score must between 0 - 100')
        self._score = score

s = Students()
s.set_score(99)
s.get_score()



'''
class Field(object):

    _count = 0

    def __init__(self, **kw):
        self.name = kw.get('name', None)
        self._default = kw.get('default', None)
        self.primary_key = kw.get('primary_key', False)
        self.nullable = kw.get('nullable', False)
        self.updatable = kw.get('updatable', True)
        self.insertable = kw.get('insertable', True)
        self.ddl = kw.get('ddl', '')
        self._order = Field._count
        Field._count += 1

    @property
    def default(self):
        d = self._default
        return d() if callable(d) else d

    def __str__(self):
        s = ['<%s:%s,%s,default(%s),' % (self.__class__.__name__, self.name, self.ddl, self._default)]
        print s
        print self.nullable and s.append('N')
        print self.updatable and s.append('U')
        print self.insertable and s.append('I')
        s.append('>')
        print s
        print ''.join(s)

f = Field()
f.__str__()

'''
