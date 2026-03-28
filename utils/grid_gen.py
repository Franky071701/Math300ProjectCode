import random
import numpy as np

# A function that would generate a grid for testing
def generate_grid(size, obstable_prob = 0.2, weight_prob = 0.2):
    # initialzing a grid of 1s (uniform cost)
    grid = np.ones((size, size))

    # the generation of the grid
    for i in range(size):
        for j in range(size):

            r = random.random()
            # if less than the obstacle prob, make it into an obstacle
            if r < obstable_prob:
                grid[i][j] = -1     # obstacle
            # if less than the weight prob, make it into a diffult terrain
            elif r < obstable_prob + weight_prob:
                grid[i][j] = 5      # difficult terrain
    
    return grid

