from collections import deque
from bisect import bisect_left
import numpy as np
import sys 
def generate_adjacency_matrix(nodes):
    adj_matrix=[]
    sat=101
    while True:
        try:
            sat = int(input('saturation> '))
            if sat>100 or sat<0:
                print("Saturation has to be beetwen 0 and 100.")
                continue
            break
        except ValueError:
            print("Saturation MUST be an integer")
        except KeyboardInterrupt:
            print("\nKeyboardInterrupt")
            sys.exit(1)
    
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

def dfs_matrix(visited, matrix, lst, v=0):
    visited[v] = True
    lst.append(v+1)

    for i in range(len(matrix)):
        if matrix[v][i] == 1 and not visited[i]:
            dfs_matrix(visited, matrix, lst, i)

def input_adjacency_matrix(nodes):
    matrix = []

    for i in range(1,nodes+1):
        tmp=[]
        while not tmp:
            try:
                tmp = [int(x) for x in input(f'{i}> ').replace(","," ").split()]
                if any(j < 1 for j in tmp):
                    print("Error: Nodes' labels MUST be greater than zero.")
                    tmp=[]
                if any(j > nodes for j in tmp):
                    print("Error: Nodes' labels MUST NOT exceed the defined number of nodes.")
                    tmp=[]

            except ValueError:
                print("Node MUST be an integer.")
            except KeyboardInterrupt:
                print('\nKeyboard Interrupt')
                sys.exit(1)
        
        tmp.sort()
        matrix.append([])
        for num in range(1, nodes + 1):
            # binary search in tmp
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
    for i in range(size): print("-"*(len(str(i))+1),end='')
    print("-")
    for i in range(size): 
        print(f"{i+1} |",end='')
        for j in range(size):
            print(" "*len(str(j+1)),end='')
            print(f"{matrix[i][j]}",end="")
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