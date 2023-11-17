# CSE121-Project-Code

## Eulerian Path Finder using Fleury's Algorithm in Python

This Python script provides an implementation of Fleury's Algorithm to find an Eulerian path in a directed graph. The provided code consists of a Graph class with three essential methods:

1. **__init__:** Initializes the graph with a list of vertices.
2. **add_edge(u, v):** Adds a directed edge from vertex u to vertex v in the graph.
3. **eulerian_path_util(start, visited_edges):** A utility function that recursively explores the graph using Fleury's Algorithm, avoiding bridges and marking visited edges.
4. **is_eulerian_path_exist():** Checks whether the graph satisfies the conditions for having an Eulerian path, i.e., every vertex has the same number of incoming and outgoing edges.
5. **eulerian_path():** Calls the utility function to find an Eulerian path and returns the set of visited edges.
