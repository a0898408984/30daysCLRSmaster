'''  BELLMAN_FORD
O(VE) NO NWC BUT YES Negetive weight
every vertex has value  pi, color, d
G.V = all vertices
for all u in G.V
    ############ WE HAVE ############
u.color = color of u
u.d = distances(s and u shortest distance)
u.pi = predecessor of u
'''
from directedgraph import DirectedGraph
import math

inf = math.inf
colorlst = ['white','gray','black']
valuekey = ['color','d','pi']
valueStr = "{valuekey[0] : colorlst[0], valuekey[1] : inf, valuekey[2] : None}"

def init_single_source(G,startnode):
    for node in G.getAllNodes():
        G.nodeMap[node].value = eval(valueStr)
    G.nodeMap[startnode].value[valuekey[1]] = 0

def relaxation(G,u,v):
    tar = G.nodeMap[u].value[valuekey[1]] + G.getEdgeDistance(u,v)
    if G.nodeMap[v].value[valuekey[1]] > G.nodeMap[u].value[valuekey[1]] + G.getEdgeDistance(u,v):
        G.nodeMap[v].value[valuekey[1]] = tar
        G.nodeMap[v].value[valuekey[2]] = u

def BELLMAN_FORD(G,startnode) -> bool:
    init_single_source(G,startnode)
    for i in range(G.getNodeNumber() - 1):
        for item in G.getAllEdges():
            relaxation(G,item[0],item[1])
    for item in G.getAllEdges():
        u,v = item
        tar = G.nodeMap[u].value[valuekey[1]] + G.getEdgeDistance(u,v)
        if G.nodeMap[v].value[valuekey[1]] > tar:
            return False
    return True

def test():
    G = DirectedGraph()
    for i in range(5):
        G.addNode(i)
    G.addEdge(0,1,6)
    G.addEdge(0,2,7)
    G.addEdge(0,4,2)
    G.addEdge(1,2,8)
    G.addEdge(1,3,5)
    G.addEdge(1,4,-4)
    G.addEdge(2,3,-3)
    G.addEdge(2,4,9)
    G.addEdge(3,1,-2)
    G.addEdge(4,3,7)
    print(BELLMAN_FORD(G,0))
    for i in range(5):
        print(G.getNodeValue(i))
if __name__ == "__main__":
    test()