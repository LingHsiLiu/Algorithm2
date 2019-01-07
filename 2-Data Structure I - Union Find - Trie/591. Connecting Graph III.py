# 591. Connecting Graph III
# Given n nodes in a graph labeled from 1 to n. There is no edges in the graph at beginning.

# You need to support the following method:

# connect(a, b), an edge to connect node a and node b
# query(), Returns the number of connected component in the graph
# Example
# 5 // n = 5
# query() return 5
# connect(1, 2)
# query() return 4
# connect(2, 4)
# query() return 3
# connect(1, 4)
# query() return 3


class ConnectingGraph3:
    """
    @param a: An integer
    @param b: An integer
    @return: nothing
    """
    def __init__(self, n):
        self.size = n
        self.father = {}
        for i in range(1, n + 1):
            self.father[i] = i
            
    def connect(self, a, b):
        # write your code here
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a != root_b:
            self.father[root_a] = root_b
            self.size -= 1

    """
    @return: An integer
    """
    def query(self):
        # write your code here
        return self.size
    
    def find(self, node):
        path = []
        while node != self.father[node]:
            path.append(node)
            node = self.father[node]
        
        for n in path:
            self.father[n] = node
        return node             
