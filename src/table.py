from collections import deque

def generate_table(nodes, saturation):
    pass


def input_table(nodes):
    table = []

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
    print('List of edges:')
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
    marked = [False for _ in range(len(vertices(graph)))]
    stack = []

    stack.append(vertex)

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
    vert = vertices(graph)
    in_degree = deque([0 for _ in range(len(vert))])

    for v in vert:
        for edge in graph:
            if edge[1] == v:
                in_degree[v] += 1
    
    queue = deque([x for x in range(len(vert)) if in_degree[x] == 0])

    topo_sort = []

    while queue:
        vertex = queue.popleft()
        topo_sort.append(vertex)

        for neighbor in get_neighbors(graph, vertex):
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if len(topo_sort) != len(vert):
        print('Graph has at least one cycle')
        return []

    return topo_sort


def table_tarjan(graph):
    topo_sort = deque([])

    vert = vertices(graph)

    temporary_mark = set()
    permanent_mark = set()

    def visit(vertex):
        if vertex in permanent_mark:
            return
        if vertex in temporary_mark:
            raise ValueError('Graph has at least one cycle')
        
        temporary_mark.add(vertex)

        for u in get_neighbors(graph, vertex):
            visit(u)

        temporary_mark.remove(vertex)
        permanent_mark.add(vertex)

        topo_sort.appendleft(vertex)
    
    for v in vert:
        if v not in permanent_mark:
            visit(v)

    return topo_sort