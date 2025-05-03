from adj_lst import *
from adj_mat import *
from table import *

def menu(graph, rep):
    state = ''

    while True and state != 'exit':            
        try:
            state = input('action> ').strip().lower()

            if state == 'exit':
                print('Closing the program')
                state = 'exit'

            elif state == 'print':
                if rep == 'list':
                    print_adjacency_list(graph)
                elif rep == 'matrix':
                    print_adjacency_matrix(graph)
                elif rep == 'table':
                    print_table(graph)

            elif state == 'find':
                try:
                    start = int(input('start> '))
                    end = int(input('end> '))

                    if rep == 'list':
                        adjacency_list_find(graph, start, end)
                    elif rep == 'matrix':
                        adjacency_matrix_find(graph, start, end)
                    elif rep == 'table':
                        table_find(graph, start, end)
                except ValueError:
                    print('Values must be numbers')

            elif state == 'bfs':
                if rep == 'list':
                    adjacency_list_bfs()
                elif rep == 'matrix':
                    adjacency_matrix_bfs(graph)
                elif rep == 'table':
                    table_bfs(graph)

            elif state == 'dfs':
                if rep == 'list':
                    adjacency_list_dfs()
                elif rep == 'matrix':
                    adjacency_matrix_dfs(graph)
                elif rep == 'table':
                    table_dfs(graph)

            elif state == 'kahn':
                print('Topological order using Kahn\' algorithm: ')
                if rep == 'list':
                    print(adjacency_list_kahn())
                elif rep == 'matrix':
                    print(adjacency_matrix_kahn())
                elif rep == 'table':
                    print(table_kahn(graph))

            elif state == 'tarjan':
                if rep == 'list':
                    print(adjacency_list_kahn)
                elif rep == 'matrix':
                    print(adjcacency_matrix_tarjan)
                elif rep == 'table':
                    print(table_tarjan())

            else:
                print('This commend doesn\'t exist')

        except KeyboardInterrupt:
            state = 'exit'
            print('\nKeyboard Interrupt')