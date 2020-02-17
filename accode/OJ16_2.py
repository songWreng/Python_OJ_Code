m = int(input())
p = []
for i in range(m):
	p.append(list(map(int, input().split(','))))
def solve(cur, marks, rem): 
	# marks[i] = 1 表示结点i在路径中
	# rem 表示已入选结点的个数，即marks中的1的个数
	# cur 起点，从未入选的结点中选择其中一个i
	if rem == m - 1:
		return p[cur][0]
	waylen = 0
	mini = 65535
	for i in range(1, m):
		if marks[i] == 1: continue
		marks[i] = 1
		tmp = p[cur][i] + solve(i, marks.copy(), rem + 1)
		waylen += tmp
		mini = min(mini, waylen) 
		# print(cur, i, mini, waylen)
		marks[i] = 0 
		waylen -= tmp # 恢复很关键
		
	return  mini

marks = [0]*m
print(solve(0, marks, 0))