# coding=ANSI
# À¨ºÅÆ¥Åä
def solve09():
	dict = {'}':'{', ']':'[', ')':'('}
	str = input()
	p = []
	top = 0
	for s in str:
		if s == '{' or s == '[' or s == '(':
			top += 1
			p.append(s)
		elif s == '}' or s == ']' or s == ')':
			if (top >= 0 and dict[s] == p[top - 1]):
				top -= 1
				del p[top]
			else: break
	if len(p) == 0:
		print("True")
	else:
		print("False")
solve09()

  