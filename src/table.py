from collections import defaultdict, deque

def generate_table():
    pass


def input_table():
    table = []

    while True:
        try:
            nodes = int(input('nodes> '))
        except ValueError:
            print('Number of nodes MUST be an integer')
            continue
        else:
            break

    for i in range(nodes):
        tmp = [int(x) for x in input(f'{i}> ').split()]
        
        for num in tmp:
            table.append((i, num))

    # for debugging
    print(table)

    return table


def vertices(graph):
    unique_vertices = set()

    for u, v in graph:
        unique_vertices.add(u)
        unique_vertices.add(v)

    return list(unique_vertices)


def print_table(graph):
    for edge in graph:
        print(edge)


def table_find(graph, start, end):
    exists = False

    for edge in graph:
        if start == edge[0] and end == edge[1]:
            exists = True
            break

    if exists == True:
        print(f'True: Edge {(start, end)} exists in the Graph.')
    else:
        print(f'False: Edge {(start, end)} doesn\'t exist in the Graph.')


def get_neighbors(graph, vertex):
    neighbors = []

    for edge in graph:
        if edge[0] == vertex:
            neighbors.append(edge[1])

    return list(set(neighbors))


def table_bfs(graph, vertex=0):
    print('Breath-first search order:')
    marked = [False for _ in range(len(vertices(graph)))]
    queue = []
    
    queue.append(vertex)
    marked[vertex] = True

    while queue:
        vertex = queue.pop(0)
        print(vertex, end=' ')

        for x in get_neighbors(graph, vertex):
            if not marked[x]:
                queue.append(x)
                marked[x] = True

    print()


def table_dfs(graph, vertex=0):
    print('Depth-first search order:')
    marked = [False for _ in range(len(vertices(graph)))]

    stack = [vertex]
    while stack:
        vertex = stack.pop()
        print(vertex, end=' ')
        marked[vertex] = True

        for x in get_neighbors(graph, vertex):
            if not marked[x]:
                stack.append(x)
                marked[x] = True

    print()


def table_kahn(graph):
    in_degree = defaultdict(int)
    adj = defaultdict(list)

    for u, v in graph:
        adj[u].append(v)
        in_degree[v] += 1

    all_vertices = vertices(graph)
    for v in all_vertices:
        in_degree[v] = in_degree.get(v, 0)

    zero_in_degree = deque([v for v in all_vertices if in_degree[v] == 0])
    
    topo_order = []

    while zero_in_degree:
        current = zero_in_degree.popleft()
        topo_order.append(current)

        for neighbor in adj.get(current, []):
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                zero_in_degree.append(neighbor)

    if len(topo_order) != len(all_vertices):
        print('Graph has at least one cycle')
        return []

    return topo_order


def table_tarjan(graph):
    pass