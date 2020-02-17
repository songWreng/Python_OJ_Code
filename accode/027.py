'''
输入：
一行数据构建唯一查找树(数据不会重复)
n 表示插入元素的数量
n行插入元素 (每插入成功，前序遍历)
m 表示删除的数据
m行删除数据 (删除成功，后序遍历，否则输出“Delete Error”)
'''
class TreeNode():
    def __init__(self, v):
        self.Value = v
        self.Left = None
        self.Right = None
def Insert(tree, v):
    if tree == None:
        tree = TreeNode(v)
    else:
        if tree.Value < v:
            tree.Right = Insert(tree.Right, v)
        elif v < tree.Value:
            tree.Left = Insert(tree.Left, v)
    return tree

def FindMin(tree):
    p = tree
    if p == None: return None
    while p.Left != None:
        p = p.Left
    return p

def Delete(tree, v):
    if tree != None:
        if tree.Value < v:
            tree.Right = Delete(tree.Right, v)
        elif v < tree.Value:
            tree.Left = Delete(tree.Left, v)
        else:
            if tree.Left != None and tree.Right != None:
                tmp = FindMin(tree.Right)
                tree.Value = tmp.Value
                tree.Right = Delete(tree.Right, tmp.Value)
            else:
                if tree.Right == None: tree = tree.Left
                else: tree = tree.Right
    return tree

def Find(tree, v):
    if tree != None:
        if tree.Value < v: return Find(tree.Right, v)
        elif tree.Value > v: return Find(tree.Left,v)
        else: return tree
    else:
        return None

def PrintByDLR(tree):
    if tree != None:
        print(tree.Value, end = " ")
        PrintByDLR(tree.Left)
        PrintByDLR(tree.Right)

def PrintByLRD(tree):
    if tree != None:
        PrintByLRD(tree.Left)
        PrintByLRD(tree.Right)
        print(tree.Value, end = " ")

def solve():
    myTree = None
    p = [int(b) for b in input().split()]
    for a in p:
        myTree = Insert(myTree, a)
    #PrintByDLR(myTree)
    for i in range(int(input())):
        myTree = Insert(myTree, int(input()))
        PrintByDLR(myTree)
        print()
    for i in range(int(input())):
        v = int(input())
        if Find(myTree, v) != None:
            myTree = Delete(myTree, v)
            PrintByLRD(myTree)
            print()
        else:
            print("Delete Error")
       
solve()