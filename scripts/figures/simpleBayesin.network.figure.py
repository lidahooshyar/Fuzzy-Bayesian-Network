import networkx as nx
import matplotlib.pyplot as plt
import math
from matplotlib.patches import FancyArrowPatch


G = nx.DiGraph()
nodes = ["A", "B", "C"]
G.add_nodes_from(nodes)

edges = [
    ("A", "C"), 
    ("B", "C")
]
G.add_edges_from(edges)

pos = {
    "A": (0.3, 0),
    "B": (0.7, 0),
    "C": (0.5, -0.5)  
}

edge_labels = {
    ("A", "C"): "P(C|A)",
    ("B", "C"): "P(C|B)"
}

edge_radii = {
    ("A", "C"): (0.064, 0.055),
    ("B", "C"): (0.064, 0.055)
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

plt.figure(figsize=(8, 8), dpi=100)
plt.gca().set_facecolor("white")

nx.draw_networkx_nodes(G, pos, nodelist=["A", "B", "C"], 
                       node_shape='o', node_size=3000, node_color="#2090A3", 
                       edgecolors='black', linewidths=2.5)
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
    if edge == ("B", "C"):
        mid_x = (start_pos[0] + end_pos[0]) / 2 - 0.05 
        mid_y = (start_pos[1] + end_pos[1]) / 2
    elif edge == ("A", "C"):
        mid_x = (start_pos[0] + end_pos[0]) / 2 - 0.05 
        mid_y = (start_pos[1] + end_pos[1]) / 2
    else:
        mid_x = (start_pos[0] + end_pos[0]) / 2
        mid_y = (start_pos[1] + end_pos[1]) / 2

    plt.text(mid_x, mid_y, edge_labels[edge], fontsize=18, ha='center', va='center', color='black')

for node, (x, y) in pos.items():
    plt.text(x - 0.08, y, node, fontsize=18, ha='right', va='center', color='black')

plt.xlim(-0.2, 1.2)
plt.ylim(-1.0, 0.2)
plt.axis('off') 
plt.tight_layout()
plt.show()
