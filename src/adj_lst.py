def adjacency_list():
    adj_lst = []
    nodes = int(input('nodes> '))

    for i in range(1, nodes+1):
        tmp = [int(x) for x in input(f'{i}> ').split()]
        
        for num in tmp:
            adj_lst.append((i, num))

    print(adj_lst)

    return adj_lst