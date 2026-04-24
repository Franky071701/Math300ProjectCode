# Implemeting  A* again but for dealing with the real data
# using the heapq module
import heapq
import networkx as nx
# using the helper functions that were made
from utils.algo_helpers_RealData import haversine, reconstruct_path, get_coords, get_distance

# the A star logic
def a_star_on_graph(graph, start, goal):
    # intializing 
    pq = [(0, start)]
    g_score = {start:0}
    parent = {start: None}
    visited = []
    node_counter = 0

    visited_set = set()

    # looping 
    while pq:
        current = heapq.heappop(pq)[1]   # popping the lowest f_score node

        # preventing counting the same node
        if current in visited_set:
            continue

        node_counter += 1
        visited_set.add(current)
        visited.append(current)         # adding a node to the list of visited

        # if the current node is the goal then return the path
        if current == goal:
            path = reconstruct_path(parent, start, goal) 
            return path, node_counter, visited 
        
        # else, continue searching for the goal
        for neighbor in graph.neighbors(current):
            weight = get_distance(graph, current, neighbor)
            tentative_g = g_score[current] + weight

            # checking if the current neighbor is a better path
            if tentative_g < g_score.get(neighbor, float('inf')):
                parent[neighbor] = current
                g_score[neighbor] = tentative_g

                # calculating the haversine: f = g + h
                h = haversine(get_coords(graph, neighbor), get_coords(graph, goal))
                f = tentative_g + h

                # pushing the node
                heapq.heappush(pq, (f, neighbor))
    
    return None, node_counter, visited  # in case the goal is never found
