class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, value):
        if value not in self.vertices:
            self.vertices[value] = []

    def add_edge(self, vertex1, vertex2, weight=1):
        if vertex1 not in self.vertices or vertex2 not in self.vertices:
            raise ValueError("Both vertices must already be in the graph.")

        self.vertices[vertex1].append({"vertex": vertex2, "weight": weight})
        self.vertices[vertex2].append({"vertex": vertex1, "weight": weight})

    def get_vertices(self):
        return list(self.vertices.keys())

    def get_neighbors(self, vertex):
        if vertex not in self.vertices:
            raise ValueError("Vertex not found in the graph.")
        return self.vertices[vertex]

    def size(self):
        return len(self.vertices)

