import time
import csv      # for storing the results
from utils.grid_gen import generate_grid
from compare import compare_algorithms
from algorithms.A_star import a_star_search
from algorithms.dijkstras import dijkstra


# initializing some sizes
sizes = [100, 200, 300]

def run_multiple_experiments():
    # opening a csv file
    csv_filename = "algorithm_results.txt"
    with open(csv_filename, mode="w", newline='') as file:
        writer = csv.writer(file, delimiter="\t")
    
    # 2. Write the column headers
        writer.writerow(["Grid Size", "Algorithm", "Time (s)", "Nodes Explored", "Path Length"])
    
        # testing each size 
        for size in sizes:
            print(f"\nGRID SIZE: {size} x {size}")
            print("==============")

            grid = generate_grid(size)

            start = (0, 0)
            goal = (size - 1, size - 1)

            # A* plots and time
            t0 = time.perf_counter()
            path_a, nodes_a, visited_a = a_star_search(grid, start, goal)

            time_a = time.perf_counter() - t0

            # Dijstras time and plots
            t0 = time.perf_counter()
            path_d, visited_d = dijkstra(grid, start, goal)

            time_d = time.perf_counter() - t0
            nodes_d = len(visited_d)

            print("\n== A* ==")
            print(f"Time: {time_a:.3f}s")
            print(f"Nodes explored: {nodes_a}")
            path_len_a = len(path_a) if path_a else "None"
            print(f"Path Length: {path_len_a}")


            print("\nDijkstras")
            print(f"Time: {time_d:.3f}s")
            print(f"Nodes explored: {nodes_d}")
            path_len_d = len(path_d) if path_d else "None"
            print(f"Path Length: {path_len_d}")
    
            # Write A* row
            writer.writerow([f"{size}x{size} ", "A* ", f"{time_a:.3f}", nodes_a, path_len_a])
            # Write Dijkstra row
            writer.writerow([f"{size}x{size} ", "Dijkstra", f"{time_d:.3f}", nodes_d, path_len_d])

            # comparing the plots
            compare_algorithms(grid, path_a, visited_a, path_d, visited_d, size)

    print(f"\nResults successfully saved to {csv_filename}!")



if __name__ == "__main__":
    run_multiple_experiments()
    