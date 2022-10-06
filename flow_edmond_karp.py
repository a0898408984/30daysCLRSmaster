'''EDMOND-KARP
'''

from directedgraph import DirectedGraph
from sssp_dijkstra import DIJKSTRA, AnalysisDijkstraPath
import math

inf = math.inf
colorlst = ['white','gray','black']
valuekey = ['color','d','pi']
valueStr = "{valuekey[0] : colorlst[0], valuekey[1] : inf, valuekey[2] : None}"



def FORD_FULKERSON(G,startnode,endnode):
    '''RETURN A DICTIONARY OR NONE
        IF DICT, ITS KEY HAS AUGMENTEDPATH AND MAXIMUMFLOW
    '''
    if startnode == endnode:
        return
    for edge in G.getAllEdges():
        G.setEdge(edge[0],edge[1],G.getEdgeDistance(edge[0],edge[1]), 0)
    Gf = G.getSameGraph()
    ans_f = 0
    ans_p = []
    while True:
        DIJKSTRA(Gf,startnode)
        if not Gf.nodeMap[endnode].value[valuekey[1]] < inf:
            break                
        else:
            '''has path from start to end in Gf'''
            path_Dijkstra = AnalysisDijkstraPath(Gf,startnode,endnode)
            Cf = inf
            for i in range(len(path_Dijkstra) - 1):
                u,v = path_Dijkstra[i], path_Dijkstra[i+1]
                tar = Gf.getEdgeDistance(u,v)
                if Cf > tar:
                    Cf = tar
            for i in range(len(path_Dijkstra) - 1):
                u,v = path_Dijkstra[i], path_Dijkstra[i+1]
                # G
                newFlow = G.getEdgeFlow(u,v)+Cf if G.isEdgeExist(u,v) else G.getEdgeFlow(v,u)-Cf
                if newFlow < 0:
                    newFlow = 0
                G.setEdge(u,v,G.getEdgeDistance(u,v), newFlow)

                # GF
                if Gf.getEdgeDistance(u,v) <= Cf:
                    Gf.deleteEdge(u,v)
                else:
                    Gf.setEdge(u,v,Gf.getEdgeDistance(u,v) - Cf, Gf.getEdgeFlow(u,v))
                if Gf.isEdgeExist(v,u):
                    Gf.setEdge(v,u,Gf.getEdgeDistance(v,u) + Cf, Gf.getEdgeFlow(v,u))
                else:
                    Gf.setEdge(v,u,Cf,0)
            ans_f += Cf
            ans_p.append(path_Dijkstra)
    return {'augmentedPath':ans_p,'maximumFlow':ans_f}
                
def test():
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
    ans = FORD_FULKERSON(G,0,3)
    print(ans)

def test2():
    G = DirectedGraph()
    for i in range(4):
        G.addNode(i)
    G.addEdge(0,1,200000000)
    G.addEdge(0,2,200000000)
    G.addEdge(1,2,1)
    G.addEdge(1,3,200000000)
    G.addEdge(2,3,200000000)
    ans = FORD_FULKERSON(G,0,3)
    print(ans)


if __name__ == '__main__':
    test()
