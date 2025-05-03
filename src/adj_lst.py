from collections import defaultdict, deque

def generate_adjacency_list():
    pass


def input_adjacency_list():
    adj_lst = []
    nodes = int(input('nodes> '))

    for i in range(nodes):
        tmp = [int(x) for x in input(f'{i}> ').split()]
        
        for num in tmp:
            adj_lst.append((i, num))

    # for debugging
    print(adj_lst)

    return adj_lst


def vertices(graph):
    unique_vertices = set()

    for u, v in graph:
        unique_vertices.add(u)
        unique_vertices.add(v)

    return list(unique_vertices)


def print_adjacency_list(graph):
    print(graph)


def adjacency_list_find(graph, start, end):
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
    queue = []
    
    queue.append(vertex)
    marked[vertex] = True

    while queue:
        vertex = queue.pop(0)
        print(vertex, end=' ')

        for x in graph[vertex]:
            if not marked[x]:
                queue.append(x)
                marked[x] = True

    print()

# seems like dfs does not work :(
def adjacency_list_dfs(graph, vertex=0):
    print('Depth-first search order:')
    marked = [False for _ in range(len(graph))]

    stack = [vertex]
    while len(stack) > 0:
        vertex = stack.pop()
        print(vertex, end=' ')
        marked[vertex] = True

        for x in graph[vertex]:
            if not marked[x]:
                stack.append(x)
                marked[x] = True

    print()


def adjacency_list_kahn(graph):
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
        print("Graph has at least one cycle")
        return []

    return topo_order


def adjacency_list_tarjan(graph):
    pass