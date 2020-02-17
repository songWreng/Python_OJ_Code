from collections import deque
def solve():
    s = input().split()
    q = deque()
    if s[0] != '#':
        q.append(0)
    while len(q) != 0:
        # 出栈，输出，右子树入栈，再左子树入栈
        i = q.pop()
        print(s[i])
        if 2*i + 2 < len(s) and s[2*i + 2] != '#':
            q.append(2*i + 2)
        if 2*i + 1 < len(s) and s[2*i + 1] != '#':
            q.append(2*i + 1)
        
solve()

