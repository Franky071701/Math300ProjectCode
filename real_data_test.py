# Testing with real data
import numpy as np
import matplotlib.pyplot as plt
import osmnx as ox
import networkx as nx
import csv
import time
import traceback

from algorithms.a_star_on_graph import a_star_on_graph
from compare import compare_algorithms # use later
from utils.algo_helpers_RealData import create_graph_gif, get_coords

def run_real_data():
        csv_filename = "real_data_results.txt"
    
        # Setting up the Graph Data
        print("Testing A* with Richland Real Data...")
        place = "Richland, Washington, USA"
        graph = ox.graph_from_place(place, network_type='walk')

        start_lat_lon = (46.33, -119.26)    # wsu tri cities campus
        goal_lat_lon = (46.226, -119.227)   # columbia center mall
        start_node = ox.nearest_nodes(graph, start_lat_lon[1], start_lat_lon[0])
        goal_node = ox.nearest_nodes(graph, goal_lat_lon[1], goal_lat_lon[0])

        # Running A*
        start_time_a = time.perf_counter()
        path_a, count_a, visited_a = a_star_on_graph(graph, start_node, goal_node)
        end_time_a = time.perf_counter()
        duration = end_time_a - start_time_a

        # Running Dijkstras (NEED TO DO THIS)

        # Opening a file and writing data
        # Using 'a' (append) if you want to keep old results, or 'w' to overwrite
        with open(csv_filename, mode="w", newline='') as file:
            writer = csv.writer(file, delimiter="\t")
            
            # Write Header
            writer.writerow(["Location", "Algorithm", "Time (s)", "Nodes Explored", "Path Length"])
            
            if path_a:
                print(f"SUCCESS! Path found in {duration:.4f} seconds.")
                # Calculating the path length (number of nodes in this case)
                path_len = len(path_a)
                
                # Writing the result row inside the 'with' block
                writer.writerow([place, "A*", f"{duration:.4f}", count_a, path_len])
                
                # Visuals
                fig, ax = ox.plot_graph_route(graph, path_a, route_color="magenta", show=False)
                plt.show()
                create_graph_gif(graph, visited_a, path_a, "a_star_richland.gif")
            else:
                print("FAILURE: No path found.")
                writer.writerow([place, "A*", "N/A", count_a, "0"])

if __name__ == "__main__":
    run_real_data()