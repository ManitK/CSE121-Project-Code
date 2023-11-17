from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def eulerian_path_util(self, start, visited_edges):
        for v in self.graph[start]:
            edge = (start, v)

            if edge not in visited_edges:
                visited_edges.add(edge)
                self.eulerian_path_util(v, visited_edges)

    def is_eulerian_path_exist(self):
        return all(len(self.graph[vertex]) == len([v for u, v in self.graph.keys() if u == vertex]) for vertex in self.vertices)

    def eulerian_path(self):
        if not self.is_eulerian_path_exist():
            return None

        start_vertex = self.vertices[0]
        visited_edges = set()
        self.eulerian_path_util(start_vertex, visited_edges)

        return visited_edges

# Example
vertices = ['A', 'B', 'C', 'D']
edges = [('A', 'B'), ('B', 'C'), ('C', 'A'), ('C', 'D'), ('D', 'A'), ('D', 'B')]

graph = Graph(vertices)
[graph.add_edge(*edge) for edge in edges]

eulerian_path = graph.eulerian_path()

if eulerian_path:
    print("Eulerian Path Exists:")
    [print(edge) for edge in eulerian_path]
else:
    print("No Eulerian Path Exists.")
