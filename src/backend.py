import sys

def get_neighbors_to_insert(vertex, nodes):
    vertices = []

    while True:
        try:
            vertices = [int(x) for x in input(f'{vertex}> ').replace(',',' ').split()]
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

def get_vertices(graph):
    unique_vertices = set()

    for u, v in graph:
        unique_vertices.add(u)
        unique_vertices.add(v)

    return list(unique_vertices)