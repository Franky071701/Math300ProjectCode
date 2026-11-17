# This is to make a simple grid to compare both algorithms in the same grid
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def compare_algorithms(grid, path_a, visited_a, path_d, visited_d, size):
    # 2 rows, 2 columns
    fig, axes = plt.subplots(2, 2, figsize=(12, 8))

    # ======================
    # Duan SSSP PATH (Top Left)
    # ======================
    ax = axes[0, 0]  # Updated index
    ax.imshow(grid == -1, cmap="Greys")
    ax.scatter(0, 0, color="green", s=90)
    ax.scatter(grid.shape[1]-1, grid.shape[0]-1, color="red", s=90)
    if visited_a:
        vy, vx = zip(*visited_a)
        ax.scatter(vx, vy, s=1.5, color="deepskyblue", alpha=0.7)
    if path_a:
        py, px = zip(*path_a)
        ax.plot(px, py, color="magenta", linewidth=2)
    ax.set_title("Duan SSSP Path")
    ax.axis("off")

    # ======================
    # DIJKSTRA PATH (Top Right)
    # ======================
    ax = axes[0, 1]  # Updated index
    ax.imshow(grid == -1, cmap="Greys")
    ax.scatter(0, 0, color="green", s=90)
    ax.scatter(grid.shape[1]-1, grid.shape[0]-1, color="red", s=90)
    if visited_d:
        vy, vx = zip(*visited_d)
        ax.scatter(vx, vy, s=1.5, color="orange", alpha=0.7)
    if path_d:
        py, px = zip(*path_d)
        ax.plot(px, py, color="magenta", linewidth=2)
    ax.set_title("Dijkstra Search Path")
    ax.axis("off")

    # ======================
    # HEATMAPS (Bottom Row)
    # ======================
    def get_density_matrix(visited, size):
        matrix = np.zeros((size, size))
        for y, x in visited:
            if 0 <= y < size and 0 <= x < size:
                matrix[y, x] += 1
        return matrix

    # Duan SSSP Heatmap (Bottom Left)
    density_a = get_density_matrix(visited_a, size)
    sns.heatmap(density_a, ax=axes[1, 0], cmap="YlOrRd", cbar=False, xticklabels=False, yticklabels=False)
    axes[1, 0].set_title("Duan SSSP Density (Heatmap)")

    # Dijkstra Heatmap (Bottom Right)
    density_d = get_density_matrix(visited_d, size)
    sns.heatmap(density_d, ax=axes[1, 1], cmap="YlOrRd", cbar=False, xticklabels=False, yticklabels=False)
    axes[1, 1].set_title("Dijkstra Search Density (Heatmap)")

    plt.suptitle(f"Performance Analysis: Grid {size}x{size}", fontsize=16)
    plt.tight_layout()
    plt.show()