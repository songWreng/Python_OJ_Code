# coding=ANSI
'''
题目描述：
给定一个正整数N，返回N的二进制中两个连续的1之间的最长距离。如果不存在两个连续的1，则返回0
两个相邻的1的距离为1，像101中1的距离为2，依次类推
样例：
22 => 2
 8 => 0
解：
22 = 10110，8 = 1000
'''
def solve13(n):
	maxi = cur = 0
	mask = 0
	while n != 0:
		if n % 2 == 1:
			if mask != 0: cur += 1
			maxi = max(maxi, cur)
			cur = 0
			mask = 1
		elif n % 2 == 0 and mask == 1:
			cur += 1
		n //= 2
	print(maxi)
	pass
    
solve13(int(input()))  