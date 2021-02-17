import unittest
from ps2 import load_map
from graph import Node, Digraph



def directed_dfs(digraph, start, end, max_total_dist, max_dist_outdoors):
    shortest_distance = None

    def DFS_max(graph, start, end, path, shortest_route, current_len, outdoor_len, print_solution):
        nonlocal shortest_distance

        # check if global maximuma exceeded
        if current_len > max_total_dist or outdoor_len > max_dist_outdoors:
            return None

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
                curr_distance_outdoor = int(edge.get_outdoor_distance())
                if shortest_route is None or (shortest_distance is not None and current_len + distance < shortest_distance):
                    new_path = DFS_max(graph, destination, end, path, shortest_route, current_len + distance, outdoor_len + curr_distance_outdoor, print_solution)
                    if new_path is not None:
                        shortest_route = new_path
        return shortest_route

    shortest_path = DFS_max(digraph, start, end, [], None, 0, 0, False)
    if shortest_path is None:
        raise ValueError()
    if shortest_distance is None:
        shortest_distance = 0
    return shortest_path, shortest_distance

graph = load_map("simple_graph.txt")
print(graph)
max_total_dist, max_dist_outdoors = 10, 10
shortest, length = directed_dfs(graph, Node('1'), Node('5'), max_total_dist, max_dist_outdoors)
print(shortest, length)


