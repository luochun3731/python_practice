# encoding:utf-8

'''
4.编写一个签名函数：
       charcount(text)
这个函数应当返回一个带有28键的字典，28键是'a','b',·······,'z',
外加'whitespace'和'others'。对于text中每一个小写字符，如果字符是字母，
增加其对应的键的数量；如果该字符是空格，增加'whitespace'键的数量；
否则，增加'other'键的数量。例如，如下调用：stats= charcount('Exceedingly Edible')
将意味着，stats是一个带有如下内容的字典：
{'whitespase': 1, 'other': 0, 'a': 0, 'c': 1, 'b': 1, 'e': 5, 'd': 2, 'g': 1, 'f': 0,
 'i': 2, 'h': 0, 'k': 0, 'j': 0, 'm': 0, 'l': 2, 'o': 0, 'n': 1, 'q': 0, 'p': 0, 's': 0,
 'r': 0, 'u': 0, 't': 0, 'w': 0, 'v': 0, 'y': 1, 'x': 1, 'z': 0}
使用一个字典和一个for循环，应该可以用12行左右的代码完成。
'''


def charcount(text):
    dic = {'whitespase': 0, 'other': 0, 'a': 0, 'c': 0, 'b': 0, 'e': 0, 'd': 0, 'g': 0,
           'f': 0, 'i': 0, 'h': 0, 'k': 0, 'j': 0, 'm': 0, 'l': 0, 'o': 0, 'n': 0, 'q': 0,
           'p': 0, 's': 0, 'r': 0, 'u': 0, 't': 0, 'w': 0, 'v': 0, 'y': 0, 'x': 0, 'z': 0}
    for i in range(len(text)):
        for j in dic.keys():
            if text[i].lower() == j:
                dic[j] += 1
            elif text[i].isspace() and j == 'whitespase':
                dic['whitespase'] += 1
            elif text[i].lower() not in dic.keys() and not text[i].isspace() and j == 'other':
                dic['other'] += 1
    return dic.items()

print charcount('Exceedingly Edible')
