"""
01背包问题

输入：
物品的个数n
背包的容量v
n个商品的重量
n个商品的价值

输出：
输出背包的最高价值
输出选中物品的序号(从小到大)
"""
def solve():
    n = int(input())
    v = int(input())

    weights = list(map(int, input().split()))
    values = list(map(int, input().split()))
    
    dp = []
    for i in range(n):
        dp.append([0]*(v + 1))
    

    for i in range(n):
        for j in range(v + 1):
            if i == 0:
                if j >= weights[i]:
                    dp[i][j] = values[i]    
            else:
                if j >= weights[i]:
                    dp[i][j] = max(dp[i - 1][j], \
                        dp[i - 1][j -weights[i]] + values[i])
                else:
                    dp[i][j] = dp[i - 1][j]                      
    
    print(dp[-1][-1])

    j = v
    ans = []
    for i in range(n - 1, 0, -1):
        if dp[i][j] != dp[i - 1][j]:
            ans.append(i + 1)
            j -= weights[i]
    if dp[0][j] != 0:
        ans.append(1)

    for a in reversed(ans):
        print(a, end = " ")
    print()           

solve()
