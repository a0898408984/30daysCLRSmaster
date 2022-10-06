''' MST_PRIM
every vertex has value  pi, color, d
USE Value pi to get MST
'''
from directedgraph import DirectedGraph
import math
from min_heap import MinHeap

inf = math.inf
colorlst = ['white','gray','black']
valuekey = ['color','d','pi']
valueStr = "{valuekey[0] : colorlst[0], valuekey[1] : inf, valuekey[2] : None}"

def MST_PRIM(G,root):
    Q = MinHeap()
    for node in G.getAllNodes():
        G.nodeMap[node].value = eval(valueStr)
    ptr = G.nodeMap[root]
    ptr.value[valuekey[1]] = 0
    for node in G.getAllNodes():
        if len(G.getNodeInNeighbors(node)) != 0:
            Q.insertKey((G.nodeMap[node].value[valuekey[1]], node))
    existed = {}
    while not Q.isEmpty():
        tmp_ptrkey = Q.extractMin()[-1]
        existed[tmp_ptrkey] = 1
        for node in G.getNodeOutNeighbors(tmp_ptrkey):
            node_ptr = G.nodeMap[node] 
            if existed.get(node) == None and\
                G.getEdgeDistance(tmp_ptrkey,node) < node_ptr.value[valuekey[1]]:
                Q.decreaseKey((node_ptr.value[valuekey[1]], node), (G.getEdgeDistance(tmp_ptrkey,node), node))
                node_ptr.value[valuekey[1]] = G.getEdgeDistance(tmp_ptrkey,node)
                node_ptr.value[valuekey[2]] = tmp_ptrkey


def test():
    G = DirectedGraph()
    for i in range(10):
        G.addNode(i)
    G.addBiEdge(0,1,4)
    G.addBiEdge(1,2,8)
    G.addBiEdge(2,3,7)
    G.addBiEdge(3,4,9)
    G.addBiEdge(4,5,10)
    G.addBiEdge(5,6,2)
    G.addBiEdge(6,7,1)
    G.addBiEdge(7,8,7)
    G.addBiEdge(0,7,8)
    G.addBiEdge(1,7,11)
    G.addBiEdge(6,8,6)
    G.addBiEdge(2,8,2)
    G.addBiEdge(2,5,4)
    G.addBiEdge(3,5,14)
    MST_PRIM(G,0)
    print(G)
    for i in range(10):
        print(i, G.getNodeValue(i))

if __name__ == '__main__':
    test()