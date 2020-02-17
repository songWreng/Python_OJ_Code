'''
输入：完全二叉树顺序输入
输出：判断是否为AVL树，是True，否False
题目巨坑：
    1. 得判断这是一棵查找树，结点值的大小进行判断！没有说是结点的值是整数！
'''
def help_solve(p, cur):
    if cur < len(p) and p[cur] != '#':
        left = help_solve(p, 2*cur+1)
        right= help_solve(p, 2*cur+2)
        if left[1] and right[1] and abs(left[0] - right[0]) <= 1 and isBTree(cur, p):
            return [max(left[0], right[0])+1, True]
        else:
            return [-1, False]
    else:
        return [-1, True]
        
def isBTree(cur, p):
    a = b = True
    if 2*cur+1 < len(p) and p[2*cur+1] != '#':
        a =  (int(p[2*cur+1]) < int(p[cur]))
    if 2*cur+2 < len(p) and p[2*cur+2] != '#':
        b = (int(p[cur]) < int(p[2*cur+2]))
    return a and b
def solve3():
    p = input().split()
    print(help_solve(p, 0)[1])
# solve3()
'''
以上即是答案
=========================================
'''
def solve():
    p = [
        '1 2 3 # 5 6 # # # 10 # # 13',
        # '#',
        '1 2 3 4 5 6 7 8 9',
        '10 2 # 30 # # # 40',
        '1 2 3 4 5 6 7 # # 8 # # # 9',
        # '# # # # #',
        '1 2 3 4 # # 5',
        '40 20 50 10 # # 60'
    ]
    for r in p:
        q = r.split()
        print(q)
        print(help_solve(q, 0)[1])
    # p = input().split()
    # if p[0] == '#':
    #     print("False")
    # else:
    #     print(help_solve(p, 0)[1])


def GetDepth(p, cur, d):
    if cur < len(p) and p[cur] != '#':
        if d[cur] == -1:
            d[cur] = max(GetDepth(p, 2*cur+1, d), GetDepth(p, 2*cur+2, d)) + 1
        return d[cur]
    else:
        return -1

def isOK(ll, dd, rr, p):
    if ll >= len(p): l = '#'
    else: l = p[ll]
    if rr >= len(p): r = '#'
    else: r = p[rr]
    d = p[dd]
    if l == '#' and r == '#':
        return True
    else:
        if l == '#':
            return int(d) < int(r)
        elif r == '#':
            return int(l) < int(d)
        else:
            return int(l) < int(d) and int(d) < int(r)

def isBalance(p, cur, d):
    if cur < len(p) and p[cur] != '#':
        if abs(GetDepth(p, 2*cur+1, d) - GetDepth(p, 2*cur+2, d)) > 1 \
            or not isOK(2*cur+1, cur, 2*cur+2, p):
            return False
        else:
            return isBalance(p, 2*cur+1, d) and isBalance(p, 2*cur+2, d)
    else:
        return True

def solve2():
    q = input().split()
    d = [-1]*len(q)
    print(isBalance(q,0,d))
# solve2()

def test():
    p = [
        '1 2 3 # 5 6 # # # 10 # # 13',
        #'#',
        '1 2 3 4 5 6 7 8 9',
        '10 2 # 30 # # # 40',
        '1 2 3 4 5 6 7 # # 8 # # # 9',
        #'# # # # #',
        '1 2 3 4 # # 5',
        '40 20 50 10 # # 60'
    ]
    for r in p:
        a = r.split()
        d = [-1]*len(a)
        print(isBalance(a, 0, d))

def main():
    solve()
    print()
    test()
    pass

main()