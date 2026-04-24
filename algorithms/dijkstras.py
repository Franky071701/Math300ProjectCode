import heapq
from utils.algo_helpers_2D import get_neighbors
# taking in the grid, a start point and the end goal
def dijkstra(grid, start, goal):
    nodes_count = 0
    nodes_visited = []
    
    count = 0
    pq = [(0, count, start)]
    
    parent = {}
    distances = {start: 0}
    closed_set = set()

    while pq:
        current_cost, _, current = heapq.heappop(pq)

        if current in closed_set:
            continue

        nodes_count += 1
        nodes_visited.append(current)
        closed_set.add(current)

        if current == goal:
            return reconstruct_path(parent, start, goal), nodes_count, nodes_visited

        for neighbor in get_neighbors(current, grid):
            weight = grid[neighbor[0]][neighbor[1]]
            new_cost = current_cost + weight

            if neighbor not in distances or new_cost < distances[neighbor]:
                distances[neighbor] = new_cost
                parent[neighbor] = current
                count += 1
                heapq.heappush(pq, (new_cost, count, neighbor))

    return None, nodes_count, nodes_visited

# for making the best path
def reconstruct_path(parent, start, goal):
    path = []
    current = goal
    while current != start:
        path.append(current)
        current = parent[current]
    path.append(start)
    path.reverse()
    return path
