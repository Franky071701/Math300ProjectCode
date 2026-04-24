# An implementation of A* using python

# using the heapq module for a priority queue, and for pushing/popping nodes
import heapq
# using the helper functions that were made
from utils.algo_helpers_2D import get_neighbors, heuristic


# The actual A* algorithm
def a_star_search(grid, start, goal):
    # initalizing a node visited for the plots
    nodes_count = 0
    nodes_visited = []

    # A priority queue
    count = 0
    pq = [(0, count, start)]    # to prevent tie-breaking issues
   

    # Trackers
    parent = {}
    g_score = {start: 0}

    # Using a set for O(1) lookup speed during the search
    closed_set = set()

    while pq:
        f, _, current = heapq.heappop(pq)
        
        if current in closed_set:
            continue
            
        nodes_count += 1
        nodes_visited.append(current)
        closed_set.add(current)
        
        if current == goal:
            return reconstruct_path(parent, start, goal), nodes_count, nodes_visited

        for neighbor in get_neighbors(current, grid):
            weight = grid[neighbor[0]][neighbor[1]]
            tentative_g_score = g_score[current] + weight

            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                parent[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score = tentative_g_score + heuristic(neighbor, goal)
                count += 1
                heapq.heappush(pq, (f_score, count, neighbor))

    return None, nodes_count, nodes_visited


# A helper function that shows the "best" path of A*
def reconstruct_path(parent, start, goal):
    path = []
    current = goal
    while current != start:
        path.append(current)
        current = parent[current]
    path.append(start)
    path.reverse()
    return path

    

