import heapq
import math
from utils.algo_helpers_2D import get_neighbors

def duan_et_al_sssp(grid, start, goal):
    nodes_count = 0
    nodes_visited = []

    count = 0
    pq = [(0, count, start)]  # (priority, count, node)

    parent = {}
    distances = {start: 0}
    closed_set = set()

    #Calculate the number of rows and columns in the grid
    rows, cols = len(grid), len(grid[0])
    n = rows * cols  # Total number of nodes in the grid
    K = max(1, int(math.pow(math.log2(n if n > 1 else 2), 1.0 / 3.0)))

    #Loop until the priority queue is empty
    while pq:
        batch = []

        for _ in range(K):
            if not pq:
                break

            current_cost, _, current_node = heapq.heappop(pq)

            if current_node in closed_set:
                continue

            nodes_count += 1
            nodes_visited.append(current_node)
            closed_set.add(current_node)

            if current_node == goal:
                return reconstruct_path(parent, start, goal), nodes_count, nodes_visited

            batch.append((current_cost, current_node))

        for current_cost, current in batch:
            for neighbor in get_neighbors(current, grid):
                weight = grid[neighbor[0]][neighbor[1]]
                new_cost = current_cost + weight

                # If the neighbor has not been visited or we found a shorter path to it, update its cost and parent
                if neighbor not in distances or new_cost < distances[neighbor]:
                    distances[neighbor] = new_cost
                    parent[neighbor] = current
                    count += 1
                    heapq.heappush(pq, (new_cost, count, neighbor))

    return None, nodes_count, nodes_visited

def reconstruct_path(parent, start, goal):
    path = []
    current = goal

    while current != start:
        path.append(current)
        current = parent.get(current)

        if current is None:
            return None  # No path found

    path.append(start)
    path.reverse()
    return path
