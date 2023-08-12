import pytest
from graph import Graph

def test_add_vertex():
    graph = Graph()
    graph.add_vertex("A")
    assert "A" in graph.get_vertices()

def test_add_edge():
    graph = Graph()
    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_edge("A", "B")
    assert len(graph.get_neighbors("A")) == 1
    assert len(graph.get_neighbors("B")) == 1

def test_get_vertices():
    graph = Graph()
    graph.add_vertex("A")
    graph.add_vertex("B")
    assert set(graph.get_vertices()) == {"A", "B"}

def test_get_neighbors():
    graph = Graph()
    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_edge("A", "B", 2)
    neighbors = graph.get_neighbors("A")
    assert neighbors[0]["vertex"] == "B"

def test_neighbors_with_weight():
    graph = Graph()
    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_edge("A", "B", 2)
    neighbors = graph.get_neighbors("A")
    assert neighbors[0]["weight"] == 2

def test_size():
    graph = Graph()
    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_vertex("C")
    assert graph.size() == 3
    
def test_one_vertex_and_edge():
    graph = Graph()
    graph.add_vertex("A")
    graph.add_edge("A", "A", 3)
    neighbors = graph.get_neighbors("A")
    assert len(neighbors) == 2  # Expect 2 self-loop neighbors
    assert neighbors[0]["vertex"] == "A"
    assert neighbors[0]["weight"] == 3
    assert neighbors[1]["vertex"] == "A"
    assert neighbors[1]["weight"] == 3


if __name__ == "__main__":
    pytest.main()
