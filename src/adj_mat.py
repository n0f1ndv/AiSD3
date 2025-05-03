from bisect import bisect_left
import numpy as np

def generate_adjacency_matrix(nodes):
    adj_matrix=[]
    sat = int(input('saturation> '))
    max_ver = int(nodes*(nodes-1)/2)
    sat_ver=int(round(max_ver*sat/100,0))
    verses = np.random.choice(range(0, max_ver), size=sat_ver, replace=False)
    k=0
    for i in range(nodes):
        adj_matrix.append([])
        for j in range(nodes):
            if j>i:
                if k in verses:
                    adj_matrix[i].append(1)
                else:
                    adj_matrix[i].append(0)
                k=k+1
            else:
                adj_matrix[i].append(0)
    return adj_matrix

def input_adjacency_matrix(nodes):
    matrix = []

    for i in range(1,nodes+1):
        tmp = [int(x) for x in input(f'{i}> ').split()]
        tmp.sort()
        matrix.append([])
        for num in range(1, nodes + 1):
            # Wyszukiwanie binarne w liście tmp
            index = bisect_left(tmp, num)
            if index < len(tmp) and tmp[index] == num:
                matrix[i - 1].append(1)
            else:
                matrix[i - 1].append(0)
    return matrix

def print_adjacency_matrix(matrix):
    size = len(matrix)
    print("  | ", end="")
    for i in range(1,size+1): print(F"{i} ",end='')
    print()
    print("--+",end="")
    print("--"*size)
    for i in range(size): 
        print(f"{i+1} |",end='')
        for j in matrix[i]:
            print(f" {j}",end="")
        print()

def adjacency_matrix_find(graph, start, end):
    if graph[start-1][end-1]==1:
        print(f'True: Edge {(start, end)} exists in the Graph.')
    else:
        print(f'False: Edge {(start, end)} doesn\'t exist in the Graph.')

def adjacency_matrix_bfs(matrix,start=0):
    lst=[]
    n = len(matrix)
    visited = [False] * n
    queue = []

    visited[start] = True
    queue.append(start)

    while queue:
        v = queue.pop()
        lst.append(v+1)

        for i in range(n):
            if matrix[v][i] == 1 and not visited[i]:
                visited[i] = True
                queue.insert(0,i)
    print('Breath-first search order:')
    print(*lst)

def adjacency_matrix_dfs(graph):
    lst=[]
    n = len(graph)
    visited = [False] * n

    dfs_matrix(visited,graph, lst)
    print('Depth-first search order:')
    print(*lst)

def adjacency_matrix_kahn():
    pass

def adjcacency_matrix_tarjan():
    pass

def dfs_matrix(visited, matrix, lst, v=0):
    visited[v] = True
    lst.append(v+1)

    for i in range(len(matrix)):
        if matrix[v][i] == 1 and not visited[i]:
            dfs_matrix(visited, matrix, lst, i)