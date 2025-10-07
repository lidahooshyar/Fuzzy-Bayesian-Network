import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as fuzz

np.random.seed(0)  

data = np.vstack((
    np.random.randn(67, 2) * 0.1 + [0.2, 0.2],  # Cluster near (0.2, 0.2)
    np.random.randn(67, 2) * 0.1 + [0.5, 0.5],  # Cluster near (0.5, 0.5)
    np.random.randn(66, 2) * 0.1 + [0.8, 0.8]   # Cluster near (0.8, 0.8)
))

data = np.transpose(data)

cntr, u, u0, d, jm, p, fpc = fuzz.cluster.cmeans(data, c=3, m=2, error=0.005, maxiter=1000, init=None)

updated_membership_matrix = u

labels = np.argmax(u, axis=0)
centers = cntr

print("Initial Membership Matrix:")
print(u0)

print("\nUpdated Membership Matrix:")
print(updated_membership_matrix)

colors = ['r', 'g', 'b']
cluster_names = ['Low Expression', 'Medium Expression', 'High Expression']

plt.figure(figsize=(10, 8))
for i in range(3):
    plt.scatter(data[0, labels == i], data[1, labels == i], c=colors[i], label=cluster_names[i])

plt.scatter(centers[:, 0], centers[:, 1], c='black', marker='x', s=100, label='Centers')

plt.xlabel('Expression level ')
plt.ylabel('Protein level')

plt.legend()
plt.show()