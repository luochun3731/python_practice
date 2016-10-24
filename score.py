#encoding:utf-8

while True:
    score = raw_input('please input a score: ')
    if score.lower() == 'q':
        break
    elif not score.isdigit():
        print 'please input a valid score! '
        continue
    else:
        score = int(score)
        if 100 >= score >= 90:
            print 'A'
        elif 90 >= score >= 80:
            print 'B'
        elif 80 >= score >= 60:
            print 'C'
        elif 60 >= score >= 0:
            print 'D'
