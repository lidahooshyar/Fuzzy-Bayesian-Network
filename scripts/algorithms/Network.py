import networkx as nx
import matplotlib.pyplot as plt
import math
from matplotlib.patches import FancyArrowPatch

G = nx.DiGraph()
nodes = ["Age", "Race", "Physical activity", "Smoking status", "Lung cancer", "Gene expression"]
G.add_nodes_from(nodes)

edges = [
    ("Age", "Physical activity"), 
    ("Age", "Smoking status"), 
    ("Race", "Physical activity"), 
    ("Race", "Smoking status"), 
    ("Physical activity", "Lung cancer"), 
    ("Smoking status", "Lung cancer"),
    ("Gene expression", "Lung cancer")
]
G.add_edges_from(edges)

pos = {
    "Age": (0, 1.15),
    "Race": (1, 1.15),
    "Physical activity": (0, 0),
    "Smoking status": (1, 0),
    "Lung cancer": (0.5, -1.1),
    "Gene expression": (2, 0.3)
}

edge_labels = {
    ("Age", "Physical activity"): "P(Ph|A)",
    ("Age", "Smoking status"): "P(S|A)",
    ("Race", "Physical activity"): "P(Ph|R)",
    ("Race", "Smoking status"): "P(S|R)",
    ("Physical activity", "Lung cancer"): "P(L|Ph)",
    ("Smoking status", "Lung cancer"): "P(L|S)",
    ("Gene expression", "Lung cancer"): "P(L|G)"
}

edge_radii = {
    ("Age", "Physical activity"): (0.09, 0.13),
    ("Age", "Smoking status"): (0.01, 0.098),
    ("Race", "Physical activity"): (0.095, 0.094),
    ("Race", "Smoking status"): (0.08, 0.13),
    ("Physical activity", "Lung cancer"): (0.079, 0.11),
    ("Smoking status", "Lung cancer"): (0.1, 0.11),
    ("Gene expression", "Lung cancer"): (0.1, 0.096)
}

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

plt.rcParams['text.usetex'] = False  
plt.figure(figsize=(8, 6), dpi=100)
plt.gca().set_facecolor("white")


nx.draw_networkx_nodes(G, pos, nodelist=["Age", "Race", "Physical activity", "Smoking status", "Lung cancer"], 
                       node_shape='o', node_size=2200, node_color='#4E91A1', edgecolors='black', linewidths=3)

nx.draw_networkx_nodes(G, pos, nodelist=["Gene expression"], node_shape='s', node_size=2200, 
                       node_color='#E75480', edgecolors='black', linewidths=3)
for edge in G.edges():
    start_center = pos[edge[0]]
    end_center = pos[edge[1]]
 
    start_radius, end_radius = edge_radii[edge]
 
    start_pos, end_pos = calculate_circumference_point(start_center, end_center, start_radius, end_radius)

    arrow = FancyArrowPatch(
        start_pos, end_pos, connectionstyle="arc3,rad=0.0",
        arrowstyle="-|>", color="black", lw=3,
        mutation_scale=15 
    )
    plt.gca().add_patch(arrow)

    if edge == ("Age", "Smoking status"):
        mid_x = (start_pos[0] + end_pos[0]) / 2 - 0.16
        mid_y = (start_pos[1] + end_pos[1]) / 2
    elif edge == ("Race", "Physical activity"):
        mid_x = (start_pos[0] + end_pos[0]) / 2 + 0.19
        mid_y = (start_pos[1] + end_pos[1]) / 2
    elif edge == ("Race", "Smoking status"):
    
        mid_x = (start_pos[0] + end_pos[0]) / 2 + 0.13  
        mid_y = (start_pos[1] + end_pos[1]) / 2
    else:
        mid_x = (start_pos[0] + end_pos[0]) / 2 - 0.14
        mid_y = (start_pos[1] + end_pos[1]) / 2 
    plt.text(mid_x, mid_y, edge_labels[edge], fontsize=18, ha='center', va='center', color='black')
for node, (x, y) in pos.items():
    plt.text(x - 0.13, y, node, fontsize=18, ha='right', va='center', color='black')

plt.xlim(-0.5, 2.5)
plt.ylim(-1.5, 1.5)
plt.axis('off') 
plt.tight_layout()
plt.show()