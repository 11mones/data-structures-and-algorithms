from collections import deque

class Queue:
    def __init__(self):
        self.dq = deque()

    def enqueue(self, value):
        self.dq.append(value)

    def dequeue(self):
        return self.dq.popleft()

    def __len__(self):
        return len(self.dq)

class Vertex:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value

class Edge:
    def __init__(self, vertex, weight=0):
        self.weight = weight
        self.vertex = vertex

class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, value):
        vertex = Vertex(value)
        self.adjacency_list[vertex] = []
        return vertex

    def add_edge(self, start_vertex, end_vertex, weight=0):
        edge = Edge(end_vertex, weight)
        self.adjacency_list[start_vertex].append(edge)
        edge = Edge(start_vertex, weight)
        self.adjacency_list[end_vertex].append(edge)

    def get_vertices(self):
        return self.adjacency_list.keys()

    def get_neighbors(self, vertex):
        return self.adjacency_list.get(vertex, [])

    def breadth_first(self, start_vertex):
        result = []
        visited = set()
        q = Queue()

        q.enqueue(start_vertex)
        visited.add(start_vertex)

        while len(q):
            current_vertex = q.dequeue()
            result.append(current_vertex.value)

            neighbors = self.get_neighbors(current_vertex)
            for edge in neighbors:
                neighbor = edge.vertex
                if neighbor not in visited:
                    q.enqueue(neighbor)
                    visited.add(neighbor)

        return result

def business_trip(graph, city_names):


    """
    Calculate the total cost of a business trip between cities if exist.

    Args:
        graph (Graph): The graph representing cities and flight connections.
        city_names (list): A list of city names representing the trip itinerary.

    Returns:
        int or None: The total cost of the trip if all flights are direct, or None if any flight is not available.
    """


    total_cost = 0

    for i in range(len(city_names) - 1):
        current_city = city_names[i]
        next_city = city_names[i + 1]

        neighbors = graph.get_neighbors(Vertex(current_city))  
        direct_flight = False

        for edge in neighbors:
            if edge.vertex.value == next_city:
                total_cost += edge.weight
                direct_flight = True
                break

    if not direct_flight:
        return None

    return total_cost



  

