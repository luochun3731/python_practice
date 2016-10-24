#encoding:utf-8
# 输出0-100中的所有偶数,并计算个数
### range method ###
print '### range method ###'
x = range(0, 101, 2)
print 'even numbers from 0 to 100:\n', x
print 'there are %s even numbers from 0 to 100\n' % len(x)

### for loop ###
print '### for loop ###'
count2 = 0
print 'even numbers from 0 to 100: '
for i in range(101):  # range(101)返回0-100
    if i % 2 == 0:
        print i,
        count2 += 1
print '\nthere are %s even numbers from 0 to 100\n' % count2

### while loop ###
print '### while loop ###'
count = 0
x = 100
print 'even numbers from 100 to 0:'
while x >= 0:
    print x,
    x -= 2
    count += 1
print '\nthere are %s even numbers from 0 to 100\n' % count

print '### while loop ###'
count1 = 0
x = 0
print 'even numbers from 0 to 100: '
while x <= 100:
    print x,
    x += 2
    count1 += 1
print '\nthere are %s even numbers from 0 to 100\n' % count1
