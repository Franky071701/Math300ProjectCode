import heapq
from utils.algo_helpers import get_neighbors
# taking in the grid, a start point and the end goal
def dijkstra(grid, start, goal):
    
    #Initialize distances and the priority queue
    distances = {start: 0}
    priority_queue = [(0, start)]
    
    #Tracking path and visited nodes for the visualization
    came_from = {start: None}
    visited = []
    
    while priority_queue:
        current_cost, current_node = heapq.heappop(priority_queue)
        
        #Track the order of travel for visuals
        visited.append(current_node)
        
        #Hit the goal, reconstruct the path backwards and return
        if current_node == goal:
            path = []
            curr = goal
            while curr is not None:
                path.append(curr)
                curr = came_from[curr]
            path.reverse()
            return path, visited
            
        #Optimization check
        if current_cost > distances.get(current_node, float('inf')):
            continue
            
        #Check all neighbors with `get_neighbors` function (Bryan Gave)
        for neighbor in get_neighbors(current_node, grid):
            #The cost to move
            weight = grid[neighbor[0]][neighbor[1]]
            new_cost = current_cost + weight
            
            #New Shorter Path, update it
            if neighbor not in distances or new_cost < distances[neighbor]:
                distances[neighbor] = new_cost
                came_from[neighbor] = current_node
                heapq.heappush(priority_queue, (new_cost, neighbor))
                
    #Return empty path if no path is found, and the visited nodes for visual
    return None, visited


