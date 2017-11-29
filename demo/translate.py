# coding=utf-8
# __author__='Administrator'


from string import maketrans

table = maketrans('cs', 'kz')
print len(table)
print table[97:123]

s = 'this is an incredible test'

print s.translate(table)
print "s:", s

print s.translate(table, ' ')


