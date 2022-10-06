''' DIJKSTRA
O(ElgV) NO Negetive weight
every vertex has value  pi, color, d
G.V = all vertices
for all u in G.V
    ############ WE HAVE ############
u.color = color of u
u.d = distances(s and u shortest distance)
u.pi = predecessor of u
'''
from directedgraph import DirectedGraph
from min_heap import MinHeap
import math


inf = math.inf
colorlst = ['white','gray','black']
valuekey = ['color','d','pi']
valueStr = "{valuekey[0] : colorlst[0], valuekey[1] : inf, valuekey[2] : None}"

def init_single_source(G,startnode):
    for node in G.getAllNodes():
        G.nodeMap[node].value = eval(valueStr)
    G.nodeMap[startnode].value[valuekey[1]] = 0

def relaxation(G,Q,u,v):
    tar = G.nodeMap[u].value[valuekey[1]] + G.getEdgeDistance(u,v)
    if G.nodeMap[v].value[valuekey[1]] > G.nodeMap[u].value[valuekey[1]] + G.getEdgeDistance(u,v):
        Q.decreaseKey((G.nodeMap[v].value[valuekey[1]],v), (tar,v))
        G.nodeMap[v].value[valuekey[1]] = tar
        G.nodeMap[v].value[valuekey[2]] = u


def DIJKSTRA(G,startnode):
    init_single_source(G,startnode)
    Q = MinHeap()
    for nodeidx in G.getAllNodes():
        Q.insertKey((G.nodeMap[nodeidx].value[valuekey[1]], nodeidx))
    existed = {}
    while not Q.isEmpty():
        item = Q.extractMin()
        existed[item[1]] = 1
        u = item[1]
        for v in G.getNodeOutNeighbors(u):
            if existed.get(v) == None:
                relaxation(G,Q,u,v)

def AnalysisDijkstraPath(G,startnode,endnode) -> list:
    if not G.isNodeExisted(startnode) or not G.isNodeExisted(endnode):
        return []
    if G.nodeMap[startnode].value[valuekey[1]] != 0 or\
         G.nodeMap[startnode].value[valuekey[2]] != None:
        return []
    if startnode == endnode:
        return [endnode]
    ans = []
    nownode = endnode
    while True:
        ans.append(nownode)
        if G.nodeMap[nownode].value[valuekey[2]] == None:
            break
        nownode = G.nodeMap[nownode].value[valuekey[2]] 
    ans.reverse()
    return ans 

def test():
    G = DirectedGraph()
    for i in range(5):
        G.addNode(i)
    G.addEdge(0,1,10)
    G.addEdge(0,2,5)
    G.addEdge(1,2,2)
    G.addEdge(1,3,1)
    G.addEdge(2,1,3)
    G.addEdge(2,3,9)
    G.addEdge(2,4,2)
    G.addEdge(3,4,4)
    G.addEdge(4,0,7)
    G.addEdge(4,3,6)
    print(G)
    DIJKSTRA(G,0)
    for i in range(5):
        print(i,G.getNodeValue(i))
    ans = AnalysisDijkstraPath(G,0,3)
    print(ans)

if __name__ == "__main__":
    test()