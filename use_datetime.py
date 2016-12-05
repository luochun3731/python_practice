#encoding:utf-8

# 题目：输出指定格式的日期。
import datetime

'''
__name__ 是当前模块名，当模块被直接运行时模块名为 __main__ 。
这句话的意思就是，当模块被直接运行时，代码将被运行，当模块是被导入时，代码不被运行。
'''
if __name__ == '__main__':
	# 输出今日日期，格式为 dd/mm/yyyy。更多选项可以查看 strftime() 方法
    print datetime.date.today().strftime('%d/%m/%Y')

    # 创建日期对象
    myBirthDate = datetime.date(1987, 2, 18)
    print myBirthDate.strftime('%d-%m-%Y')
    
    # 查看对象所有方法
    print dir(myBirthDate)
    
    myBirthDateNextDay = myBirthDate + datetime.timedelta(days=1)
    print myBirthDateNextDay.strftime('%Y-%m-%d')

    myFirstBirthday = myBirthDate.replace(year=myBirthDate.year + 1)
    print myFirstBirthday.strftime('%Y-%m-%d')