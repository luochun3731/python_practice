#encoding:utf-8

# 输出九九乘法表

# i x j = i*j
for i in range(1, 10):
    for j in range(1, 10):
        if i >= j:
            print '%s x %s = %s ' % (j, i, i*j),
    print ''

print ''

for i in range(1, 10):
    for j in range(1, i+1):
        print '%s x %s = %s ' % (j, i, i*j),
    print ''
