import numpy as np
import matplotlib.pyplot as plt
M = 80
dt = 1.

# X[i] = vertex i position
X = np.linspace(0, 1, M+1)

# A is the (M+1)x(M+1) galerkin matrix 
A = np.empty((M+1, M+1))

def get_element_matrix(edge_idx):
    element_matrix = np.empty((2, 2))

    element_matrix[0, 0] = -0.5
    element_matrix[0, 1] = 0.5
    element_matrix[1, 0] = -0.5
    element_matrix[1, 1] = 0.5
    
    return element_matrix

# Edges range from 1 to M-1
# Edge i is connected to node i-1 and i
for edge_idx in range(1, M):
    i = edge_idx-1
    j = edge_idx
    
    element_matrix = get_element_matrix(edge_idx)
    A[i,i] += element_matrix[0, 0]
    A[i,j] += element_matrix[0, 1]
    A[j,i] += element_matrix[1, 0]
    A[j,j] += element_matrix[1, 1]


# Solve (I + dtA)mu_{t+1} = mu_t
mu = np.sin(X*2*np.pi)

for i in range(10000):
    mu = np.linalg.solve(np.eye(M+1, M+1) + A*dt, mu)

    plt.clf()
    plt.ylim(-1, 1)
    plt.plot(X, mu)
    plt.pause(0.001)
plt.show()


