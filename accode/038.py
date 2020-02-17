def help_solve38(p, size, decision, cur):
    if cur < size:
        mini = 100000
        way = []
        for i in range(size):
            if i not in decision:
                decision[cur] = i
                [tmp, tmpway] = help_solve38(p, size, decision, cur + 1)
                if mini > tmp:
                    way = tmpway
                    mini = tmp
                decision[cur] = -1
        return [mini, way]
    else:
        sum = 0
        q = [0]*size
        for i in range(size):
            sum += p[i][decision[i]]
            q[i] = decision[i] + 1
        # print("sum =", sum, "D:", decision)
        return [sum, q]

def solve38():
    n = int(input())
    p = []
    for i in range(n):
        p.append(list(map(int, input().split())))
    decision = [-1]*n
    [r, p] = help_solve38(p, n, decision, 0)
    print(r)
    print(p)
solve38()