# coding=GBK
# Hash应用 数宝石
def hashf(c):
	return ord(c) % 10

str = input()
h = [None] * 10
cnt = 0

for s in str:
	i = hashf(s)
	while h[i] != None:
		i = (i + 1) % 10
	h[i] = s

str = input()
for s in str:
	i = hashf(s)
	while h[i] != None and h[i] != s:
		i = (i + 1) % 10
	if h[i] == s:
		cnt += 1
print(cnt)


  