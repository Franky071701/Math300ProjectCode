# This is to make a simple grid to compare both algorithms in the same grid
import matplotlib.pyplot as plt

def compare_algorithms(grid, path_a, visited_a, path_d, visited_d, size):

    fig, axes = plt.subplots(1, 2, figsize=(12,6))

    # ======================
    # A*
    # ======================

    ax = axes[0]
    ax.imshow(grid == -1, cmap="Greys")
    ax.scatter(0, 0, color="green", s=90)          # start
    ax.scatter(grid.shape[1]-1, grid.shape[0]-1, color="red", s=90)  # goal

    if visited_a:
        vy, vx = zip(*visited_a)
        ax.scatter(vx, vy, s=1.5, color="deepskyblue", alpha=0.7)
        

    if path_a:
        py, px = zip(*path_a)
        ax.plot(px, py, color="magenta", linewidth=2)

    ax.set_title("A* Search")
    ax.axis("off")

    # ======================
    # DIJKSTRA
    # ======================

    ax = axes[1]
    ax.imshow(grid == -1, cmap="Greys")

    ax.scatter(0, 0, color="green", s=90)          # start
    ax.scatter(grid.shape[1]-1, grid.shape[0]-1, color="red", s=90)  # goal

    if visited_d:
        vy, vx = zip(*visited_d)
        ax.scatter(vx, vy, s=1.5, color="orange", alpha=0.7)

    if path_d:
        py, px = zip(*path_d)
        ax.plot(px, py, color="magenta", linewidth=2)

    ax.set_title("Dijkstra Search")
    ax.axis("off")

    plt.suptitle(f"Grid Size: {size} x {size}", fontsize=12)
    plt.tight_layout()
    plt.show()