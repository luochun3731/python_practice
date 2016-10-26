# encoding:utf-8


# 根据range()函数，创建一个对浮点数float进行操作的frange()函数
def frange(start, stop, inc):
    result = []
    while start < stop:
        result.append(start)
        start += inc
    return result

print frange(0, 6, 0.5)


# 创建一个与range()相同参数逻辑的frange()函数
def frange1(agr0, agr1=None, agr2=None):
    start = 0.0
    inc = 1.0
    if agr2 is not None:
        start = float(agr0)
        stop = agr1
        inc = agr2
    elif agr1 is not None:
        start = float(agr0)
        stop = agr1
    else:
        stop = agr0
    result = []
    while start < stop:
        result.append(start)
        start += inc
    return result

print frange1(5.0)
print frange1(2, 8)
print frange1(1, 20, 5)
