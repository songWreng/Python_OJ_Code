# coding=GBK
# 升温倒计时
import random
def solve016(p):
	psize = len(p)
	ans = [0] * psize
	for i in range(psize - 1):
		k = i + 1
		while k < psize and p[i] >= p[k]: k += 1
		
		if k < psize and p[k] > p[i]:
			ans[i] = k - i
	print(ans)

def main():
	n = 7
	#p = [int(b) for b in input().split()]
	while n:
		n -= 1
		maxi = random.randint(1, 20)
		p = [random.randint(-20, 45) for a in range(maxi)]
		print(p)
		solve016(p)
		print()
main()