# coding=utf-8
# __author__='wujide'

import re

# match 匹配
reg = r'\d{3}\-\d{3,8}'
tel = '0021-123456789'
if re.match(reg, tel):
    print 'It\'s matched !'
else:
    print "No"

# search 匹配
reg_search = r'\d{3}\-\d{3,8}'
if re.search(reg_search, tel):
    print 'It\'s searched !'
else:
    print "No"

# split 切分
s = 'a, b   c;; d'
print "s_split:", re.split(r'[\s,;]+', s)


# group 分组
reg_1 = r'(\d{3})-(\d{3,8})$'
txt = '123-456789'
m = re.match(reg_1, txt)
print "groups:", m.groups()
print "group():", m.group()
print "group(1):", m.group(1)
print "group(2):", m.group(2)

# findall
# tel_find: ['(021)88776543', '010-55667890', '02584533622', '057184720483', '83792274']
reg_2 = r"\(?0\d{2,3}[) -]?\d{7,8}|\d{7,8}"
txt_2 = '(021)88776543 010-55667890 02584533622 057184720483 83792274'
tel_find = re.findall(reg_2, txt_2)
if tel_find:
    print "tel_find:", tel_find
else:
    print "nothing find"

# email_find: ['test@test.com ', 'test.test@test.com ', '_123@123.com ', '3434@123.456.cn ', '456@456.me ']
email = 'test@test.com test.test@test.com _123@123.com 3434@123.456.cn 456@456.me '
reg_3 = r'\w+[\w.]*@[\w.]+\.\w+ '
email_find = re.findall(reg_3, email)
if email_find:
    print "email_find:", email_find
else:
    print "no email found"

# finditer() 返回的是迭代器
# result：hello world
print "fi.group(): "
for fi in re.finditer('\w+', 'hello, world!'):
    print fi.group(),
print '\n'

# start([group])
email_bef_rm = "tony@tiremove_thisger.net"
m = re.search("remove_this", email_bef_rm)
email_after_rm = email_bef_rm[:m.start()] + email_bef_rm[m.end():]
print "email_after_rm:", email_after_rm


# 先编译
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
print re_telephone.match('012-34567').group()
print '\n'

# re.I
re_str = re.compile(r'\w+ab', re.I)
for str_ignore in re_str.finditer('aab,Aab,bAB,bAc'):
    print str_ignore.group(),
print '\n'

# sub & subn
p = re.compile('(one|two|three)')
print p.sub('num', 'one word two words three words apple', 2)
print p.subn('num', 'one word two words three words apple', 2)
