# This is going to make an animation showing how both algorithms work

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
import numpy as np

def create_search_gif(grid, visited_nodes, path, filename, title, size):
    fig, ax = plt.subplots(figsize=(6, 6))
    
    # Static elements: The obstacles and the final path
    ax.imshow(grid == -1, cmap="Greys")
    ax.set_title(title)
    ax.axis("off")
    
    # Start and Goal points
    ax.scatter(0, 0, color="green", s=50, label="Start")
    ax.scatter(size-1, size-1, color="red", s=50, label="Goal")

    # This element will be updated in the animation
    scatter = ax.scatter([], [], s=2, color="cyan", alpha=0.5)
    line, = ax.plot([], [], color="magenta", linewidth=2)

    # To make the GIF run at a reasonable speed, we don't animate every single node
    # We take 'steps' (e.g., show 100 new nodes per frame)
    step = max(1, len(visited_nodes) // 50) 
    
    def update(frame):
        # Update the explored nodes up to the current frame
        current_limit = frame * step
        if current_limit < len(visited_nodes):
            nodes = visited_nodes[:current_limit]
            if nodes:
                vy, vx = zip(*nodes)
                scatter.set_offsets(np.c_[vx, vy])
        
        # Once all nodes are shown, draw the final path
        if current_limit >= len(visited_nodes) and path:
            py, px = zip(*path)
            line.set_data(px, py)
            
        return scatter, line

    # Create animation: 60 frames is usually enough for a smooth GIF
    ani = FuncAnimation(fig, update, frames=range(60), blit=True)
    
    # Save as GIF
    writer = PillowWriter(fps=15)
    ani.save(filename, writer=writer)
    plt.close()
    print(f"Animation saved as {filename}")