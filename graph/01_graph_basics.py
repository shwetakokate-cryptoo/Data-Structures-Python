"""
==========================================
Graph Basics
==========================================

This program demonstrates the basic
implementation of an undirected graph
using an adjacency list.

Operations:
- Add Vertex
- Add Edge
- Display Graph
"""


class Graph:
    """Represents an undirected graph."""

    def __init__(self):
        self.graph = {}

    # --------------------------------------
    # Add Vertex
    # --------------------------------------

    def add_vertex(self, vertex: str) -> None:
        """Add a new vertex to the graph."""

        if vertex not in self.graph:
            self.graph[vertex] = []

    # --------------------------------------
    # Add Edge
    # --------------------------------------

    def add_edge(self, vertex1: str, vertex2: str) -> None:
        """Create an undirected edge."""

        self.add_vertex(vertex1)
        self.add_vertex(vertex2)

        self.graph[vertex1].append(vertex2)
        self.graph[vertex2].append(vertex1)

    # --------------------------------------
    # Display Graph
    # --------------------------------------

    def display(self) -> None:
        """Display the adjacency list."""

        print("\nGraph (Adjacency List):")

        for vertex in self.graph:
            connections = " -> ".join(self.graph[vertex])
            print(f"{vertex}: {connections}")


# ------------------------------------------
# Main Program
# ------------------------------------------

def main():

    graph = Graph()

    graph.add_edge("A", "B")
    graph.add_edge("A", "C")
    graph.add_edge("B", "C")
    graph.add_edge("B", "D")

    graph.display()


if __name__ == "__main__":
    main()
