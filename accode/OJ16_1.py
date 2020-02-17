'''
输入：数组p
输出：子数组满足元素之和等于数组和的一半
'''

def solve(p, aim, i, q):
    num = 0
    if aim == 0:
        print(q)
        num += 1
        return num
    elif i < len(p):
        # 对于p[i]，存在两种选择：要么选，要么不选
        # Case 1:选择
        if aim >= p[i]: 
            q.append(p[i])
            num += solve(p, aim - p[i], i + 1, q)
            del q[-1] # 复原q，将加入的p[i]删除
        # Case2: 不选
        num += solve(p, aim, i + 1, q)
    return num

p = list(map(int, input().split()))

aim = sum(p) // 2
q = []

m = solve(p, aim, 0, q)
if m == 0:
    print("False")
else:
    print("True")

