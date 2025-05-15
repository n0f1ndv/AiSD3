from collections import deque

def print_adjacency_list(graph):
    print('Adjacency list:')
    for u in range(len(graph)):
        tmp = []
        for v in graph[u]:
            tmp.append(v)

        print(f'{u}-> {tmp}')


def adjacency_list_find(graph, start, end):
    exists = False

    print(graph[start])
    for v in graph[start]:
        print(v)
        if v == end:
            exists = True
            break

    return exists 


def get_zero_in_degree(graph):
    in_degree = [0 for _ in range(len(graph))]

    for u in range(len(graph)):
        for v in graph[u]:
            in_degree[v] += 1

    return deque([x for x in range(len(graph)) if in_degree[x] == 0])


def adjacency_list_bfs(graph, vertex=0):
    visited = [False for _ in range(len(graph))]
    queue = []

    # enques vertices which are not accessible from anothers
    for vertex in get_zero_in_degree(graph):
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

    # puts on stack vertices which are not accessible from anothers
    for vertex in get_zero_in_degree(graph):
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
    
    for v in range(len(graph)):
        if v not in permanent_mark:
            visit(v)

    return topo_sort