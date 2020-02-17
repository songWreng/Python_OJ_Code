# coding=ANSI
from collections import deque

def solve23(p):
	q = deque()
	plen = len(p)
	cur = 0
	pre = None
	while not (len(q) == 0 and cur == None):
		if cur != None and cur < plen and p[cur] != '#':
			while cur < plen and p[cur] != '#':
				q.append(cur)
				cur = 2 * cur + 1
			if cur >= plen:
				cur = None
		else:
			tmp = q[-1]
			j = 2*tmp + 2
			if j == pre or j>= plen or p[j] == '#':
				print(p[tmp])
				pre = tmp
				q.pop()
				cur = None
			else:
				cur = j
	pass

p = input().split()
if p[0] != '#':
	solve23(p)
