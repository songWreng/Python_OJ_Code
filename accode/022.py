# coding=utf-8
from collections import deque
def HelpSolve22(stk):
	if len(stk) > 0:
		#print(stk)
		curTree = stk.popleft()
		root = curTree[1].index(curTree[0][0])
		print(curTree[1][root], end=" ")
		if root >= 1:
			LeftTree = [None]*2
			LeftTree[0] = curTree[0][1:root+1]
			LeftTree[1] = curTree[1][0:root-1+1]
			#print("L:", LeftTree)
			if LeftTree[0] != []:
				stk.append(LeftTree)
		if root + 1 <= len(curTree[0]):
			RightTree = [None]*2
			RightTree[0] = curTree[0][root + 1:]
			RightTree[1] = curTree[1][root + 1:]
			#print("R:", RightTree)
			if RightTree[0] != []:
				stk.append(RightTree)
		HelpSolve22(stk)

def solve22(pre, cur):
	stk = deque()
	stk.append([pre, cur])
	HelpSolve22(stk)
	print()

pre = [b for b in input().split()]
cur = [b for b in input().split()]
solve22(pre, cur)
