# coding=GBK
from collections import deque
class TreeNode:
	def __init__(self, e = '#'):
		self.value = e
		self.left = None
		self.right = None
	
def bt_insert(node, e):
	if (node.left == None and e < node.value):
		node.left = TreeNode(e)
		pass
	elif node.right == None and e > node.value:
		node.right = TreeNode(e)
	else:
		if e < node.value:
			bt_insert(node.left, e)
		elif e > node.value:
			bt_insert(node.right, e)


def DLR_Non_recursion(tree, str): # 最简单的一个
	q = deque()
	cur = tree
	q.append(cur)
	i = 0
	while len(q):
		cur = q.pop()
		#print(cur.value, end = " ")
		str[i] = cur.value
		i += 1
		if cur.right != None:
			q.append(cur.right)
		if cur.left != None:
			q.append(cur.left)
	#print()
	pass

def LDR_Non_recursion(tree, str):
	q = deque()
	cur = tree
	i = 0
	while not (cur == None and len(q) == 0):
		if cur != None:        # 树非空，入栈！继续找 
			while cur != None:
				q.append(cur)
				cur = cur.left
		else:                       # 若是空树，则弹出
			cur = q.pop()
			#print(cur.value, end = " ")
			str[i] = cur.value
			i += 1
			cur = cur.right
	#print()
	pass

def makeTree(p):
	tree = TreeNode(p[0])
	for d in p[1:]:
		bt_insert(tree, d)
	return tree

def main():
	n = int(input())
	s = input()
	ls = len(s)
	Dp = [[None]*ls, [None]*ls]
	D = makeTree(s)
	DLR_Non_recursion(D, Dp[0])
	LDR_Non_recursion(D, Dp[1])
	while n > 0:
		s = input()
		ls = len(s)
		Tp = [[None]*ls, [None]*ls]
		T = makeTree(s)
		DLR_Non_recursion(T, Tp[0])
		LDR_Non_recursion(T, Tp[1])
		if Dp == Tp:
			print("Yes")
		else:
			print("No")
		n -= 1
	pass


main()