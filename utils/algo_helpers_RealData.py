import math
from matplotlib.animation import FuncAnimation, PillowWriter
from matplotlib import pyplot as plt
import osmnx as ox

# Function using the haversine formula for the real data
def haversine(coord1, coord2):
    # defining the earth's radius
    R = 6371000   # in meters

    #Extracting Latitude and Longitude
    lat1, lon1 = coord1
    lat2, lon2 = coord2
    
    # Converting all to Radians (Math functions need radians)
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)
    
    # Calculating 'a' (Square of half the chord length)
    a = math.sin(delta_phi/2)**2 + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda/2)**2
    
    # Calculating 'c' (Angular distance in radians)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    
    # Returning distance
    return R * c

# A helper function that shows the "best" path
def reconstruct_path(parent, start, goal):
    path = []
    current = goal
    while current != start:
        path.append(current)
        current = parent[current]
    path.append(start)
    path.reverse()
    return path

def create_graph_gif(graph, visited_nodes, path, filename):
    # Getting the base positions of all nodes in the city
    # This allows the dots to appear in the right spot on the map
    node_positions = {node: (data['x'], data['y']) for node, data in graph.nodes(data=True)}
    
    # Setting up the plot using OSMnx
    fig, ax = ox.plot_graph(graph, show=False, close=False, edge_color="#333333", node_size=0)

    # ZOOM LOGIC: Use the path nodes to focus the camera
    path_coords = [get_coords(graph, node) for node in path]
    lats, lons = zip(*path_coords)
    
    padding = 0.002 
    ax.set_ylim(min(lats) - padding, max(lats) + padding)
    ax.set_xlim(min(lons) - padding, max(lons) + padding)
    
    scatter = ax.scatter([], [], s=5, color="cyan", alpha=0.3)
    
    step = max(1, len(visited_nodes) // 50)

    # setting a good frame rate
    def update(frame):
        current_limit = frame * step
        nodes_to_show = visited_nodes[:current_limit]
        
        if nodes_to_show:
            # Look up the lat/lon for each visited Node ID
            coords = [node_positions[node] for node in nodes_to_show]
            scatter.set_offsets(coords)
        
        # Draw path at the very end
        if frame == 59 and path:
            ox.plot_graph_route(graph, path, ax=ax, route_color="magenta", node_size=0)
            
        return scatter,

    ani = FuncAnimation(fig, update, frames=80, blit=False)
    ani.save(filename, writer=PillowWriter(fps=15))


# A helper function for getting the distance
def get_distance(graph, u, v):
    data = graph.get_edge_data(u, v)
    if data is None: 
        return float('inf') # No road exists
    # Use .get() to avoid KeyError if 'length' is missing
    return data[0].get('length', 0)

# A helper function for getting the coordinates
def get_coords(graph, node_id):
    lat = graph.nodes[node_id]['y']
    lon = graph.nodes[node_id]['x']
    return (lat, lon)