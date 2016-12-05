#encoding:utf-8

# 题目：暂停一秒输出。
import time

print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
time.sleep(1)
print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

d = {1: 'a', 2: 'b'}
for k, v in dict.items(d):
	print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
	print k, v
	time.sleep(1)
