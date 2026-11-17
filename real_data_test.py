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
from algorithms.duan_sssp_on_graph import duan_sssp_on_graph
from algorithms.dijkstras_on_graph import dijkstra_on_graph

def run_real_data():
        csv_filename = "real_data_results.txt"
    
        # Setting up the Graph Data
        print("Testing Duan's SSSP vs Dijkstra with Richland Real Data...")
        place = "Richland, Washington, USA"
        graph = ox.graph_from_place(place, network_type='walk')

        start_lat_lon = (46.33, -119.26)    # wsu tri cities campus
        goal_lat_lon = (46.226, -119.227)   # columbia center mall
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

        # Opening a file and writing data
        # Using 'a' (append) if you want to keep old results, or 'w' to overwrite
        with open(csv_filename, mode="w", newline='') as file:
        writer = csv.writer(file, delimiter="\t")
        writer.writerow(["Location", "Algorithm", "Time (s)", "Nodes Explored", "Path Length"])
        
        if path_d:
            print(f"Dijkstra SUCCESS! Time: {duration_d:.4f}s, Nodes: {count_d}")
            writer.writerow([place, "Dijkstra", f"{duration_d:.4f}", count_d, len(path_d)])
            create_graph_gif(graph, visited_d, path_d, "dijkstra_richland.gif")
        else:
            writer.writerow([place, "Dijkstra", "N/A", count_d, "0"])

        if path_s:
            print(f"Duan SSSP SUCCESS! Time: {duration_s:.4f}s, Nodes: {count_s}")
            writer.writerow([place, "Duan SSSP", f"{duration_s:.4f}", count_s, len(path_s)])
            create_graph_gif(graph, visited_s, path_s, "duan_sssp_richland.gif")
        else:
            writer.writerow([place, "Duan SSSP", "N/A", count_s, "0"])

if __name__ == "__main__":
    run_real_data()