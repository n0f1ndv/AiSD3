def adjacency_list():
    adj_lst = []
    nodes = int(input('nodes> '))

    for i in range(nodes):
        tmp = [int(x) for x in input(f'{i}> ').split()]
        
        for num in tmp:
            adj_lst.append((i, num))

    print(adj_lst)

    return adj_lst


def print_adj_lst(graph):
    pass


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


def adjacency_list_bfs(graph, vertex=0):
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