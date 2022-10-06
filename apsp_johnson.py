''' JOHNSON
MAKE A GRAPH FIRST

'''
from directedgraph import DirectedGraph
from sssp_bellman_ford import BELLMAN_FORD
from sssp_dijkstra import DIJKSTRA
import math

inf = math.inf
colorlst = ['white','gray','black']
valuekey = ['color','d','pi']
valueStr = "{valuekey[0] : colorlst[0], valuekey[1] : inf, valuekey[2] : None}"

def JOHNSON(G):
    G2 = G.getSameGraph()
    s = inf
    for x in G2.getAllNodes():
        if s > x:
            s = x
    s -= 1
    G2.addNode(s)
    for x in G.getAllNodes():
        G2.addEdge(s,x,0)
    if not BELLMAN_FORD(G2,s):
        print('NWC FOUND!')
    else:
        h = {}
        for v in G2.getAllNodes():
            h[v] = G2.nodeMap[v].value[valuekey[1]]
        for edge in G2.getAllEdges():
            val = G2.getEdgeDistance(edge[0],edge[1])
            if val == None:
                val = inf
            if edge[0] == edge[1]:
                val = 0    
            G2.setEdge(edge[0],edge[1], val + h[edge[0]] - h[edge[1]])
            D = []
            G2.deleteNode(-1)
            node_to_idx = dict(zip(G2.getAllNodes(), range(G2.getNodeNumber()) ))
            # idx_to_node = dict(zip(range(G2.getNodeNumber()), G2.getAllNodes() ))     
        for i in range(G2.getNodeNumber()):
            tmp1 = []
            for j in range(G2.getNodeNumber()):
                tmp1.append(None)
            D.append(tmp1)
        for i,u in enumerate(G2.getAllNodes()):
            DIJKSTRA(G2,u)
            for j,v in enumerate(G2.getAllNodes()):
                val = G2.getEdgeDistance(u,v)
                val = G2.nodeMap[v].value[valuekey[1]]
                if val == None:
                    val = inf
                if i == j:
                    val = 0
                D[i][j] = val + h[v] - h[u]
        return node_to_idx, D

def AnalysisJohnsonDistance(fromNode, toNode,S ,D):
    ans_d = D[S[fromNode]][S[toNode]]
    return ans_d

def test():
    G = DirectedGraph()
    for i in range(1,6):
        G.addNode(i)
    G.addEdge(1,2,3)
    G.addEdge(1,3,8)
    G.addEdge(1,5,-4)
    G.addEdge(2,4,1)
    G.addEdge(2,5,7)
    G.addEdge(3,2,4)
    G.addEdge(4,1,2)
    G.addEdge(4,3,-5)
    G.addEdge(5,4,6)
    print(G)
    S, D = JOHNSON(G)
    ans = AnalysisJohnsonDistance(5,1,S,D)
    print(ans)
    print(G)

if __name__ == '__main__':
    test()