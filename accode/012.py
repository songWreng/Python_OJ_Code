# coding=ANSI
# 递归全排列实现
def solve12():
	maxi = int(input())
	remain = list(range(1, maxi + 1))
	p = [0] * maxi
	helpSolve12(remain, p, 0)
	pass

def helpSolve12(remain, p, cur):
	if cur >= len(p):
		print(p)
	else:
		for i in range(len(remain)):
			p[cur] = remain[i]
			copyRemain = [a for a in remain]
			del copyRemain[i]
			helpSolve12(copyRemain, p, cur + 1)
              


# 各加简单的实现
def persum(mark, p, cur, psize):
	pass
	if cur >= psize:
		print(p)
		return;

	for i in range(psize):
		if mark[i] == 1: # 标记
			continue
		p[cur] = i + 1
		mark[i] = 1 # 标记为1
		persum(mark, p, cur + 1, psize)
		mark[i] = 0 # 清除标记
		
def solve12_v2():
	n = int(input())
	mark = [0]*n
	p = [0]*n
	persum(mark, p, 0, n)


#solve12()
solve12_v2()


