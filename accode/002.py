# coding=ANSI
# ʮ����ת������
a = int(input())
p = []
top = 0
while a != 0:
	p.append(a % 2)
	top += 1
	a = a // 2

for a in reversed(p):
	print(a, end="")
print()

  