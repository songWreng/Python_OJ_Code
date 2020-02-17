# coding=ANSI
# Ğ¡ÇàÍÜÌøÌ¨½×
def solve07():
	n = int(input())
	if n == 1:
		print(1)
	elif n == 2:
		print(2)
	else:
		p = [-1]*n
		p[0:2] = (1, 2)
		print(helpSolve07(n, p))
def helpSolve07(n, p):
	if p[n - 1] == -1:
		p[n - 1] = helpSolve07(n - 1, p) + helpSolve07(n - 2, p)
	return p[n - 1]

solve07()

