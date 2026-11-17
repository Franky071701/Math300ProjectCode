import heapq
import math
from utils.algo_helpers_RealData import get_distance, reconstruct_path

def duan_sssp_on_graph(graph, start, end):
    # Initialize
    pq = [(0, start)]
    distances = {start: 0}
    parent = {}
    visited = []
    closed_set = set()

    # Calculate k based on the number of nodes in the graph
    n = len(graph.nodes)
    k = max(1, int(math.pow(math.log2(n if n > 1 else 2), 1.0 / 3.0)))

    # Loop until the priority queue is empty
    while pq:
        batch = []
        for _ in range(k):
            if not pq:
                break
            current_cost, current = heapq.heappop(pq)

            # If the current node has already been visited, skip it
            if current in closed_set:
                continue

            closed_set.add(current)
            visited.append(current)

            # If we reached the end node, reconstruct the path and return it
            if current == end:
                return reconstruct_path(parent, start, end), len(visited), visited

            batch.append((current_cost, current))
        
        # Process the batch of nodes
        for current_cost, current in batch:
            for neighbor in graph.neighbors(current):
                weight = get_distance(graph, current, neighbor)
                new_cost = current_cost + weight

                # If the neighbor has not been visited or we found a shorter path to it, update its cost and parent
                if neighbor not in distances or new_cost < distances[neighbor]:
                    distances[neighbor] = new_cost
                    parent[neighbor] = current
                    heapq.heappush(pq, (new_cost, neighbor))

    return None, len(visited), visited


