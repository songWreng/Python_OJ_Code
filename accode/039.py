def help_solve39(p, size, decision, cur):
    if cur <= size - 2:
        mini = 10000
        for i in range(size):
            if i in decision or i == 0:
                continue
            decision[cur] = i
            tmp = help_solve39(p, size, decision, cur + 1)
            decision[cur] = -1

            if mini > tmp: mini = tmp
        return mini
    else:
        decision[cur] = 0
        sum = 0
        pre = 0
        for i in range(size):
            sum += p[pre][decision[i]]
            pre = decision[i]
        # print("D:",decision, end = " ")
        # print("sum =",sum)
        return sum

def solve39():
    n = int(input())
    p = []
    for i in range(n):
        p.append(list(map(int, input().split(','))))
    decision = [-1]*n
    r = help_solve39(p, n, decision, 0)
    print(r)
    # print(p)
solve39()