# encoding:utf-8

'''
字符串类型的数字和数字类型相加会出现TypeError的异常，
捕获这个异常并尝试修复这个异常，在输入数字和字符串类型的数字时能输出结果
例如在运行程序时可得出下面的结果：
输入一个数字类型的数1                          #键盘输入1
输入一个字符串类型的数字'3'                    #键盘输入‘1’
1与3的和是4                                    #运行结果
'''


try:
    var_int = input('please input a int number: ')
    var_str = input('please input a string number: ')
    sum = var_int + var_str
    print sum
except TypeError as reason:
    print 'ERROR:', reason
    sum = var_int + int(var_str)
    print 'sum of input: ', sum
finally:
    print 'finally'
