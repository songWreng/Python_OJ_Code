# coding=ANSI
# Á´±í×ªÖÃ
def solve11():
	n = int(input())
	p = [int(b) for b in input().split()]
	helpSolve11(p, 0, n - 1)
	for i in p: print(i)
	pass

def helpSolve11(p, left, right):
	if left < right:
		p[left], p[right] = p[right], p[left]
		helpSolve11(p, left + 1, right - 1)
solve11()
