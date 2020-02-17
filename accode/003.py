# coding=ANSI
# ·ê7¾Í³ö
n = int(input())
p = [1]*n
cnt = n
i = j = 0
while cnt > 0:
	if (p[j] == 1):
		i += 1
		if i % 7 == 0:
			p[j] = 0
			cnt -= 1
			print(j + 1)
	j += 1
	if (j >= n): j = 0