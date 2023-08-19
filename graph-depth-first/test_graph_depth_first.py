from graph_depth_first import Graph 
import pytest

@pytest.fixture
def sample_graph():
    graph = Graph()
    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_vertex("C")
    graph.add_vertex("D")
    graph.add_vertex("E")

    graph.add_edge("A", "B")
    graph.add_edge("A", "C")
    graph.add_edge("B", "D")
    graph.add_edge("D", "E")

    return graph

def test_depth_first(sample_graph):
    result = sample_graph.depth_first("A")
    assert result == ["A", "B", "D", "E", "C"]


