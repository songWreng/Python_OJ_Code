"""
构造AVL树，并输出其前序序列
"""

class Node():
    def __init__(self, v):
        self.Value = v
        self.Left = None
        self.Right = None
        self.Depth = 0

def GetDepth(node):
    if node == None: return -1
    return node.Depth

def SingleRotateWithLeft(node):
    tmp = node.Right
    node.Right = tmp.Left
    tmp.Left = node
    node.Depth = max(GetDepth(node.Left), GetDepth(node.Right)) + 1
    tmp.Depth = max(GetDepth(tmp.Left), GetDepth(tmp.Right)) + 1
    return tmp
def SingleRotateWithRight(node):
    tmp = node.Left
    node.Left = tmp.Right
    tmp.Right = node
    node.Depth = max(GetDepth(node.Left), GetDepth(node.Right)) + 1
    tmp.Depth = max(GetDepth(tmp.Left), GetDepth(tmp.Right)) + 1
    return tmp
def DoubleRotateWithLeft(node):
    node.Right = SingleRotateWithRight(node.Right)
    return SingleRotateWithLeft(node)
def DoubleRotateWithRight(node):
    node.Left = SingleRotateWithLeft(node.Left)
    return SingleRotateWithRight(node)

def Insert(node, v):
    if node == None:
        node = Node(v)
    else:
        if node.Value < v:
            node.Right = Insert(node.Right, v)
            node.Depth = max(GetDepth(node.Left), GetDepth(node.Right)) + 1
            if GetDepth(node.Right) - GetDepth(node.Left) > 1:
                if v < node.Right.Value:
                    node = DoubleRotateWithLeft(node)
                elif node.Right.Value < v:
                    node = SingleRotateWithLeft(node)

        elif v < node.Value:
            node.Left = Insert(node.Left, v)
            node.Depth = max(GetDepth(node.Left), GetDepth(node.Right)) + 1
            if GetDepth(node.Left) - GetDepth(node.Right) > 1:
                if node.Left.Value < v:
                    node = DoubleRotateWithRight(node)
                elif v < node.Left.Value:
                    node = SingleRotateWithRight(node)
    return node

def PrintByDLR(node):
    if node != None:
        print(node.Value)
        PrintByDLR(node.Left)
        PrintByDLR(node.Right)

def solve():
    # p = list(map(int, input().split()))
    p = [10,5,50,3,8,20,60,4,30,55,70,56]
    tree = None
    for a in p:
        tree = Insert(tree, a)
    PrintByDLR(tree)
solve()

