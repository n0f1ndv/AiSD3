from adjacency_matrix_represenation import generate_adjacency_matrix
import sys

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


def generate_table(nodes):
    table = []
    adj_mat = generate_adjacency_matrix(nodes)

    for u in range(nodes):
        for v in range(nodes):
            if adj_mat[u][v] == 1:
                table.append((u, v))

    print(adj_mat)

    return table


def input_table(nodes):
    table = []

    for u in range(nodes):
        vertices = get_vertices(u, nodes)
        
        for num in vertices:
            table.append((u, num))

    # for debugging
    print(table)

    return table