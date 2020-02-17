# coding=ANSI
# 归并排序
def merg(p, left, mid, right, q):
	i = left; j = mid + 1
	m = left
	while i <= mid and j <= right:
		if p[i] < p[j]:
			q[m] = p[i]
			i += 1
		else:
			q[m] = p[j]
			j += 1
		m += 1
	while i <= mid:
		q[m] = p[i]
		i += 1;
		m += 1;
	while j <= right:
		q[m] = p[j]
		j += 1
		m += 1
	for k in range(left, right + 1):
		p[k] = q[k]


def sortByMerg(p, n):
	q = [0] * n
	m = 1
	while m < n:
		k = 2*m
		for i in range(0, n, k):
			right = i + k - 1
			mid = i + m - 1
			if right >= n:
				right = n - 1
			if mid < right:
				merg(p, i, mid, right, q)
		m = k
'''递归版本的如下：
# 后序遍历（自底向上）
def helpSortByMerg(p, left, right, q):
	if left == right:
		return
	mid = (left + right) // 2
	helpSortByMerg(p, left, mid, q)
	helpSortByMerg(p, mid +1, right, q)
	merg(p, left, mid, right, q)

def sortByMerg(p, n):
	q = [0]*n
	helpSortByMerg(p, 0, n - 1, q)
	pass
'''
		
def main():
	n = int(input())
	while n > 0:
		tmp = input()
		p = [int(b) for b in tmp.split()]
		sortByMerg(p, len(p))
		print(p)
		n -= 1

          
main()

  