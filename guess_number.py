#encoding:utf-8
# 1.将猜字游戏写完整,运行出结果.

import random

x = random.randint(10, 30)
i = input('Please input a number between 10 and 30: ')

while True:
    if i < x:
        i = input('too samll, try again: ')  
    elif i == x:
    	print('you are lucky')
    	break
    else:
    	i = input('too large, try again: ')  
    	
