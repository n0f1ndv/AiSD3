def adjacency_list():
    adj_lst = []
    nodes = int(input('nodes> '))

    for i in range(nodes):
        tmp = [int(x) for x in input(f'{i}> ').split()]
        
        for num in tmp:
            adj_lst.append((i, num))

    # for debugging
    print(adj_lst)

    return adj_lst


def print_adj_lst(graph):
    print(graph)


def vertecies(graph):
    lst = []

    for edge in graph:
        if edge[0] not in lst:
            lst.append(edge[0])

    return lst


def neighbours(graph, node):
    lst = []

    for edge in graph:
        if node == edge[0]:
            lst.append(edge[1])

    return lst


def find(graph, start, end):
    exists = False

    for edge in graph:
        if start == edge[0] and end == edge[1]:
            exists = True
            break

    if exists == True:
        print(f'True: Edge {(start, end)} exists in the Graph.')
    else:
        print(f'False: Edge {(start, end)} doesn\'t exist in the Graph.')


def adjacency_list_bfs(graph, vertex=0):
    print('Breath-first search order:')
    marked = [False for _ in range(len(graph))]
    
    queue = [vertex]
    while len(queue) > 0:
        vertex = queue.pop(0)
        if not marked[vertex]:
            print(vertex, end=' ')
            marked[vertex] = True

            for x in neighbours(graph, vertex):
                if not marked[x]:
                    queue.append(x)

    print()


def adjacency_list_dfs(graph, vertex=0):
    print('Depth-first search order:')
    marked = [False for _ in range(len(graph))]

    stack = [vertex]
    while len(stack) > 0:
        vertex = stack.pop()
        if not marked[vertex]:
            print(vertex, end=' ')
            marked[vertex] = True

            for x in neighbours(graph, vertex):
                if not marked[x]:
                    stack.append(x)

    print()