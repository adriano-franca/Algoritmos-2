class Graph:
    def __init__(self, V):
        self.V = V  
        self.E = 0
        self.adj = [ [] for _ in range(V) ]
    
    def add_edge(self, u, v, w=1):
        self.adj[u].append((v, w))
        self.adj[v].append((u, w))
        self.E+=1
        #print(f"origem: {u} destino: {v}, lista de adjacencias{self.adj}")

    def find_star(self):
        for i in range(1, len(self.adj)):
            if len(self.adj[i]) == self.V-2:
                break
        return i

    '''def dfs(self, node, visited=None):
        if not visited:
            visited = set()
        if node not in visited:
            visited.add(node)
            for neigh in self.adj[node]:
                self.dfs(neigh, visited)
    '''

def findCenter(edges):
    g = Graph(max(max(edge) for edge in edges) + 1)
    for origem, destino in edges:
        g.add_edge(origem, destino)
    return g.find_star()

edges = [[1,2],[2,3],[4,2]]
print(findCenter(edges))