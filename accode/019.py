'''
注意:
属性命名限制：Node, root, elem, lchild, rchild
变量命名限制：MyTree

输入：
要建立二叉树的元素
命令的数量n
n行执行的命令

输出：
n行命令运行结果
空树或者不存时，都输出None
'''
from collections import deque
class Node():
    def __init__(self, e):
        self.elem = e
        self.lchild = None
        self.rchild = None
class Tree():
    def __init__(self, e):
        self.root = Node(e)

def PrintDLR(node):
    if node != None:
        print(node.elem)
        PrintDLR(node.lchild)
        PrintDLR(node.rchild)
    
def solve19():
    s = input().split()
    MyTree = None
    if len(s) > 0 and s[0] != '#':
        q = deque()
        MyTree = Tree(s[0])
        q.append(MyTree.root)
        flag = 0
        for c in s[1:]:
            if c != '#':
                newNode = Node(c)
            else:
                newNode = None
            q.append(newNode)
            if (flag == 0):
                if q[0] != None: q[0].lchild = newNode
                flag = 1
            else: 
                if q[0] != None: q[0].rchild = newNode
                flag = 0
                q.popleft()
   
    n = int(input())
    while n > 0:
        try:
            eval(input())
        except:
            print("None")
        n -= 1
solve19()





