import sys
from collections import defaultdict
from adjacency_matrix_represenation import generate_adjacency_matrix
from backend import get_neighbors_to_insert

def generate_adjacency_list(nodes):
    adjacency_list = defaultdict(list)
    adj_mat = generate_adjacency_matrix(nodes)

    for u in range(nodes):
        adjacency_list[u]

        for v in range(nodes):
            if adj_mat[u][v] == 1:
                adjacency_list[u].append(v)


    return adjacency_list


def input_adjacency_list(nodes):
    adjacency_list = []

    for u in range(nodes):
        adjacency_list.append([])

        vertices = get_neighbors_to_insert(u, nodes)
        
        for v in vertices:
            adjacency_list[u].append(v)

    # for debugging
    print(adjacency_list)

    return adjacency_list