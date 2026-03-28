# An implementation of A* using python

# using the heapq module for a priority queue, and for pushing/popping nodes
import heapq
# using the helper functions that were made
from utils.algo_helpers import get_neighbors, heuristic


# The actual A* algorithm
def a_star_search(grid, start, goal):
    # initalizing a node visited for the plots
    nodes_count = 0
    nodes_visited = []

    # A priority queue
    pq = []
    heapq.heappush(pq, (0, start))

    # Trackers
    parent = {}
    g_score = {start: 0}

    while pq:
        # Extracting the node with the lowest priority/cost from the heap, _ is used for ordering in the heap but not needed for the path logic
        _, current = heapq.heappop(pq)   
        # updating the search metrics and visit history    
        nodes_count += 1
        nodes_visited.append(current)
        
        # if the target was reached, then stop immediately 
        if current == goal:
            return reconstruct_path(parent, start, goal), nodes_count, nodes_visited
        # Exploring adjacent tiles
        for neighbor in get_neighbors(current, grid):
            # Calculating the 'tentative' g_score: Current cost + neighbor's weight
            # This accounts for 'difficult terrain' (weight 5) vs 'normal' (weight 1)
            weight = grid[neighbor[0]][neighbor[1]]
            tentative_g_score = g_score[current] + weight

            #If this path to the neighbor is the best we've found so far
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                # Record the better path
                parent[neighbor] = current
                g_score[neighbor] = tentative_g_score
                # f(n) = g(n) + h(n), the "intelligence" of A*
                f_score = tentative_g_score + heuristic(neighbor, goal)
                heapq.heappush(pq, (f_score, neighbor))

    # Return None if the goal is unreachable (surrounded by obstacles)
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

    

