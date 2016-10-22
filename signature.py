#encoding:utf-8

'''
1.编写一个签名函数：  valid(text,chars='ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
这个函数应当返回一个（或者是空的）字符串，它是只含有char字符的text的副本。
例如
        valid('Barking!')                                 #Returns 'B'
        valid('KL754','0123456789')                       #Returns '754'
        valid('BEAN','abcdefghijklmnopqrstuvwxyz')        #Returns ''
该函数应该在6行左右完成，可以使用一个for循环和一个if语句。
'''


def valid(text, chars='ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'):
    str = ''
    for i in range(len(text)):
        if text[i] in chars:
            str += text[i]
    return str

print valid('Barking!')
print valid('KL754', '0123456789')
print valid('BEAN', 'abcdefghijklmnopqrstuvwxyz')
