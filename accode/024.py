# coding=ANSI
'''
思路：
	根据查找二叉树的特点，可以唯一确定一个树，也就是说他们的完全二叉树的序号相同；
所以可以考虑计算原序列的完全二叉树的序号，接下来处理测试序列；
	如果是同一棵树的必要条件是：序列的长度相同！长度不同一定返回False！
	逐个计算测试序列的完全二插树的序号，存在两种情况：
		某个结点的序号不在原来序列的范围；
		某个序号对应的值不同；
上面两种情况可以判定为False。
'''
def solve24():
	N = int(input())
	p = [int(b) for b in input()]
	dp = {0:p[0]}
	for a in p[1:]:
		i = 0
		while i in dp:
			if a < dp[i]:
				i = 2*i + 1
			elif a > dp[i]:
				i = 2*i + 2
		dp[i] = a

	while N > 0:
		q = [int(b) for b in input()]
		if len(q) == len(p):
			flag = True
			dq = {0:q[0]}
			for a in q[1:]:
				i = 0
				while i in dq:
					if a < dq[i]:
						i = 2*i + 1
					elif a > dq[i]:
						i = 2*i + 2
				dq[i] = a

				if (i not in dp) or dp[i] != a:
					flag = False
					break
		else:
			flag = False

		if flag == True:
			print("YES")
		else:
			print("NO")
		N -= 1

	pass # end function

solve24()

