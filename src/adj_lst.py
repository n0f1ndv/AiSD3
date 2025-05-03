from collections import defaultdict, deque

def generate_adjacency_list():
    pass


def input_adjacency_list(nodes):
    adjacency_list = defaultdict(list)

    for u in range(nodes):
        adjacency_list[u]

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


def adjacency_list_bfs(graph, vertex=0):
    marked = [False for _ in range(len(graph))]
    queue = []

    queue.append(vertex)
    marked[vertex] = True

    while queue:
        vertex = queue.pop(0)
        print(vertex, end=' ')

        for x in graph[vertex]:
            if not marked[x]:
                queue.append(x)
                marked[x] = True

    print()

def adjacency_list_dfs(graph, vertex=0):
    marked = [False for _ in range(len(graph))]
    stack = []

    stack.append(vertex)

    while stack:
        vertex = stack.pop()
        print(vertex, end=' ')
        marked[vertex] = True

        for x in graph[vertex]:
            if not marked[x]:
                stack.append(x)
                marked[x] = True

    print()


def adjacency_list_kahn(graph):
    zero_in_degree = [0 for _ in range(len(graph))]

    for u in range(len(graph)):
        for v in graph[u]:
            zero_in_degree[v] += 1

    queue = deque([x for x in range(len(graph)) if zero_in_degree[x] == 0])

    topo_sort = []

    while queue:
        vertex = queue.popleft()
        topo_sort.append(vertex)

        for neighbor in graph[vertex]:
            zero_in_degree[neighbor] -= 1
            if zero_in_degree[neighbor] == 0:
                queue.append(neighbor)

    if len(topo_sort) != len(graph):
        print('Graph has at least one cycle')
        return []

    return topo_sort


def adjacency_list_tarjan():
    pass