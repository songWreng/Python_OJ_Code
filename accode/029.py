class Node():
    def __init__(self, v):
        self.Value = v
        self.Left = None
        self.Right = None

def help_printTreeByDir(tree, tabNum):
    if tree != None:
        print("    "*tabNum, end = "")
        # print('%2d(%d)' % (tree.Value, tree.Depth))
        print("%2d" % tree.Value)
        help_printTreeByDir(tree.Left, tabNum + 1)
        help_printTreeByDir(tree.Right, tabNum + 1)
def PrintTreeByDir(tree):
    help_printTreeByDir(tree, 0)
    pass 

def CreateHurffman(p):
    q = [None]*len(p)
    for i,a in enumerate(p):
        q[i] = Node(a)
    
    for i in range(len(p) - 1):
        t1 = i 
        t2 = i + 1
        for j in range(t2, len(p)): # 找到最小值和第二小的值
            if q[j].Value < q[t1].Value:
                t2 = t1
                t1 = j
            elif q[j].Value < q[t2].Value:
                t2 = j
        newNode = Node(q[t1].Value + q[t2].Value)
        newNode.Left = q[t1]
        newNode.Right = q[t2]

        q[t1] = newNode
        q[t2] = q[i]
        q[i] = None
    return newNode

def help_CalWPL(node, num, res):
    if node.Left and node.Right:
        res = help_CalWPL(node.Left, num + 1, res)
        res = help_CalWPL(node.Right, num + 1, res)
        return res
    else:
        res += num * node.Value
        return res
def CalWPL(HTree):
    return help_CalWPL(HTree, 0, 0)

def test():
    # p = [7,2,5,4]
    s = '4 2 1 1'
    # s = '36 2 8 5 6 25 13 19'
    p = list(map(int, s.split()))
    huffmanTree = CreateHurffman(p)
    PrintTreeByDir(huffmanTree)
    print("WPL =", CalWPL(huffmanTree))

def solve():
    # p = [int(b) for b in input().split()]
    print(CalWPL(CreateHurffman([int(b) for b in input().split()])))
def main():
    test()
    # solve()
main()







