
# Since A* is being tested on grid, using Manhattan Distance as the Heuristic
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


# Getting the neighbors (4-direction, up, down, left, right)
def get_neighbors(node, grid):
    x, y = node
    neighbors = []
    directions = [(1,0), (-1,0), (0,1), (0,-1)]

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        # Boundary Check: Stay inside the grid
        if 0 <= nx < len(grid) and 0 <= ny < len(grid):
            # Obstacle check: Don't walk through "walls"
            if grid[nx][ny] != -1:
                neighbors.append((nx, ny))

    return neighbors


