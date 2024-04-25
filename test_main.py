from main import *

def test_reachable():
    graph = build_undirected_graph([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'B')])
    assert sorted(find_reachable_nodes(graph, 'A')) == ['A', 'B', 'C', 'D']

    graph = build_undirected_graph([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'B'), ('E', 'F'), ('F', 'G')])
    assert sorted(find_reachable_nodes(graph, 'A')) == ['A', 'B', 'C', 'D']
    assert sorted(find_reachable_nodes(graph, 'E')) == ['E', 'F', 'G']

def test_connected():
    graph = build_undirected_graph([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'B')])
    assert is_graph_connected(graph) == True
    graph = build_undirected_graph([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'B'), ('E', 'F'), ('F', 'G')])
    assert is_graph_connected(graph) == False

def test_n_components():
    graph = build_undirected_graph([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'B')])
    assert count_connected_components(graph) == 1

    graph = build_undirected_graph([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'B'), ('E', 'F'), ('F', 'G')])
    assert count_connected_components(graph) == 2
