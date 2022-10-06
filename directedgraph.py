class Vertex:
    pass
class Edge:
    pass
class DirectedGraph:
    pass

class Edge:
    def __init__(self, fromNode = None, toNode = None, distance = 1, flow = 0) -> None:
        self.fromNode = fromNode
        self.toNode = toNode
        self.distance = distance
        self.flow = flow
           

    def __repr__(self) -> str:
        return 'Edge(Object): {} to {} distance is {}'.format(self.fromNode, self.toNode, self.distance) if self.fromNode != None or self.toNode != None else 'This edge is broken!'

    def setfromNode(self, fromNode) -> None:
        if type(fromNode) == int:
            self.fromNode = fromNode

    def setfromNode(self, fromNode) -> None:
        if type(fromNode) == int:
            self.fromNode = fromNode

    def settoNode(self, toNode) -> None:
        if type(toNode) == int:
            self.toNode = toNode
    
    def settoNode(self, toNode) -> None:
        if type(toNode) == int:
            self.toNode = toNode
    

class Vertex:
    def __init__(self,
                 key = 0,
                 value = 0,
                 ) -> None:

        self.key = key if type(key) == int else 0
        self.value = value
        self.inEdges = []
        self.outEdges = []

    def __repr__(self) -> str:
        return 'Vertex(Object): key = {}'.format(self.key)

    def setKey(self,key) -> None:
        self.key = key if type(key) == int else 0

    def setValue(self, value) -> None:
        self.value = value

    def getNumIndegree(self) -> int:
        return len(self.inEdges)

    def getNumOutdegree(self) -> int:
        return len(self.outEdges)

class DirectedGraph:
    def __init__(self) -> None:
        self.number_of_nodes = 0
        self.number_of_edges = 0
        self.nodeMap = {}

    def __repr__(self) -> str:
        return 'Graph(Object) : num_of_nodes : {} num_of_edges(directed) : {}'.format(self.number_of_nodes, self.number_of_edges)

    def getNodeNumber(self) -> int:
        return self.number_of_nodes
    
    def getEdgeNumber(self) -> int:
        return self.number_of_edges
    
    def isNodeExisted(self, nodekey) -> bool:
        return self.nodeMap.get(nodekey) != None
    
    def isEdgeExist(self, fromNodekey, toNodekey)-> bool:
        if self.isNodeExisted(fromNodekey) and self.isNodeExisted(toNodekey):
            for edge in self.nodeMap[fromNodekey].outEdges:
                if edge.toNode == toNodekey:
                    return True
        else:
            return False

    def getNodeValue(self, nodekey):
        if self.isNodeExisted(nodekey):
            return self.nodeMap[nodekey].value
    
    def getEdgeDistance(self, fromnodekey, tonodekey):
        if self.isEdgeExist(fromnodekey,tonodekey):
            for edge in self.nodeMap[fromnodekey].outEdges:
                if edge.toNode == tonodekey:
                    return edge.distance

    def getEdgeFlow(self, fromnodekey, tonodekey):
        if self.isEdgeExist(fromnodekey,tonodekey):
            for edge in self.nodeMap[fromnodekey].outEdges:
                if edge.toNode == tonodekey:
                    return edge.flow

    def getNodeInNeighbors(self, nodekey) -> list:
        """ [int,int, ... , int] """
        ans = []
        if self.isNodeExisted(nodekey):
            for edge in self.nodeMap[nodekey].inEdges:
                ans.append(edge.fromNode)
            return ans
        else:
            return ans

    def getNodeOutNeighbors(self, nodekey) -> list:
        """ [int,int, ... , int] """
        ans = []
        if self.isNodeExisted(nodekey):
            for edge in self.nodeMap[nodekey].outEdges:
                ans.append(edge.toNode)
            return ans
        else:
            return ans
    
    def addNode(self, nodekey, nodevalue = 0) -> None:
        if not self.isNodeExisted(nodekey):
            newNode = Vertex(key = nodekey, value = nodevalue)
            self.nodeMap[nodekey] = newNode
            self.number_of_nodes += 1
        else:
            self.setNode(nodekey, nodevalue)
    
    def setNode(self, nodekey, nodevalue = 0) -> None:
        if not self.isNodeExisted(nodekey):
            self.addNode(nodekey,nodevalue)
        else:
            ptr = self.nodeMap[nodekey]
            ptr.value = nodevalue
    
    def addEdge(self, fromNodekey, toNodekey, distance = 1, flow = 0) -> None:
        if self.isEdgeExist(fromNodekey,toNodekey):
            return None
        distance = distance if type(distance) == int else 0
        flow = flow if type(flow) == int else 0
        if not self.isNodeExisted(fromNodekey):
            self.addNode(fromNodekey)
        if not self.isNodeExisted(toNodekey):
            self.addNode(toNodekey)

        newEdge = Edge(fromNodekey, toNodekey, distance, flow)
        self.nodeMap[fromNodekey].outEdges.append(newEdge)
        self.nodeMap[toNodekey].inEdges.append(newEdge)
        self.number_of_edges += 1

    def setEdge(self, fromNodekey, toNodekey, distance = 1, flow = 0) -> None:
        distance = distance if type(distance) == int else 0
        flow = flow if type(flow) == int else 0
        if not self.isEdgeExist(fromNodekey, toNodekey):
            self.addEdge(fromNodekey, toNodekey, distance, flow)
        else:
            for edge in self.nodeMap[fromNodekey].outEdges:
                if edge.toNode == toNodekey:
                    edge.distance = distance
                    edge.flow = flow
                    break
    
    def addBiEdge(self, node1, node2, distance = 1, flow = 0) -> None:
        self.addEdge(node1,node2,distance, flow)
        self.addEdge(node2,node1,distance, flow)

    def setBiEdge(self, node1, node2, distance = 1, flow = 0) -> None:
        self.setEdge(node1,node2,distance, flow)
        self.setEdge(node2,node1,distance, flow)

    def deleteNode(self, nodekey) -> None:
        if self.isNodeExisted(nodekey):
            for fromnode in self.getNodeInNeighbors(nodekey):
                self.deleteEdge(fromnode, nodekey)
            for tonode in self.getNodeOutNeighbors(nodekey):
                self.deleteEdge(nodekey, tonode)
            self.nodeMap.pop(nodekey, None)
            self.number_of_nodes -= 1

    def deleteEdge(self, fromNodekey, toNodekey) -> None:
        if self.isEdgeExist(fromNodekey, toNodekey):
            for edge in self.nodeMap[fromNodekey].outEdges:
                if edge.toNode == toNodekey:
                    self.nodeMap[fromNodekey].outEdges.remove(edge)
                    break
            for edge in self.nodeMap[toNodekey].inEdges:
                if edge.fromNode == fromNodekey:
                    self.nodeMap[toNodekey].inEdges.remove(edge)
                    break
            self.number_of_edges -= 1
    
    def deleteBiEdge(self, node1, node2) -> None:
        self.deleteEdge(node1,node2)
        self.deleteEdge(node2,node1)
            
    def getAllNodes(self):
        """get all nodes -> [int,int, ... ,int] """
        return list(self.nodeMap.keys())
    
    def getAllEdges(self):
        """get all edges -> [[int,int], [int,int], ..., [int,int]]"""
        ans = []
        for node in self.nodeMap.keys():
            ptr = self.nodeMap[node]
            for edge in ptr.outEdges:
                ans.append([node, edge.toNode])
        return ans
    
    def getOppoGraph(self):
        ''' all edges directed change'''
        G2 = DirectedGraph()
        for node1 in self.getAllNodes():
            G2.addNode(node1)
            for node2 in self.getNodeOutNeighbors(node1):
                G2.addEdge(node2,node1,distance=self.getEdgeDistance(node1,node2), flow=self.getEdgeFlow(node1,node2))
        return G2
                
    def getSameGraph(self):
        ''' all edges directed change'''
        G2 = DirectedGraph()
        for node1 in self.getAllNodes():
            G2.addNode(node1)
            for node2 in self.getNodeOutNeighbors(node1):
                G2.addEdge(node1,node2,distance=self.getEdgeDistance(node1,node2), flow=self.getEdgeFlow(node1,node2))
        return G2
            
def test():
    a = DirectedGraph()
    for i in range(100):
        a.addNode(i)
    for i in range(100):
        for j in range(100):
            if i < j:
                a.addEdge(i,j)
    print(a)

if __name__ == '__main__':
    test()