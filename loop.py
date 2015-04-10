count = 0
while (count < 9):
    print 'The count is:', count
    count = count + 1

print 'wenjifei youjichu'


count = 0
while count < 5:
   print 'wenjifei youjichu'
   count = count + 1
else:
   print 'wenjifei feichang youjichu'

del count

for letter in 'wenjifei youjichu':
    print 'Current letter: ', letter

list = [ 'wen', 'ji', 'fei', 'you', 'ji', 'chu' ]

for word in list:
    print 'Current word: ', word

for index in range(len(list)):
    print 'Current word: ', list[index]

del list

count = 0
for num in range(2, 100):
    for i in range(2, num):
        if num%i == 0:
            break
    else:
        print num, '\n'
        count += 1

print count

del count

