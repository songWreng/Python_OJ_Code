'''
数据表示一二叉树
L R的值
输出二叉树中大于等于L小于等于R的结点的和。
'''
p = [int(b) for b in input().split()]
[L, R] = [int(b) for b in input().split()]
sum = 0
for a in p:
    if a >= L and a <= R:
        sum += a
print(sum)

