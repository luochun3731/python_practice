#encoding:utf-8

# 生成一个50以内的能被5整除的列表

five = []
for i in range(51):
    if i % 5 == 0:
        five.append(i)
print five
print len(five)
