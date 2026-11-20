import time
import csv      # for storing the results
from utils.grid_gen import generate_grid
from utils.compare import compare_algorithms
from algorithms.dijkstras import dijkstra
from algorithms.duan_sssp import duan_et_al_sssp


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

            # Duan plots and time
            t0 = time.perf_counter()
            path_duan, nodes_duan, visited_duan = duan_et_al_sssp(grid, start, goal)
            time_duan = time.perf_counter() - t0

            # Dijstras time and plots
            t0 = time.perf_counter()
            path_d, nodes_d, visited_d = dijkstra(grid, start, goal)
            time_d = time.perf_counter() - t0
            nodes_d = len(visited_d)

            print("\n== Duan SSSP ==")
            print(f"Time: {time_duan:.3f}s")
            print(f"Nodes explored: {nodes_duan}")
            path_len_duan = len(path_duan) if path_duan else "None"
            print(f"Path Length: {path_len_duan}")


            print("\nDijkstras")
            print(f"Time: {time_d:.3f}s")
            print(f"Nodes explored: {nodes_d}")
            path_len_d = len(path_d) if path_d else "None"
            print(f"Path Length: {path_len_d}")
    
            # Write Duan SSSP row
            writer.writerow([f"{size}x{size} ", "Duan SSSP", f"{time_duan:.3f}", nodes_duan, path_len_duan])
            # Write Dijkstra row
            writer.writerow([f"{size}x{size} ", "Dijkstra", f"{time_d:.3f}", nodes_d, path_len_d])

            # comparing the plots
            compare_algorithms(grid, path_duan, visited_duan, path_d, visited_d, size)

    print(f"\nResults successfully saved to {csv_filename}!")



if __name__ == "__main__":
    run_multiple_experiments()
    