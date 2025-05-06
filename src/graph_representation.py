import sys
from collections import defaultdict
from bisect import bisect_left
import numpy as np

# Functions which provide adjacency list graph representation
def generate_adjacency_list(nodes):
    adjacency_list = defaultdict(list)
    adj_mat = generate_adjacency_matrix(nodes)

    for u in range(nodes):
        adjacency_list[u]

        for v in range(nodes):
            if adj_mat[u][v] == 1:
                adjacency_list[u].append(v)


    return adjacency_list


def input_adjacency_list(nodes):
    adjacency_list = defaultdict(list)

    for u in range(nodes):
        adjacency_list[u]

        while True:
            try:
                vertices = [int(x) for x in input(f'{u}> ').replace(","," ").split()]
                if any(j < 0 for j in vertices):
                    print("Error: Nodes' labels MUST be greater than zero.")
                    continue
                if any(j > nodes for j in vertices):
                    print("Error: Nodes' labels MUST NOT exceed the defined number of nodes.")
                    continue
                break

            except ValueError:
                print("Node MUST be an integer.")
            except KeyboardInterrupt:
                print('\nKeyboard Interrupt')
                sys.exit(1)
        
        for v in vertices:
            adjacency_list[u].append(v)

    # for debugging
    print(adjacency_list)

    return adjacency_list


# Functions which provide table graph representation
def generate_table(nodes):
    table = []
    adj_mat = generate_adjacency_matrix(nodes)

    for u in range(nodes):
        for v in range(nodes):
            if adj_mat[u][v] == 1:
                table.append((u, v))

    print(adj_mat)

    return table


def input_table(nodes):
    table = []

    for i in range(nodes):
        while True:
            try:
                tmp = [int(x) for x in input(f'{i}> ').replace(","," ").split()]
                if any(j < 0 for j in tmp):
                    print("Error: Nodes' labels MUST be greater than zero.")
                    continue
                if any(j > nodes for j in tmp):
                    print("Error: Nodes' labels MUST NOT exceed the defined number of nodes.")
                    continue
                break

            except ValueError:
                print("Node MUST be an integer.")
            except KeyboardInterrupt:
                print('\nKeyboard Interrupt')
                sys.exit(1)
        
        for num in tmp:
            table.append((i, num))

    # for debugging
    print(table)

    return table


# Functions which provide adjacency matrix graph representation
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


def input_adjacency_matrix(nodes):
    matrix = []

    for i in range(nodes):
        while True:
            try:
                tmp = [int(x) for x in input(f'{i}> ').replace(","," ").split()]
                if any(j < 0 for j in tmp):
                    print("Error: Nodes' labels MUST be greater than zero.")
                    continue
                if any(j > nodes-1 for j in tmp):
                    print("Error: Nodes' labels MUST NOT exceed the defined number of nodes.")
                    continue
                break

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
                matrix[i].append(1)
            else:
                matrix[i].append(0)
    return matrix