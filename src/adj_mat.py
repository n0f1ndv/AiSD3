import numpy as np

def generate_adjacency_matrix():
    nodes = int(input('nodes> '))
    sat = int(input('saturation> '))

    adj_matrix = np.random.randint(0, 2, (nodes, nodes))
    adj_matrix[np.triu_indices(nodes, 1)[::-1]] = 0

    return adj_matrix

def input_adjacency_matrix():
    pass

def print_adjacency_matrix(matrix):
    print(*[str(row)[1:-1] for row in matrix], sep='\n')

def adjacency_matrix_find():
    pass

def adjacency_matrix_bfs():
    pass

def adjacency_matrix_dfs():
    pass

def adjacency_matrix_kahn():
    pass

def adjcacency_matrix_tarjan():
    pass