'''BIPARTITE
'''
from directedgraph import DirectedGraph
from flow_edmond_karp import FORD_FULKERSON
import math

inf = math.inf
colorlst = ['white','gray','black']
valuekey = ['color','d','pi']
valueStr = "{valuekey[0] : colorlst[0], valuekey[1] : inf, valuekey[2] : None}"

def BIPARTITE_AB_MATCH(G,A,B):
    '''A, B nodes are needed : [int,int,...,int]'''
    s = inf
    t = -inf
    for x in G.getAllNodes():
        if s > x:
            s = x
        if t < x:
            t = x
    s -= 1
    t += 1
    G.addNode(s)
    G.addNode(t)
    for item in G.getAllEdges():
        u,v = item[0],item[1]
        G.setEdge(u,v,1)
    for v in A:
        G.addEdge(s,v)
    for u in B:
        G.addEdge(u,t)
    tmp_ans = FORD_FULKERSON(G,s,t)
    ans = {}
    if tmp_ans != None:
        for x in tmp_ans:
            if type(tmp_ans[x]) != int:
                ans['matching'] = [y[1:-1] for y in tmp_ans[x]]
            else:
                ans['matching_number'] = tmp_ans[x]
    return ans

def test():
    A = [0,1,2,3,4]
    B = [5,6,7,8]
    G = DirectedGraph()
    for i in range(9):
        G.addNode(i)
    G.addEdge(0,5)
    G.addEdge(1,5)
    G.addEdge(2,6)
    G.addEdge(2,7)
    G.addEdge(2,8)
    G.addEdge(3,7)
    G.addEdge(4,7)
    ans = BIPARTITE_AB_MATCH(G,A,B)
    print(ans)

if __name__ == '__main__':
    test()