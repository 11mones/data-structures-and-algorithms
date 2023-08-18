import pytest
from graph_business_trip import Graph, business_trip



def test1():
    g = Graph()
    Pandora = g.add_vertex('Pandora')
    Metroville = g.add_vertex('Metroville')
    Arendelle = g.add_vertex('Arendelle')
    Naboo = g.add_vertex('Naboo')
    Monstropolis = g.add_vertex('Monstropolis')
    Narnia = g.add_vertex('Narnia')

    g.add_edge(Metroville, Pandora, 82)
    g.add_edge(Metroville, Arendelle, 99)
    g.add_edge(Metroville, Narnia, 37)
    g.add_edge(Metroville, Naboo, 26)
    g.add_edge(Metroville, Monstropolis, 105)
    g.add_edge(Pandora, Arendelle, 150)
    g.add_edge(Arendelle, Monstropolis, 42)
    g.add_edge(Naboo, Monstropolis, 73)
    g.add_edge(Narnia, Naboo, 250)

    assert business_trip(g, ["Naboo", "Pandora"]) is None

def test2():
    g = Graph()
    Pandora = g.add_vertex('Pandora')
    Metroville = g.add_vertex('Metroville')
    Arendelle = g.add_vertex('Arendelle')
    Naboo = g.add_vertex('Naboo')
    Monstropolis = g.add_vertex('Monstropolis')
    Narnia = g.add_vertex('Narnia')

    g.add_edge(Metroville, Pandora, 82)
    g.add_edge(Metroville, Arendelle, 99)
    g.add_edge(Metroville, Narnia, 37)
    g.add_edge(Metroville, Naboo, 26)
    g.add_edge(Metroville, Monstropolis, 105)
    g.add_edge(Pandora, Arendelle, 150)
    g.add_edge(Arendelle, Monstropolis, 42)
    g.add_edge(Naboo, Monstropolis, 73)
    g.add_edge(Narnia, Naboo, 250)

    assert business_trip(g, ["Narnia", "Arendelle", "Naboo"]) is None
