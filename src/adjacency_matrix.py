from collections import deque

def print_adjacency_matrix(graph):
    size = len(graph)
    print("  | ", end="")
    for i in range(size): print(F"{i} ",end='')
    print()
    print("--+",end="")
    for i in range(size): print("-"*(len(str(i))+1),end='')
    print("-")
    for i in range(size): 
        print(f"{i} |",end='')
        for j in range(size):
            print(" "*len(str(j+1)),end='')
            print(f"{graph[i][j]}",end="")
        print()


def adjacency_matrix_find(graph, start, end):
    if graph[start][end] == 1:
        return True
    
    return False


def get_zero_in_degree(graph):
    n = len(graph)
    in_degree = [0] * n

    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                in_degree[j] += 1

    return  deque([i for i in range(n) if in_degree[i] == 0])

def adjacency_matrix_bfs(graph,start=0):
    lst = []
    n = len(graph)
    visited = [False] * n
    queue = deque()

    visited[start] = True
    queue.append(start)

    while queue:
        v = queue.popleft()
        lst.append(v)

        for i in range(n):
            if graph[v][i] == 1 and not visited[i]:
                visited[i] = True
                queue.append(i)

    print(*lst)


def adjacency_matrix_dfs(graph):

    def dfs(visited, graph, lst, v=0):
        visited[v] = True
        lst.append(v)

        for i in range(len(graph)):
            if graph[v][i] == 1 and not visited[i]:
                dfs(visited, graph, lst, i)

    lst=[]
    n = len(graph)
    visited = [False] * n

    dfs(visited, graph, lst)
    print(*lst)


def adjacency_matrix_kahn(graph):
    n = len(graph)
    in_degree = [0] * n

    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                in_degree[j] += 1

    queue = deque([i for i in range(n) if in_degree[i] == 0])
    topo_order = []

    while queue:
        u = queue.popleft()
        topo_order.append(u)

        for v in range(n):
            if graph[u][v] == 1:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)

    if len(topo_order) != n:
        print('Graph has at least one cycle')

    return topo_order


def adjcacency_matrix_tarjan(graph):
    n = len(graph)
    top_order = deque([])
    temporary_mark = set()
    permanent_mark = set()

    def visit(v):
        if v in permanent_mark:
            return
        if v in temporary_mark:
            raise ValueError("Graph has at least one cycle")

        temporary_mark.add(v)

        for u in range(n):
            if graph[v][u] == 1:
                visit(u)

        temporary_mark.remove(v)
        permanent_mark.add(v)
        top_order.appendleft(v)

    for v in range(n):
        if v not in permanent_mark:
            visit(v)

    return top_order