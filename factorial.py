# encoding:utf-8


# 递归求阶乘
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return factorial(n - 1)*n
print factorial(5)


# 递归求正整数之和
def sum(x):
    if x == 1:
        return 1
    else:
        return sum(x - 1) + x
print sum(4)


# 求1-10的阶乘值之和
def sum_of_factorial(m):
    sum = 0
    for i in range(1, m + 1):
        sum += factorial(i)
    return sum
print sum_of_factorial(10)
