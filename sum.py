#encoding:utf-8

# 计算100以内所有整数和

sum = 0
for i in range(101):
    sum += i
print sum

sum1 = 0
x = 0
while 0 <= x <= 100:
    sum1 += x
    x += 1
print sum1
