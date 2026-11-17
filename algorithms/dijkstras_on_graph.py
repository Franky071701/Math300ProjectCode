import heapq
from utils.algo_helpers_RealData import get_distance, reconstruct_path

# Dijkstra's algorithm implementation for a graph
def dijkstra_on_graph(graph, start, end):
    # Initalize the priority queue with the starting node and its cost (0)
    pq = [(0, start)]
    distances = {start: 0}
    parent = {}
    visited = []
    closed_set = set()

    # Loop until the priority queue is empty
    while pq:
        current_cost, current = heapq.heappop(pq)

        # If the current node has already been visited, skip it
        if current in closed_set:
            continue

        closed_set.add(current)
        visited.append(current)

        # If we reached the end node, reconstruct the path and return it
        if current == end:
            return reconstruct_path(parent, start, end), len(visited), visited

        # Explore the neighbors of the current node
        for neighbor in graph.neighbors(current):
            weight = get_distance(graph, current, neighbor)
            new_cost = current_cost + weight

            # If the neighbor has not been visited or we found a shorter path to it, update its cost and parent
            if neighbor not in distances or new_cost < distances[neighbor]:
                distances[neighbor] = new_cost
                parent[neighbor] = current
                heapq.heappush(pq, (new_cost, neighbor))

    # return none, and the number of visited nodes if the end node is not reachable
    return None, len(visited), visited

