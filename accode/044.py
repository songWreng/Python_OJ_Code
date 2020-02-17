INF = 65535
class MatrixGraph():
    def __init__(self, v, d = False):
        self.Vcnt = v           # 点数
        self.digraph = d        # True = 有向图，False = 无向图
        self.adj = []           # 邻接矩阵v*v
        
class Edge(): # 带权边
    def __init__(self, b = -1, e = -1, w = -1):
        self.begin = b
        self.end = e
        self.weight = w
    def copy(self, oedge): # 拷贝其他边的数据
        self.begin = oedge.begin
        self.end = oedge.end
        self.weight = oedge.weight        

def Prime(graph, v = 0): # Prime 算法得到最小生成树(默认从图中的结点0开始)
    def getMinEdge(edges):
        minEdge = -1
        mini = INF
        for i in range(len(edges)):
            if edges[i].weight == 0: continue
            if edges[i].weight < mini:
                minEdge = i
                mini = edges[i].weight
        return minEdge

    mst = [] # MST只有 V - 1 条边.
    for i in range(graph.Vcnt - 1):
        mst.append(Edge())

    pedge = [None]*graph.Vcnt
    
    for i in range(graph.Vcnt):
        pedge[i] = Edge(v, i, graph.adj[v][i])
    
    pedge[v].weight = 0
    edgeCount = 0 # 已经找到的MST边数
    for i in range(1, graph.Vcnt):
        edgeNum = getMinEdge(pedge)
        mst[edgeCount].copy(pedge[edgeNum])
        edgeCount += 1
        v = pedge[edgeNum].end
        pedge[v].weight = 0
        for j in range(graph.Vcnt):
            if graph.adj[v][j] < pedge[j].weight:
                pedge[j].begin = v
                pedge[j].weight = graph.adj[v][j]
    return mst

def test02():
    V = int(input())
    G = MatrixGraph(V)
    while V > 0:
        G.adj.append(list(map(int, input().split())))
        V -= 1
    
    mst = Prime(G)
    sum = 0    
    for a in mst:
        sum += a.weight
    print(sum)
test02()



