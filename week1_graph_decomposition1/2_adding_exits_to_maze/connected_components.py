#Uses python3

import sys

class Vertex():
    def __init__(self, index):
        self.index = index
        self.neighbours = {}
        self.visited = False
        self.component = None

    def addNeighbour(self, w):
        self.neighbours.update({w : None})

class Graph():
    def __init__(self, edges, vertices):
        self.edges = edges
        self.vertices = vertices
        self.components = 0
    
    def explore(self, V):
        
        V.visited = True
        V.component = self.components

        for v, w in self.edges:
            # find the edges of the vertex in question and explore its neighbour
            if V == w:
                if not v.visited:
                    self.explore(v)
            elif V == v:
                if not w.visited:
                    self.explore(w)
            

    def DFS(self):
    
        for v in self.vertices:
            if not v.visited:
                # explore each component recursively
                self.explore(v)
                self.components += 1

def number_of_components(graph):
    
    graph.DFS()
    return graph.components

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]

    vertices = [Vertex(i) for i in range(n)]

    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))

    adj = []
    for (a, b) in edges:
        adj.append([vertices[a-1], vertices[b-1]])

    graph = Graph(adj, vertices)
    print(number_of_components(graph))
