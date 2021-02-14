import unittest
from ps2 import load_map
from graph import Node, Digraph



def shortest_path(graph: Digraph, start, end, print_solution=True):
    shortest_distance = None

    def DFS(graph, start, end, path, shortest_route, current_len, print_solution):
        nonlocal shortest_distance
        path = path + [start]
        if print_solution:
            print(f"Current path: {path}")
        if start == end:  # check if we have reached the destination
            shortest_distance = current_len
            if print_solution:
                print(f"Shortest path found: {path} (len: {current_len})")
            return path

        edges = graph.get_edges_for_node(start)
        for edge in edges:
            destination = edge.get_destination()
            if destination not in path:  # no cycles
                distance = int(edge.get_total_distance())
                if shortest_route is None or (shortest_distance is not None and current_len + distance < shortest_distance):
                    new_path = DFS(graph, destination, end, path, shortest_route, current_len + distance, print_solution)
                    shortest_route = new_path
        return shortest_route

    return DFS(graph, start, end, [], None, 0, print_solution)

graph = load_map("simple_graph.txt")
print(graph)
shortest = shortest_path(graph, Node('1'), Node('5'))
print(shortest)


