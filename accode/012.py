# coding=ANSI
# �ݹ�ȫ����ʵ��
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
              


# ���Ӽ򵥵�ʵ��
def persum(mark, p, cur, psize):
	pass
	if cur >= psize:
		print(p)
		return;

	for i in range(psize):
		if mark[i] == 1: # ���
			continue
		p[cur] = i + 1
		mark[i] = 1 # ���Ϊ1
		persum(mark, p, cur + 1, psize)
		mark[i] = 0 # ������
		
def solve12_v2():
	n = int(input())
	mark = [0]*n
	p = [0]*n
	persum(mark, p, 0, n)


#solve12()
solve12_v2()


