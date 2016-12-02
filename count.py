#encoding:utf-8

str = raw_input("input a string:\n")

letter = 0
space = 0
digit = 0
other = 0

for c in str:
	if c.isalpha():
		letter += 1
	elif c.isspace():
		space += 1
	elif c.isdigit():
		digit += 1
	else:
		other += 1
print 'char = %d\nspace = %d\ndigit = %d\nother = %d' % (letter, space, digit, other)