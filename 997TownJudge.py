class Graph:
    def __init__(self, V):
        self.V = V
        self.E = 0
        self.adj = [ [] for _ in range(V)]

    def add_edge(self, u, v, w=1):
        self.adj[u].append( (v, w) )
        self.E +=1

    def town_judge(self):
        candidate = -1
        for i in range(1, self.V):
            if len(self.adj[i])==0:
                if candidate!=-1: return -1
                candidate = i
        if candidate==-1: return -1
        
        for i in range(1, self.V):
            if i==candidate: continue
            if (candidate,1) not in self.adj[i]: return -1
        return candidate

class Solution:
    def findJudge(self, n, trust):

        g = Graph(n+1)
        for source, target in trust:
            g.add_edge(source, target)
        return g.town_judge()
        