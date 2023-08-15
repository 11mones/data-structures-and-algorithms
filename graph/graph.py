class Graph:

    def __init__(self):

        """
        Initialize empty graph.
        """
        
        self.vertices = {}

    def add_vertex(self, value):

        """
        Adding new vertex to the graph, and it takes the value for the new vertex.
        """

        if value not in self.vertices:
            self.vertices[value] = []

    def add_edge(self, vertex1, vertex2, weight=1):

        """
        Add the edge between the vertices in the graph and it takes the first vertex and the second and the weight of the edge,
        if any of the vertexes is not in the graph it raises ValueError

        """
        if vertex1 not in self.vertices or vertex2 not in self.vertices:
            raise ValueError("Both vertices must already be in the graph.")

        self.vertices[vertex1].append({"vertex": vertex2, "weight": weight})
        self.vertices[vertex2].append({"vertex": vertex1, "weight": weight})

    def get_vertices(self):

        """
        Getting a list of the vertices in graph.

        """
        return list(self.vertices.keys())

    def get_neighbors(self, vertex):

        """
        Getting the neighbors of a vertex in the graph and it takes the vertex that we wanna find the neighbour for,
        and it returns list of dictionaries contain neighbours vertxes and their weights, and it raises a ValueError
        if the vertex is not in the graph

        
        """
        if vertex not in self.vertices:
            raise ValueError("Vertex not found in the graph.")
        return self.vertices[vertex]

    def size(self):

        """
        Get number of vertices in the graph.

        """
        return len(self.vertices)
