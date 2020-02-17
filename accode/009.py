# coding=ANSI
# ¶ş·Ö²éÕÒ
def solve10():
	n = int(input())
	datas = []
	for i in range(n):
		datas.append([int(b) for b in input().split(',')])
	for i in range(n):
		print(helpSolve10(datas[i], int(input())))

def helpSolve10(p, target):
	left = 0; right = len(p) - 1
	while left <= right:
		mid = (left + right) // 2
		if target < p[mid]: right = mid - 1
		elif target > p[mid]: left = mid + 1
		else:
			while (mid >= 1 and p[mid - 1] == target): 	mid -= 1
			return mid
	return -1
              
              
solve10()