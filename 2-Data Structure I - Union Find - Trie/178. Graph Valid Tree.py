# 178. Graph Valid Tree
# Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

# Example
# Given n = 5 and edges = [[0, 1], [0, 2], [0, 3], [1, 4]], return true.

# Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], return false.

# Notice
# You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.

class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def validTree(self, n, edges):
        # write your code here
        if n - 1 != len(edges):
            return False

        self.father = {i: i for i in range(n)}
        self.size = n

        for a, b in edges:
            self.union(a, b)
        return self.size == 1
        
    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a != root_b:
            self.size -= 1
            self.father[root_a] = root_b
            
    def find(self, node):
        path = []
        while node != self.father[node]:
            path.append(node)
            node = self.father[node]
        
        for n in path:
            self.father[n] = node
        return node 
        

