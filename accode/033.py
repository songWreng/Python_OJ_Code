class RBNode():
    def __init__(self, v, c = 'r'):
        self.Value = v
        self.Color = c
        self.Left = None
        self.Right = None
        self.Parent = None

# 单旋转
def LeftRotate(node):
    tmp = node.Right
    node.Right = tmp.Left
    if tmp.Left != None:
        tmp.Left.Parent = node
    tmp.Parent = node.Parent
    if node.Parent == None: pass
    elif node.Parent.Left == node:
        node.Parent.Left = tmp
    elif node.Parent.Right == node:
        node.Parent.Right = tmp
    tmp.Left = node
    node.Parent = tmp
    return tmp

def RightRotate(node):
    tmp = node.Left
    node.Left = tmp.Right
    if tmp.Right != None:
        tmp.Right.Parent = node
    tmp.Parent = node.Parent
    if node.Parent == None: pass
    elif node.Parent.Right == node:
        node.Parent.Right = tmp
    elif node.Parent.Left == node:
        node.Parent.Left = tmp
    tmp.Right = node
    node.Parent = tmp
    return tmp

# 插入结点
def RBInsert(t, v):
    cur = t
    pre = cur.Parent
    while cur != None:
        pre = cur
        if v < cur.Value: cur = cur.Left
        elif cur.Value < v: cur = cur.Right
        else: return t
    newNode = RBNode(v, 'r')
    newNode.Parent = pre
    if pre.Value < v: pre.Right = newNode
    else: pre.Left = newNode
    
    # 调整
    while newNode.Color == 'r' and newNode.Parent != None and newNode.Parent.Color == 'r':
        if newNode.Parent == newNode.Parent.Parent.Left:
            uncle = newNode.Parent.Parent.Right
            if uncle != None and uncle.Color == 'r':
                uncle.Color = newNode.Parent.Color = 'b'
                newNode.Parent.Parent.Color = 'r'
                newNode = newNode.Parent.Parent
            else:
                if newNode == newNode.Parent.Right:
                    newNode = LeftRotate(newNode.Parent)
                    newNode = newNode.Left
                newNode.Parent.Color = 'b'
                newNode.Parent.Parent.Color = 'r'
                newNode = RightRotate(newNode.Parent.Parent)

        else:
            uncle = newNode.Parent.Parent.Left
            if uncle != None and uncle.Color == 'r':
                uncle.Color = newNode.Parent.Color = 'b'
                newNode.Parent.Parent.Color = 'r'
                newNode = newNode.Parent.Parent
            else:
                if newNode == newNode.Parent.Left:
                    newNode = RightRotate(newNode.Parent)
                    newNode = newNode.Right
                newNode.Parent.Color = 'b'
                newNode.Parent.Parent.Color = 'r'
                newNode = LeftRotate(newNode.Parent.Parent)
                # 这里为什么要接受旋转的返回值呢？
                # 由于旋转会替换掉根结点！导致后面的t会丢树。
    if newNode.Parent == None: 
        t = newNode
    t.Color = 'b'
    return t

# 前序遍历打印树的信息
def PrintRBTree(node):
    help_PrintRBTree(node, 0)
def help_PrintRBTree(node, num):
    print(" "*num*8, end = "")
    if node != None:
        if node.Parent != None:
            print('%-2d~%2d(%c)' % (node.Value, node.Parent.Value, node.Color))
        else:
            print('@ ~%2d(%c)' % (node.Value, node.Color))
        help_PrintRBTree(node.Left, num + 1)
        help_PrintRBTree(node.Right, num + 1)
    else:
        print("  NIL")
    
def test():
    rb = RBNode(1, 'b')
    for a in range(2, 10):
        rb = RBInsert(rb, a)

    PrintRBTree(rb)
    print()
    
    print("旋转测试")
    tmp = rb.Right
    LeftRotate(rb)
    PrintRBTree(tmp)
    print()
    PrintRBTree(rb)
# test()

def PrintTreeDLR(node, choice):
    if node != None:
        if choice == 0: print(node.Value, end = " ")
        else: 
            tmp = 0
            if node.Color == 'b': tmp = 1
            print(tmp, end = " ")
        PrintTreeDLR(node.Left, choice)
        PrintTreeDLR(node.Right, choice)

def solve():
    p = list(map(int, input().split()))
    if len(p) > 0:
        rb = RBNode(p[0], 'b')
        for a in p[1:]:
            rb = RBInsert(rb, a)
        PrintTreeDLR(rb, 0)
        print()
        PrintTreeDLR(rb, 1)

solve()

