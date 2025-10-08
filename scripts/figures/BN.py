import networkx as nx
import matplotlib.pyplot as plt
import math
from matplotlib.patches import FancyArrowPatch

# Create directed graph
G = nx.DiGraph()
nodes = ["Age", "Physical activity", "Smoking status", "Lung cancer", "Genes profile"]
G.add_nodes_from(nodes)

edges = [
    ("Age", "Physical activity"), 
    ("Age", "Smoking status"), 
    ("Physical activity", "Lung cancer"), 
    ("Smoking status", "Lung cancer"),
    ("Genes profile", "Lung cancer")
]
G.add_edges_from(edges)

# Node positions
pos = {
    "Age": (0, 1.3),
    "Physical activity": (0, 0),
    "Smoking status": (1.05, 0),
    "Lung cancer": (0.5, -1.1),
    "Genes profile": (1.8, 0.18)
}

# Edge labels (conditional probabilities)
edge_labels = {
    ("Age", "Physical activity"): "P(Ph|A)",
    ("Age", "Smoking status"): "P(S|A)",
    ("Physical activity", "Lung cancer"): "P(L|Ph)",
    ("Smoking status", "Lung cancer"): "P(L|S)",
    ("Genes profile", "Lung cancer"): "P(L|G)"
}

# Edge radii for arrow positioning
edge_radii = {
    ("Age", "Physical activity"): (0.09, 0.17),
    ("Age", "Smoking status"): (0.01, 0.12),
    ("Physical activity", "Lung cancer"): (0.079, 0.14),
    ("Smoking status", "Lung cancer"): (0.1, 0.14),
    ("Genes profile", "Lung cancer"): (0.1, 0.11)
}

# Function to adjust arrow start/end positions based on node radii
def calculate_circumference_point(start, end, start_radius, end_radius):
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    distance = math.sqrt(dx**2 + dy**2)
    if distance != 0:
        offset_x_start = start_radius * dx / distance
        offset_y_start = start_radius * dy / distance
        offset_x_end = end_radius * dx / distance
        offset_y_end = end_radius * dy / distance
        start_pos = (start[0] + offset_x_start, start[1] + offset_y_start)
        end_pos = (end[0] - offset_x_end, end[1] - offset_y_end)
    else:
        start_pos, end_pos = start, end
    return start_pos, end_pos

# Plot setup
plt.rcParams['text.usetex'] = False  
plt.figure(figsize=(15, 20), dpi=100)
plt.gca().set_facecolor("white")

# Draw nodes
nx.draw_networkx_nodes(G, pos, nodelist=["Age", "Physical activity", "Smoking status", "Lung cancer"], 
                       node_shape='o', node_size=3600, node_color="#2090A3", edgecolors='black', linewidths=2.5)
nx.draw_networkx_nodes(G, pos, nodelist=["Genes profile"], node_shape='s', node_size=3600, 
                       node_color="#9FD7EE", edgecolors='black', linewidths=2.5)

# Draw edges with arrows and labels
for edge in G.edges():
    start_center = pos[edge[0]]
    end_center = pos[edge[1]]
    start_radius, end_radius = edge_radii[edge]
    start_pos, end_pos = calculate_circumference_point(start_center, end_center, start_radius, end_radius)

    arrow = FancyArrowPatch(
        start_pos, end_pos, connectionstyle="arc3,rad=0.0",
        arrowstyle="-|>", color="black", lw=2.5,
        mutation_scale=15 
    )
    plt.gca().add_patch(arrow)

    # Adjust edge label position
    if edge == ("Age", "Smoking status"):
        mid_x = (start_pos[0] + end_pos[0]) / 2 - 0.16
        mid_y = (start_pos[1] + end_pos[1]) / 2
    else:
        mid_x = (start_pos[0] + end_pos[0]) / 2 - 0.14
        mid_y = (start_pos[1] + end_pos[1]) / 2 
    plt.text(mid_x, mid_y, edge_labels[edge], fontsize=18, ha='center', va='center', color='black')

# Draw node labels
for node, (x, y) in pos.items():
    plt.text(x - 0.13, y, node, fontsize=18, ha='right', va='center', color='black')

# Set plot limits and remove axes
plt.xlim(-0.5, 2.5)
plt.ylim(-1.5, 1.5)
plt.axis('off') 
plt.tight_layout()
plt.show()
