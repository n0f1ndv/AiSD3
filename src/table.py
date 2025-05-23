from collections import deque
from backend import get_vertices


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

    return exists


def get_neighbors(graph, vertex):
    neighbors = []

    for edge in graph:
        if edge[0] == vertex:
            neighbors.append(edge[1])

    return list(set(neighbors))


def get_zero_in_degree(graph):
    vertices = get_vertices(graph)
    in_degree = deque([0 for _ in range(len(vertices))])

    for v in vertices:
        for edge in graph:
            if edge[1] == v:
                in_degree[v] += 1
    
    return deque([x for x in range(len(vertices)) if in_degree[x] == 0])


def table_bfs(graph, vertex=0):
    visited = [False for _ in range(len(get_vertices(graph)))]
    queue = []
    
    for vertex in get_zero_in_degree(graph):
        queue.append(vertex)
        visited[vertex] = True

    while queue:
        vertex = queue.pop(0)
        print(vertex, end=' ')

        for x in get_neighbors(graph, vertex):
            if not visited[x]:
                queue.append(x)
                visited[x] = True

    print()


def table_dfs(graph, vertex=0):
    visited = [False for _ in range(len(get_vertices(graph)))]
    stack = []

    for vertex in get_zero_in_degree(graph):
        stack.append(vertex)

    while stack:
        vertex = stack.pop()
        print(vertex, end=' ')
        visited[vertex] = True

        for x in get_neighbors(graph, vertex):
            if not visited[x]:
                stack.append(x)
                visited[x] = True

    print()


def table_kahn(graph):
    vertices = get_vertices(graph)
    in_degree = deque([0 for _ in range(len(vertices))])

    for v in vertices:
        for edge in graph:
            if edge[1] == v:
                in_degree[v] += 1
    
    queue = deque([x for x in range(len(vertices)) if in_degree[x] == 0])

    topo_sort = []

    while queue:
        vertex = queue.popleft()
        topo_sort.append(vertex)

        for neighbor in get_neighbors(graph, vertex):
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if len(topo_sort) != len(vertices):
        print('Graph has at least one cycle')
        return []

    return topo_sort


def table_tarjan(graph):
    topo_sort = deque([])

    vert = get_vertices(graph)

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