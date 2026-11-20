# Testing with real data
import numpy as np
import matplotlib.pyplot as plt
import osmnx as ox
import networkx as nx
import csv
import time
import traceback
import os

from utils.compare import compare_algorithms # use later
from utils.algo_helpers_RealData import create_graph_gif, get_coords
from algorithms.duan_sssp_on_graph import duan_sssp_on_graph
from algorithms.dijkstras_on_graph import dijkstra_on_graph

def run_real_data():
        csv_filename = "real_data_results.txt"
    
        # Setting up the Graph Data
        print("Testing Duan's SSSP vs Dijkstra with Richland Real Data...")
        place = "Richland, Washington, USA"

        # Show Overpass progress/retries in the terminal
        ox.settings.log_console = True
        

        graph_file = "richland_drive.graphml"
        if os.path.exists(graph_file):
            print("Loading cached graph...")
            graph = ox.load_graphml(graph_file)
        else:
            print("Downloading graph from Overpass...")
            # Midpoint between WSU Tri-Cities and Columbia Center Mall (7.5 km radius)
            #center = (46.278, -119.2435)
            center = (46.2970, -119.1926) #shifted center to avoid missing roads in the graph
            graph = ox.graph_from_point(center, dist=8500, network_type='drive')
            ox.save_graphml(graph, graph_file)

        start_lat_lon = (46.33, -119.26)    # wsu tri cities campus
        #goal_lat_lon = (46.226, -119.227)   # columbia center mall
        goal_lat_lon = (46.2647, -119.1190)   # Tri-cities Airport
        start_node = ox.nearest_nodes(graph, start_lat_lon[1], start_lat_lon[0])
        goal_node = ox.nearest_nodes(graph, goal_lat_lon[1], goal_lat_lon[0])
        
        # Running Duan's SSSP
        start_time_duan = time.perf_counter()
        path_duan, count_duan, visited_duan = duan_sssp_on_graph(graph, start_node, goal_node)
        end_time_duan = time.perf_counter()
        duration_duan = end_time_duan - start_time_duan

        # Running Dijkstras
        start_time_dijkstra = time.perf_counter()
        path_dijkstra, count_dijkstra, visited_dijkstra = dijkstra_on_graph(graph, start_node, goal_node)
        end_time_dijkstra = time.perf_counter()
        duration_dijkstra = end_time_dijkstra - start_time_dijkstra

        if path_dijkstra and path_duan:
            print(f"Paths match in length: {len(path_dijkstra) == len(path_duan)}")

        # Opening a file and writing data
        # Using 'a' (append) if you want to keep old results, or 'w' to overwrite
        with open(csv_filename, mode="w", newline='') as file:
            writer = csv.writer(file, delimiter="\t")
            writer.writerow(["Location", "Algorithm", "Time (s)", "Nodes Explored", "Path Length"])
        
            if path_dijkstra:
                print(f"Dijkstra SUCCESS! Time: {duration_dijkstra:.4f}s, Nodes: {count_dijkstra}")
                writer.writerow([place, "Dijkstra", f"{duration_dijkstra:.4f}", count_dijkstra, len(path_dijkstra)])
                create_graph_gif(graph, visited_dijkstra, path_dijkstra, "dijkstra_richland.gif")
            else:
                writer.writerow([place, "Dijkstra", "N/A", count_dijkstra, "0"])

            if path_duan:
                print(f"Duan SSSP SUCCESS! Time: {duration_duan:.4f}s, Nodes: {count_duan}")
                writer.writerow([place, "Duan SSSP", f"{duration_duan:.4f}", count_duan, len(path_duan)])
                create_graph_gif(graph, visited_duan, path_duan, "duan_sssp_richland.gif")
            else:
                writer.writerow([place, "Duan SSSP", "N/A", count_duan, "0"])

if __name__ == "__main__":
    run_real_data()