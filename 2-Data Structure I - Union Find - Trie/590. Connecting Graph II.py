# 590. Connecting Graph II
# Given n nodes in a graph labeled from 1 to n. There is no edges in the graph at beginning.

# You need to support the following method:

# 1. connect(a, b), an edge to connect node a and node b
# 2. query(a), Returns the number of connected component nodes which include node a.
# Example
# 5 // n = 5
# query(1) return 1
# connect(1, 2)
# query(1) return 2
# connect(2, 4)
# query(1) return 3
# connect(1, 4)
# query(1) return 3

class ConnectingGraph2:
    """
    @param: n: An integer
    """
    def __init__(self, n):
        # do intialization if necessary
        self.father = {}
        self.count = {}
        for i in range(1, n+1):
            self.father[i] = i
            self.count[i] = 1

    """
    @param: a: An integer
    @param: b: An integer
    @return: nothing
    """
    def connect(self, a, b):
        # write your code here
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a != root_b:
            self.father[root_a] = root_b
            self.count[root_b] += self.count[root_a]


    """
    @param: a: An integer
    @return: An integer
    """
    def query(self, a):
        # write your code here
        return self.count[self.find(a)]

    def find(self, node):
        path = []
        while node != self.father[node]:
            path.append(node)
            node = self.father[node]
        
        for n in path:
            self.father[n] = node
            
        return node




