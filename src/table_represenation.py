from adjacency_matrix_represenation import generate_adjacency_matrix
from backend import get_neighbors_to_insert
import sys

def generate_table(nodes):
    table = []
    adj_mat = generate_adjacency_matrix(nodes)

    for u in range(nodes):
        for v in range(nodes):
            if adj_mat[u][v] == 1:
                table.append((u, v))

    return table


def input_table(nodes):
    table = []

    for v in range(nodes):
        vertices = get_neighbors_to_insert(v, nodes)
        
        for num in vertices:
            table.append((v, num))

    return table