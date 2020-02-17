'''
哈夫编码
输入：
正整数：表示编码字母的数量
字符串：包含了n中字母的字符串

输出:
输出哈夫曼编码

注意：
因哈夫曼树的的构造不唯一，现约定如下：
输入中首先给出了有多少个字符要编码，
然后根据输入字符串获得每个字母按字典顺序的权值序列（每个字母的权值即该字母在字符串中出现的次数），

造哈夫曼树时每次从权值序列选取（从左到右选取）两个最小的权值，
若选取的值不相等，那么较小值的结点作为以他们值加和的新结点的左孩子，另一个则为右孩子，
若选取的值相等，先选取的做左孩子，后选取的做右孩子，
删除已选取的值的结点，并在权值序列最后（注意最后！）添加两个选取值加和的新结点。
如此往复，直到权值序列表长度为1。

我的看法：
额，根据这里的题意：对于权值序列，最小的一个数应该是相对在左边，第二小的数应该是在相对位置的右边

'''
from collections import Counter
from collections import deque


class TreeNode():
    def __init__(self, v, k = None):
        self.Value = v  # 权重
        self.Key = k    # 关键字
        self.Left = None
        self.Right = None

def PrintNode(node, t):
    if node != None:
        print('    '*t, end = "")
        if node.Key != None:
            print('%-2d:%c' % (node.Value, node.Key))
        else:
            print('%-4d' % node.Value)
        PrintNode(node.Left, t + 1)
        PrintNode(node.Right, t + 1)


def Decoding(node, di, s):
    if node != None:
        if node.Left == None and node.Right == None:
            di[node.Key] = s
        else:
            Decoding(node.Left, di, s + '0')
            Decoding(node.Right, di, s + '1')

        

def MakeTree(d): #  d 是一个权重字典
    p = deque()
    for k in d:
        p.append(TreeNode(d[k], k))

    while len(p) > 1:
        firstMin = min(p, key = lambda x : x.Value)
        del p[p.index(firstMin)]
        secondMin = min(p, key = lambda x : x.Value)
        del p[p.index(secondMin)]  

        newNode = TreeNode(firstMin.Value + secondMin.Value)
        newNode.Left = firstMin
        newNode.Right = secondMin
        p.append(newNode)

    # print("tree")
    # PrintNode(p[0], 0)

    di = {}
    Decoding(p[0], di, '')
    # print(di)
    return di


def solve():
    #input()
    s = input()
    p = dict(Counter(s))
    # print(p)
    di = MakeTree(p)
    for a in s:
        print(di[a], end =" ")
    
solve()    













