'''STRONG CONNECTED COMPONENT
USE SCC YOU WILL GET SCC-GRAPH AND NODE-GROUP-DICT
'''

from directedgraph import DirectedGraph
from dfs import DFS,TOPOLOGY
import math
inf = math.inf
colorlst = ['white','gray','black']
valuekey = ['color','d', 'f','pi']
valueStr = "{valuekey[0] : colorlst[0], valuekey[1] : 0, valuekey[2] : 0, valuekey[3] : None}"
time = 0

def SCC(G):
    '''RETURN A GRAPH AND A Node-Group-LIST'''
    G2 = G.getOppoGraph()
    DFS(G)
    topologyLst = TOPOLOGY(G)
    DFS(G2,topologyLst,1)
    node_to_group = {}
    group = -1
    for x in G2.getAllNodes():
        if node_to_group.get(x) != None:
            continue
        value = G2.getNodeValue(x)
        if value[valuekey[2]] - value[valuekey[1]] == 1:
            if value[valuekey[3]] == None:
                group += 1
                if node_to_group.get(x) == None:
                    node_to_group[x] = group
            else:
                if node_to_group.get(G2.getNodeValue(x)[valuekey[3]]) != None:
                    node_to_group[x] = node_to_group[G2.getNodeValue(x)[valuekey[3]]]
                    continue
                nowNode = x
                group += 1
                while True:
                    if node_to_group.get(nowNode) == None:                    
                        node_to_group[nowNode] = group
                        nowNode = G2.getNodeValue(nowNode)[valuekey[3]]
                    else:
                        break
                    if nowNode == None:
                        break
    G3 = DirectedGraph()
    tmp_ans = []
    for i in range(group + 1):
        tmp_ans.append([])
    for idx in node_to_group:
        tmp_ans[node_to_group[idx]].append(idx)
    for i in range(len(tmp_ans)):
        G3.addNode(i)
        G3.nodeMap[i].value = {'group':tmp_ans[i]}
    for edge in G.getAllEdges():
        u,v = edge[0],edge[1]
        if node_to_group[u] != node_to_group[v]:
            G3.addEdge(node_to_group[u],node_to_group[v])
    return G3,node_to_group

def test1():
    G = DirectedGraph()
    for i in range(8):
        G.addNode(i)
    G.addEdge(0,4)
    G.addEdge(1,0)
    G.addEdge(2,1)
    G.addEdge(2,3)
    G.addEdge(3,2)
    G.addEdge(4,1)
    G.addEdge(5,1)
    G.addEdge(5,4)
    G.addEdge(5,6)
    G.addEdge(6,2)
    G.addEdge(6,5)
    G.addEdge(7,3)
    G.addEdge(7,6)
    G.addEdge(7,7)

    print(G)
    G3,ans = SCC(G)
    print(G3)
    for i in range(G3.getNodeNumber()):
        print(i,G3.getNodeValue(i))
    print(ans)

def test2():
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
    G2,ans = SCC(G)
    print(G2)
    print(ans)
    for i in range(G2.getNodeNumber()):
        print(i,G2.getNodeValue(i))   

def test3():
    G = DirectedGraph()
    for i in range(8):
        G.addNode(i)
    G.addEdge(6,7)
    G.addEdge(7,5)
    G.addEdge(7,4)
    G.addEdge(7,0)
    G.addEdge(0,1)
    G.addEdge(0,2)
    G.addEdge(0,3)
    G.addEdge(1,0)
    G.addEdge(1,2)
    G.addEdge(5,6)
    G.addEdge(5,4)
    G.addEdge(4,3)     
    G.addEdge(3,4)
    G.addEdge(3,2)
    
    print(G)
    G2,ans = SCC(G)
    print(G2)
    print(ans)
    for i in range(G2.getNodeNumber()):
        print(i,G2.getNodeValue(i))   

def test4():
    G = DirectedGraph()
    for i in range(6):
        G.addNode(i)
    G.addEdge(0,1,16)
    G.addEdge(0,4,13)
    G.addEdge(1,2,12)
    G.addEdge(2,4,9)
    G.addEdge(2,3,20)
    G.addEdge(4,1,4)
    G.addEdge(4,5,14)
    G.addEdge(5,2,7)
    G.addEdge(5,3,4)
    print(G)
    G2,ans = SCC(G)
    print(G2)
    print(ans)
    for i in range(G2.getNodeNumber()):
        print(i,G2.getNodeValue(i))   


if __name__ == '__main__':
    test4()