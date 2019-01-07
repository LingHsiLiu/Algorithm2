# 589. Connecting Graph
# Given n nodes in a graph labeled from 1 to n. There is no edges in the graph at beginning.

# You need to support the following method:

# connect(a, b), add an edge to connect node a and node b`.
# query(a, b), check if two nodes are connected
# Example
# 5 // n = 5
# query(1, 2) return false
# connect(1, 2)
# query(1, 3) return false
# connect(2, 4)
# query(1, 4) return true

class ConnectingGraph:
    """
    @param: n: An integer
    """
    def __init__(self, n):
        # do intialization if necessary
        self.father = {}
        for i in range(1, n + 1):
            self.father[i] = i

    """
    @param: a: An integer
    @param: b: An integer
    @return: nothing
    """
    def connect(self, a, b):
        # write your code here
        self.father[self.find(a)] = self.find(b)

    """
    @param: a: An integer
    @param: b: An integer
    @return: A boolean
    """
    def query(self, a, b):
        # write your code here
        return self.find(a) == self.find(b)
    
    def find(self, node):
        path = []
        while self.father[node] != node:
            path.append(node)
            node = self.father[node]
            
        for n in path:
            self.father[n] = node
        return node 

