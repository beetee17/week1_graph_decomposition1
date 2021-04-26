#Uses python3

import sys
from collections import defaultdict

class Vertex():
    def __init__(self, index):
        self.index = index
        self.visited = False
        self.component = None

class Graph():
    def __init__(self, edges, vertices):

        # create a dict with vertex as key and list of its neighbours as values
        self.adj = defaultdict(list)

        for (a, b) in edges:
            self.adj[vertices[a-1]].append(vertices[b-1])
            self.adj[vertices[b-1]].append(vertices[a-1])
        
        self.vertices = vertices
        self.components = 0
    
    def explore(self, v):

        # pre-vist block
        v.visited = True
        v.component = self.components

        # explore each neighbour of the vertex 
        for neighbour in self.adj[v]:
            if not neighbour.visited:
                self.explore(neighbour)
        # post-visit block
            

    def DFS(self):
        
        for v in self.vertices:
            # explore each vertex (and its neighbours)
            if not v.visited:
                self.explore(v)
                # once all neighbours of the vertex have been explored, they form a single connected component
                self.components += 1




def reach(graph, x, y):
    graph.DFS()

    return 1 if graph.vertices[x].component == graph.vertices[y].component else 0
    

if __name__ == '__main__':
    input = sys.stdin.read()

    data = list(map(int, input.split()))

    n, m = data[0:2]
    data = data[2:]

    vertices = [Vertex(i) for i in range(n)]

    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))

    x, y = data[2 * m:]

    x, y = x - 1, y - 1

    graph = Graph(edges, vertices)

    print(reach(graph, x, y))
