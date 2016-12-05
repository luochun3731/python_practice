#encoding:utf-8

# 题目：将所输入的字符串以相反顺序打印出来。

# 通过索引的方法
def reverse1(str):
	output = str[::-1]
	return output

# 通过列表
def reverse2(str):
	order = []
	for i in str:
		order.append(i)
	order.reverse()
	return ''.join(order)

print reverse1('dsfgf')