from collections import defaultdict, deque
from adj_mat import generate_adjacency_matrix
import sys

def generate_adjacency_list(nodes):
    adjacency_list = defaultdict(list)
    adj_mat = generate_adjacency_matrix(nodes)

    for u in range(nodes):
        for v in range(nodes):
            if adj_mat[u][v] == 1:
                adjacency_list[u].append(v)

    return adjacency_list


def input_adjacency_list(nodes):
    adjacency_list = defaultdict(list)

    for u in range(nodes):
        adjacency_list[u]

        while True:
            try:
                vertices = [int(x) for x in input(f'{u}> ').replace(","," ").split()]
                if any(j < 0 for j in vertices):
                    print("Error: Nodes' labels MUST be greater than zero.")
                    continue
                if any(j > nodes for j in vertices):
                    print("Error: Nodes' labels MUST NOT exceed the defined number of nodes.")
                    continue
                break

            except ValueError:
                print("Node MUST be an integer.")
            except KeyboardInterrupt:
                print('\nKeyboard Interrupt')
                sys.exit(1)
        
        for v in vertices:
            adjacency_list[u].append(v)

    # for debugging
    print(adjacency_list)

    return adjacency_list


def print_adjacency_list(graph):
    print('Adjacency list:')
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


def adjacency_list_bfs(graph, vertex=0):
    visited = [False for _ in range(len(graph))]
    queue = []

    queue.append(vertex)
    visited[vertex] = True

    while queue:
        vertex = queue.pop(0)
        print(vertex, end=' ')

        for x in graph[vertex]:
            if not visited[x]:
                queue.append(x)
                visited[x] = True

    print()

def adjacency_list_dfs(graph, vertex=0):
    visited = [False for _ in range(len(graph))]
    stack = []

    stack.append(vertex)

    while stack:
        vertex = stack.pop()
        print(vertex, end=' ')
        visited[vertex] = True

        for x in graph[vertex]:
            if not visited[x]:
                stack.append(x)
                visited[x] = True

    print()


def adjacency_list_kahn(graph):
    in_degree = [0 for _ in range(len(graph))]

    for u in range(len(graph)):
        for v in graph[u]:
            in_degree[v] += 1

    queue = deque([x for x in range(len(graph)) if in_degree[x] == 0])

    topo_sort = []

    while queue:
        vertex = queue.popleft()
        topo_sort.append(vertex)

        for neighbor in graph[vertex]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if len(topo_sort) != len(graph):
        print('Graph has at least one cycle')
        return []

    return topo_sort


def adjacency_list_tarjan(graph):
    topo_sort = deque([])

    temporary_mark = set()
    permanent_mark = set()

    def visit(vertex):
        if vertex in permanent_mark:
            return
        if vertex in temporary_mark:
            raise ValueError('Graph has at least one cycle')
        
        temporary_mark.add(vertex)

        for u in graph[vertex]:
            visit(u)

        temporary_mark.remove(vertex)
        permanent_mark.add(vertex)

        topo_sort.appendleft(vertex)
    
    for v in graph:
        if v not in permanent_mark:
            visit(v)

    return topo_sort