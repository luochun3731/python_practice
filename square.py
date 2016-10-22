# encoding:utf-8

'''
一个整数加上100或268后都是一个完全平方数，求此数
注：一个整数如果是另一个整数的完全平方，我们称
这个数是完全平方数， 如1,4,9,16,25...
'''

import math

for i in range(10000):
    x = int(math.sqrt(i + 100))
    y = int(math.sqrt(i + 268))
    if(x * x == i + 100) and (y * y == i + 268):
        print i

print ''

for x in range(1000):
    for y in range(1000):
        if x * x - 100 == y * y - 268:
            print x * x - 100
