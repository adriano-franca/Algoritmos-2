import heapq

class Graph:
    def __init__(self, V):
        self.V = V
        self.E = 0
        self.adj = [[] for _ in range(V)]

    def add_edge(self, u, v, weight):
        self.adj[u].append((v, weight))
        
    def Dijkstra(self, source):
        d = [float("inf")] * self.V
        d[source] = 0
        #visited = [False] * self.V

        min_heap = []
        min_heap.append((0, source))

        while min_heap: # O(V)
            cost, working_node = heapq.heappop(min_heap) # O(V*logV)
            if d[working_node]<cost:
                continue

            #visited[working_node] = True
            for neigh, weight in self.adj[working_node]: # O(E)
                if d[working_node]+weight < d[neigh]:
                    d[neigh] = d[working_node]+weight
                    heapq.heappush(min_heap, (d[neigh], neigh))

        return d