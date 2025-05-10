import sys
from collections import defaultdict
from adjacency_matrix_represenation import generate_adjacency_matrix

def get_vertices(i, nodes):
    vertices = []

    while True:
        try:
            vertices = [int(x) for x in input(f'{i}> ').replace(',',' ').split()]
            if any(j < 0 for j in vertices):
                print('Error: Nodes\' labels MUST be greater than zero.')
                continue
            if any(j > nodes for j in vertices):
                print('Error: Nodes\' labels MUST NOT exceed the defined number of nodes.')
                continue
            break

        except ValueError:
            print('Node MUST be an integer.')
        except KeyboardInterrupt:
            print('\nKeyboard Interrupt')
            sys.exit(1)

    return vertices


# Functions which provide adjacency list graph representation
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

        vertices = get_vertices(u, nodes)
        
        for v in vertices:
            adjacency_list[u].append(v)

    # for debugging
    print(adjacency_list)

    return adjacency_list