''' DFS
every vertex has value  pi, color, d, f
G.V = all vertices
for all u in G.V
    ############ WE HAVE ############
u.color = color of u
u.d = discovery time (time to paint gray)
u.pi = predecessor of u
u.f = finishing time(time to paint black)
'''
from directedgraph import DirectedGraph
import math

inf = math.inf
colorlst = ['white','gray','black']
valuekey = ['color','d', 'f','pi']
valueStr = "{valuekey[0] : colorlst[0], valuekey[1] : 0, valuekey[2] : 0, valuekey[3] : None}"
time = 0

def DFS(G, nodes=None, mode = 0):
    '''mode == 1 and nodes != None
    use nodes to do dfs not G.getAllNodes for SCC
    '''
    global time
    if nodes == None or mode == 0:
        nodes = G.getAllNodes()
    for node in nodes:
        G.nodeMap[node].value = eval(valueStr)
    time = 0
    for node in nodes:
        ptr = G.nodeMap[node]
        if ptr.value[valuekey[0]] == colorlst[0]:
            DFS_VISIT(G,node)

def DFS_VISIT(G, nodekey):
    global time
    time += 1
    ptr = G.nodeMap[nodekey]
    ptr.value[valuekey[1]] = time
    ptr.value[valuekey[0]] = colorlst[1]
    for node in G.getNodeOutNeighbors(nodekey):
        tmp_ptr = G.nodeMap[node]
        if tmp_ptr.value[valuekey[0]] == colorlst[0]:
            tmp_ptr.value[valuekey[3]] = nodekey
            DFS_VISIT(G, node)
    ptr.value[valuekey[0]] = colorlst[2]
    time += 1
    ptr.value[valuekey[2]] = time

def TOPOLOGY(G):
    '''Need to do DFS first'''
    tmp = []
    for idx in G.getAllNodes():
        nodef = G.getNodeValue(idx)[valuekey[2]]
        tmp.append([nodef,idx])
    tmp.sort(reverse=True)
    _,ans = zip(*tmp)
    return ans

def test():
    G = DirectedGraph()
    for i in range(6):
        G.addNode(i)
    G.addEdge(0,1)
    G.addEdge(0,3)
    G.addEdge(1,4)
    G.addEdge(2,4)
    G.addEdge(2,5)
    G.addEdge(3,1)
    G.addEdge(4,3)
    G.addEdge(5,5)
    DFS(G)
    for i in range(6):
        print(G.getNodeValue(i))
    G = G.getOppoGraph()
    print('##############')
    DFS(G)
    for i in range(6):
        print(G.getNodeValue(i))

def test2(): # TOPOLOGY SORT
    G = DirectedGraph()
    for i in range(9):
        G.addNode(i)
    G.addEdge(0,1)
    G.addEdge(0,6)
    G.addEdge(1,2)
    G.addEdge(1,6)
    G.addEdge(2,5)
    G.addEdge(3,2)
    G.addEdge(3,4)
    G.addEdge(4,5)
    G.addEdge(7,6)
    DFS(G)
    for i in range(9):
        print(G.getNodeValue(i))
    print(TOPOLOGY(G))

if __name__ == '__main__':
    test()