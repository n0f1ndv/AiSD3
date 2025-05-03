from collections import defaultdict

def generate_adjacency_list():
    pass

def input_adjacency_list(nodes):
    adjacency_list = defaultdict(list)

    for u in range(nodes):
        vertices = [int(x) for x in input(f'{u}> ').split()]
        
        for v in vertices:
            adjacency_list[u].append(v)

    # for debugging
    print(adjacency_list)

    return adjacency_list

def print_adjacency_list(graph):
    for u, v in graph.items():
        print(f'{u}-> {v}')

def adjacency_list_find(graph, start, end):
    exists = False

    print(graph[start])
    for v in graph[start]:
        print(v)
        if v == end:
            exists = True
            break

    if exists == True:
        print(f'True: Edge {(start, end)} exists in the Graph.')
    else:
        print(f'False: Edge {(start, end)} doesn\'t exist in the Graph.')
            


def adjacency_list_bfs():
    pass

def adjacency_list_dfs():
    pass

def adjacency_list_kahn():
    pass

def adjacency_list_tarjan():
    pass