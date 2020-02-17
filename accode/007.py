# coding=ANSI
# 递归求最大公约数
def solve08():
	n = int(input())
	while n > 0:
		p = [int(a) for a in input().split()]
		helpSolve08(p[0], p[1])
		n -= 1
	pass

def helpSolve08(m, n):	
	if (m % n == 0):
		print(n)
	else:
		helpSolve08(n, m % n)
	pass
    
solve08()