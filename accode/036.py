# 无限背包
"""
N 物品的个数
V 背包容量
c 重量
w 价格
"""
def solve():
	N = int(input())
	V = int(input())
	c = list(map(int, input().split()))
	w = list(map(int, input().split()))
	
	dp = [0] * (V + 1)
	for i in range(N):
		for j in range(c[i], V + 1):
			dp[j] = max(dp[j - c[i]] + w[i], dp[j])
	print(dp[V])
solve()