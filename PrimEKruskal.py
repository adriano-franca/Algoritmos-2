class DisjointSets:
    def __init__(self, size):
        self.ds = [i for i in range(size)]

    def set(self, elem):
        if self.ds[elem]!=elem:
            self.ds[elem] = self.set(self.ds[elem])
        return self.ds[elem]

    def union(self, elem1, elem2):
        self.ds[ self.set(elem1) ] = self.set(elem2)


class Graph:
    def __init__(self, V):
        self.V = V
        self.E = 0
        self.adj = [[] for _ in range(V)]

    def add_edge(self, u, v, weight):
        self.adj[u].append((v, weight))
        
    def Kruskal(self):
        edges = []
        for u in range(self.V):
            for v, weight in self.adj[u]:
                edges.append((weight, u, v))
        edges.sort()    #O(E*log E)

        colors = DisjointSets(self.V)

        for weight, u, v in edges:
            if colors.set(u) != colors.set(v):
                mst_sum += weight
                colors.union(u,v)
        
        return mst_sum
        