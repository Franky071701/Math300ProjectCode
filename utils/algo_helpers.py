import math

def heuristic(a, b):
    # Manhattan distance for grid-based movement
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def get_neighbors(node, grid):
    x, y = node
    neighbors = []
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    # Use len(grid) for rows and len(grid[0]) for columns
    rows = len(grid)
    cols = len(grid[0])

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < rows and 0 <= ny < cols:
            if grid[nx][ny] != -1: # -1 represents obstacles
                neighbors.append((nx, ny))
    return neighbors


# Function using the haversine formula for the real data
def haversine(coord1, coord2):
    # defining the earth's radius
    R = 6371    # in kilometers

    #Extracting Latitude and Longitude
    lat1, lon1 = coord1
    lat2, lon2 = coord2
    
    # Converting all to Radians (Math functions need radians)
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)
    
    # Calculating 'a' (Square of half the chord length)
    a = math.sin(delta_phi/2)**2 + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda/2)**2
    
    # Calculating 'c' (Angular distance in radians)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    
    # Returning distance
    return R * c