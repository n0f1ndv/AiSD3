from collections import deque

def dfs_matrix(visited, matrix, lst, v=0):
    visited[v] = True
    lst.append(v+1)

    for i in range(len(matrix)):
        if matrix[v][i] == 1 and not visited[i]:
            dfs_matrix(visited, matrix, lst, i)


def print_adjacency_matrix(matrix):
    size = len(matrix)
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
            print(f"{matrix[i][j]}",end="")
        print()


def adjacency_matrix_find(graph, start, end):
    if graph[start][end]==1:
        print(f'True: Edge {(start, end)} exists in the Graph.')
    else:
        print(f'False: Edge {(start, end)} doesn\'t exist in the Graph.')


def adjacency_matrix_bfs(matrix,start=0):
    lst=[]
    n = len(matrix)
    visited = [False] * n
    queue = deque()

    visited[start] = True
    queue.append(start)

    while queue:
        v = queue.popleft()
        lst.append(v+1)

        for i in range(n):
            if matrix[v][i] == 1 and not visited[i]:
                visited[i] = True
                queue.append(i)
    print(*lst)


def adjacency_matrix_dfs(graph):
    lst=[]
    n = len(graph)
    visited = [False] * n

    dfs_matrix(visited,graph, lst)
    print(*lst)


def adjacency_matrix_kahn(matrix):
    n = len(matrix)
    in_degree = [0] * n

    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                in_degree[j] += 1

    queue = deque([i for i in range(n) if in_degree[i] == 0])
    top_order = []

    while queue:
        u = queue.popleft()
        top_order.append(u+1)

        for v in range(n):
            if matrix[u][v] == 1:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)

    if len(top_order) != n:
        print('Graph has at least one cycle')

    

    return top_order


def adjcacency_matrix_tarjan(matrix):
    n = len(matrix)
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
            if matrix[v][u] == 1:
                visit(u)

        temporary_mark.remove(v)
        permanent_mark.add(v)
        top_order.appendleft(v+1)

    for v in range(n):
        if v not in permanent_mark:
            visit(v)

    return top_order