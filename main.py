from collections import defaultdict

def build_undirected_graph(edges):
    """ Constructs an undirected graph from a list of edge pairs. """
    graph_dict = defaultdict(set)
    for start, end in edges:
        graph_dict[start].add(end)
        graph_dict[end].add(start)
    return graph_dict

def find_reachable_nodes(graph, initial_node):
    """
    Returns:
      A set of nodes that are reachable from the specified initial node.
    """
    explored = set([initial_node])
    to_explore = set([initial_node])
    while to_explore:
        current = to_explore.pop()
        for adjacent in graph[current]:
            if adjacent not in explored:
                explored.add(adjacent)
                to_explore.add(adjacent)
    return explored

def is_graph_connected(graph):
    if not graph:
        return True
    first_node = next(iter(graph))
    reachable_nodes = find_reachable_nodes(graph, first_node)
    return len(reachable_nodes) == len(graph)

def count_connected_components(graph):
    """
    Returns:
      The number of connected components in the graph.
    """
    seen_nodes = set()
    component_count = 0
    for node in graph:
        if node not in seen_nodes:
            visited = find_reachable_nodes(graph, node)
            seen_nodes.update(visited)
            component_count += 1
    return component_count