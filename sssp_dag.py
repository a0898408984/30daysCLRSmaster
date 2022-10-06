''' DAG
O(E + V) DAG ONLY
every vertex has value  pi, color, d
G.V = all vertices
for all u in G.V
    ############ WE HAVE ############
u.color = color of u
u.d = distances(s and u shortest distance)
u.pi = predecessor of u
'''
from directedgraph import DirectedGraph
import dfs
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

def DAG_SP(G,startnode):
    dfs.DFS(G)
    topologyLst = dfs.TOPOLOGY(G)
    init_single_source(G,startnode)
    for u in topologyLst:
        for v in G.getNodeOutNeighbors(u):
            relaxation(G,u,v)
    
def test():
    G = DirectedGraph()
    for i in range(6):
        G.addNode(i)
    G.addEdge(0,1,5)
    G.addEdge(0,2,3)
    G.addEdge(1,2,2)
    G.addEdge(1,3,6)
    G.addEdge(2,3,7)
    G.addEdge(2,4,4)
    G.addEdge(2,5,2)
    G.addEdge(3,4,-1)
    G.addEdge(3,5,1)
    G.addEdge(4,5,-2)
    print(G)
    DAG_SP(G,1)
    for i in range(6):
        print(G.getNodeValue(i))

if __name__ == "__main__":
    test()