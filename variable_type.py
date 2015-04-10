#coding=utf-8
raw_input('\n\nPlease enter to exit')
print 'wenjifei youjichu'

a = b = c = 1
print a, b, c
a, b, c = 1, 2, 'python'
print a, b, c

del a

c = 3
a = complex(b, c)
print a

del a, b, c
s = 'wenjifei youjichu'
print s[0:8], s[-8:]


print s[0], s[-8:], s * 2, s[0:8] + s[-8:]

del s

list = [ 'wen', 'ji', 'fei', 'you', 'ji', 'chu' ]
tinylist = [ 'you', 'ji', 'chu' ]

print list
print list[0]
print list[1:3]
print list[2:]
print tinylist * 2
print list + tinylist

del list, tinylist

tuple = ( 'abcd', 786, 2.23, 'youjichu' )
tinytuple = ( 'wenjifei', 'youjichu' )

print tuple
print tuple[0]
print tuple[1:3]
print tuple[2:]
print tinytuple * 2
print tuple + tinytuple

del tuple, tinytuple

dict = {}
dict['wenjifei'] = 'This is youjichu'
dict[2] = 'This is two'

tinydict = {'name': 'wenjifei', 'job': 'zhujiao'}

print dict['wenjifei']
print dict[2]
print tinydict
print tinydict.keys()
print tinydict.values()

del dict, tinydict


