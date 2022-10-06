''' BFS
every vertex has value  pi, color, d
G.V = all vertices
for all u in G.V
    ############ WE HAVE ############
u.color = color of u
u.d = distances(means how many edges between startNode and u)
u.pi = predecessor of u
'''

from directedgraph import DirectedGraph
import math
import queue

inf = math.inf
colorlst = ['white','gray','black']
valuekey = ['color','d','pi']
valueStr = "{valuekey[0] : colorlst[0], valuekey[1] : inf, valuekey[2] : None}"

def BFS(G,startNode):
    '''startNode is int'''
    if type(G) != DirectedGraph:
        return None
    if not G.isNodeExisted(startNode):
        print('dsklgfiesgiojews',startNode)
        return None
    for node in G.getAllNodes():
        G.nodeMap[node].value = eval(valueStr)
    # init startNode
    G.nodeMap[startNode].value = eval("{valuekey[0] : colorlst[0], valuekey[1] : 0, valuekey[2] : None}")
    Q = queue.Queue()
    Q.put(startNode)
    while not Q.empty():
        nowNodekey = Q.get()
        nowNode_ptr = G.nodeMap[nowNodekey]
        for node in G.getNodeOutNeighbors(nowNodekey):
            tmp_ptr = G.nodeMap[node]
            if tmp_ptr.value[valuekey[0]] == colorlst[0]:
                tmp_ptr.value[valuekey[0]] = colorlst[1]
                tmp_ptr.value[valuekey[1]] = nowNode_ptr.value[valuekey[1]] + 1
                tmp_ptr.value[valuekey[2]] = nowNodekey
                Q.put(node)
        nowNode_ptr.value[valuekey[0]] = colorlst[2]

def showBfsPath(G,startNode, endNode):
    '''if this startnode is not match in BFS(startnode), this function will stop'''
    if type(G) != DirectedGraph:
        return None
    if not G.isNodeExisted(startNode) or not G.isNodeExisted(endNode):
        return None
    try:
        if G.getNodeValue(startNode)[valuekey[2]] != None:
            return None
    except:
        return None
    if startNode == endNode:
        return [startNode]
    ans = []
    Q = queue.Queue()
    Q.put(endNode)
    while not Q.empty():
        nowNodekey = Q.get()
        queue_key = G.getNodeValue(nowNodekey)[valuekey[2]]
        if queue_key == None:
            ans.append(startNode)
            break 
        ans.append(nowNodekey)
        Q.put(queue_key)
    ans.reverse()
    return ans

def showBfsPathLength(G, startNode, endNode):
    if type(G) != DirectedGraph:
        return -1
    if not G.isNodeExisted(startNode) or not G.isNodeExisted(endNode):
        return -1
    try:
        if G.getNodeValue(startNode)[valuekey[2]] != None:
            return -1
    except:
        return -1
    if startNode == endNode:
        return 0
    return G.getNodeValue(endNode)[valuekey[1]]

def test():
    G = DirectedGraph()
    for i in range(9):
        G.addNode(i)
    G.addBiEdge(0,1)
    G.addBiEdge(0,4)
    G.addBiEdge(1,5)
    G.addBiEdge(2,3)
    G.addBiEdge(2,5)
    G.addBiEdge(2,6)
    G.addBiEdge(3,6)
    G.addBiEdge(3,7)
    G.addBiEdge(5,6)
    G.addBiEdge(6,7)
    BFS(G,1)
    for node in G.getAllNodes():
        print(G.getNodeValue(node))
    print(showBfsPath(G,1,7))
    print(showBfsPathLength(G,1,7))

if __name__ == '__main__':
    test()