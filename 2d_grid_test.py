import time
import csv      # for storing the results
import numpy as np
from utils.grid_gen import generate_grid
from compare import compare_algorithms
from algorithms.A_star import a_star_search
from algorithms.dijkstras import dijkstra
from animate_comparison import create_search_gif


# initializing some sizes
sizes = [50, 300, 500, 1000]    # 50 for a visual 300 and 500 for a better test, and 1000 to see how they scale
iterations = 3      # just because too many will take a long time

def run_multiple_experiments():
    # opening a csv file
    csv_filename = "algorithm_averages.txt"
    with open(csv_filename, mode="w", newline='') as file:
        writer = csv.writer(file, delimiter="\t")
    
    # 2. Write the column headers
        writer.writerow(["Grid Size", "Algorithm", "Avg Time (s)", "Avg Nodes", "Avg Path Length"])
    
        # testing each size 
        for size in sizes:
            print(f"\nBENCHMARKING SIZE: {size} x {size} ({iterations} runs)")
            print("==========================================")

            # Lists to store results for averaging
            results_a = {'time': [], 'nodes': [], 'path_len': []}
            results_d = {'time': [], 'nodes': [], 'path_len': []}

            # We only save the LAST grid/path of the loop to show the visual plot
            last_visual_data = {}

            for i in range(iterations):
                grid = generate_grid(size)
                start, goal = (0, 0), (size - 1, size - 1)

                # A* Run
                t0 = time.perf_counter()
                p_a, n_a, v_a = a_star_search(grid, start, goal)
                results_a['time'].append(time.perf_counter() - t0)
                results_a['nodes'].append(n_a)
                if p_a: results_a['path_len'].append(len(p_a))

                # Dijkstra Run
                t0 = time.perf_counter()
                p_d, n_d ,v_d = dijkstra(grid, start, goal)
                results_d['time'].append(time.perf_counter() - t0)
                results_d['nodes'].append(len(v_d))
                if p_d: results_d['path_len'].append(len(p_d))
                
                # Save the very last one for the visual compare_algorithms
                if i == iterations - 1:
                    last_visual_data = (grid, p_a, v_a, p_d, v_d)

            # Create GIFs for the last run of this size
            g, final_pa, final_va, final_pd, final_vd = last_visual_data
            
            if final_pa:
                create_search_gif(g, final_va, final_pa, f"astar_{size}.gif", f"A* Progress {size}x{size}", size)
            if final_pd:
                create_search_gif(g, final_vd, final_pd, f"dijkstra_{size}.gif", f"Dijkstra Progress {size}x{size}", size)

            # Calculate Means
            avg_time_a = np.mean(results_a['time'])
            avg_nodes_a = np.mean(results_a['nodes'])
            avg_path_a = np.mean(results_a['path_len']) if results_a['path_len'] else 0

            avg_time_d = np.mean(results_d['time'])
            avg_nodes_d = np.mean(results_d['nodes'])
            avg_path_d = np.mean(results_d['path_len']) if results_d['path_len'] else 0

            print(f"A* Average Time: {avg_time_a:.4f}s | Nodes: {int(avg_nodes_a)}")
            print(f"Dijkstra Average Time: {avg_time_d:.4f}s | Nodes: {int(avg_nodes_d)}")

            # Write Averages to CSV
            writer.writerow([f"{size}x{size}", "A*", f"{avg_time_a:.4f}", int(avg_nodes_a), f"{avg_path_a:.1f}"])
            writer.writerow([f"{size}x{size}", "Dijkstra", f"{avg_time_d:.4f}", int(avg_nodes_d), f"{avg_path_d:.1f}"])

            # Show the visual for the last run of this size
            compare_algorithms(*last_visual_data, size)

    print(f"\nAverages successfully saved to {csv_filename}!")



if __name__ == "__main__":
    run_multiple_experiments()
    