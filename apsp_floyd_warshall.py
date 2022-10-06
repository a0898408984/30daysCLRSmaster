''' FLOYD-WARSHALL
MAKE A GRAPH FIRST
USE FLOYD_WARSHALL(G) to get D, P MATRIX
ENJOY ANALYSIS any two nodes in G to get shortest path
'''
from directedgraph import DirectedGraph
import math
inf = math.inf

def FLOYD_WARSHALL(G):
    '''RETURN ONE DICT AND TWO MATRIX(DISTANCE, PREDECESSOR)'''
    W1 = []
    W2 = []
    DistancePair = []
    PredecessorPair = []
    for i in range(G.getNodeNumber()):
        tmp1 = []
        tmp2 = []
        tmp3 = []
        tmp4 = []
        for j in range(G.getNodeNumber()):
            tmp1.append(None)
            tmp2.append(None)
            tmp3.append(None)
            tmp4.append(None)
        W1.append(tmp1)
        DistancePair.append(tmp2)
        W2.append(tmp3)
        PredecessorPair.append(tmp4)

    node_to_idx = dict(zip(G.getAllNodes(), range(G.getNodeNumber()) ))
    idx_to_node = dict(zip(range(G.getNodeNumber()), G.getAllNodes() ))

    for i,x in enumerate(node_to_idx):
        for j,y in enumerate(node_to_idx):
            val = G.getEdgeDistance(x,y)
            pi = i 
            if val == None:
                val = inf
                pi = None
            if i == j:
                val = 0
                pi = None
            W1[i][j] = val
            W2[i][j] = pi  
    for k in range(G.getNodeNumber()):   
        if k != 0:     
            for i in range(G.getNodeNumber()):
                for j in range(G.getNodeNumber()):
                    W1[i][j] = DistancePair[i][j]
                    W2[i][j] = PredecessorPair[i][j]
        for i in range(G.getNodeNumber()):
            for j in range(G.getNodeNumber()):
                if W1[i][j] <= W1[i][k]+W1[k][j]:
                    DistancePair[i][j] = W1[i][j]
                    PredecessorPair[i][j] = W2[i][j]
                else:
                    DistancePair[i][j] = W1[i][k]+W1[k][j]
                    PredecessorPair[i][j] = W2[k][j]
    idx_to_node_dict = {'idx_to_node':idx_to_node, 'node_to_idx':node_to_idx}
 
    return idx_to_node_dict,DistancePair,PredecessorPair

def AnalysisFloydWarshall(fromNode,toNode,S,D,P) -> dict:
    '''KEY HAS DISTANCE, PATH'''
    ans_distance = inf
    ans_predecessor = []
    node_to_idx = S['node_to_idx']
    idx_to_node = S['idx_to_node']
    
    if node_to_idx.get(fromNode) == None or node_to_idx.get(toNode) == None :
        return {'distance':ans_distance, 'path':ans_predecessor}
    
    idx_u, idx_v = node_to_idx[fromNode],node_to_idx[toNode]
    
    ans_distance = D[idx_u][idx_v]
    
    if ans_distance != inf:
        ans_predecessor.append(idx_v)
        while True:
            if P[idx_u][idx_v] == None:
                break
            ans_predecessor.append(P[idx_u][idx_v])
            idx_v = P[idx_u][idx_v]
        ans_predecessor.reverse()
        for i in range(len(ans_predecessor)):
            ans_predecessor[i] = idx_to_node[ans_predecessor[i]]
    return {'distance':ans_distance, 'path':ans_predecessor}

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
    S, D, P = FLOYD_WARSHALL(G)
    print(S)
    print(D)
    print(P)
    ans = AnalysisFloydWarshall(5,2,S,D,P)
    print(ans)

if __name__ == '__main__':
    test()