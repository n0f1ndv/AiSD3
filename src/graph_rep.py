import numpy as np

def adjacency_matrix():
    nodes = int(input('nodes> '))
    sat = int(input('saturation> '))

    adj_matrix = np.random.randint(0, 2, (nodes, nodes))
    adj_matrix[np.triu_indices(nodes, 1)[::-1]] = 0

    print(*[str(row)[1:-1] for row in adj_matrix], sep='\n')

    return adj_matrix