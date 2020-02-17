# coding=ANSI
# Hash表应用: 求同一条直线上的点的数量
h = [None] * 10 # Hash表
mah = [0] * 10  # 记录下标冲突的个数
n = int(input())
while n > 0:
	p = [int(b) for b in input().split()]
	k = p[1] // p[0] # 斜率关键字
	i = k % 10
	while h[i] != None and h[i] != k:
		i += 1;
		if i >= 10 : i = 0
	if h[i] == None:
		h[i] = k
	mah[i] += 1 # 计数+1
	n -= 1

print(max(mah))



