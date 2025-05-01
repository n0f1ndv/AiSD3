import numpy as np

def adjacency_matrix(nodes, saturation):
    random_matrix = np.random.randint(0, 2, (nodes, nodes))
    random_matrix[np.triu_indices(nodes, 1)[::-1]] = 0

    return random_matrix