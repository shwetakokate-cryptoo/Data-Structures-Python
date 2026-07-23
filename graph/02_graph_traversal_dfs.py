"""
==========================================
Graph Traversal - Depth-First Search (DFS)
==========================================

This program demonstrates Depth-First Search
(DFS) traversal of an undirected graph using
recursion.

Operations:
- Add Vertex
- Add Edge
- DFS Traversal
"""


class Graph:
    """Represents an undirected graph."""

    def __init__(self):
        self.graph = {}

    # --------------------------------------
    # Add Vertex
    # --------------------------------------

    def add_vertex(self, vertex: str) -> None:

        if vertex not in self.graph:
            self.graph[vertex] = []

    # --------------------------------------
    # Add Edge
    # --------------------------------------

    def add_edge(self, vertex1: str, vertex2: str) -> None:

        self.add_vertex(vertex1)
        self.add_vertex(vertex2)

        self.graph[vertex1].append(vertex2)
        self.graph[vertex2].append(vertex1)

    # --------------------------------------
    # Depth-First Search
    # --------------------------------------

    def dfs(self, start: str) -> None:

        visited = set()

        print("DFS Traversal:")

        self._dfs_recursive(start, visited)

        print()

    def _dfs_recursive(
        self,
        vertex: str,
        visited: set
    ) -> None:

        visited.add(vertex)

        print(vertex, end=" ")

        for neighbor in self.graph[vertex]:

            if neighbor not in visited:
                self._dfs_recursive(neighbor, visited)


# ------------------------------------------
# Main Program
# ------------------------------------------

def main():

    graph = Graph()

    graph.add_edge("A", "B")
    graph.add_edge("A", "C")
    graph.add_edge("B", "D")
    graph.add_edge("B", "E")
    graph.add_edge("C", "F")

    graph.dfs("A")


if __name__ == "__main__":
    main()
