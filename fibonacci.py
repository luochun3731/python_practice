# encoding:utf-8

'''
3.利用递归写斐波那契数列的函数f(n)。
注：(斐波那契数列：1,1,2,3,5,8,13,21,34,55,·······)
解析：
f(1) = 1
f(2) = 1
f(3) = f(1) + f(2)
.....
f(n) = f(n-2) + f(n-1)
'''

def f(n):
    if 0 <= n <= 1:
        return n
    elif n >= 2:
        return f(n-2) + f(n-1)
    else:
        return 'please input a positive integer!'

print f(-1)

for i in range(1, 11):
    print f(i),
