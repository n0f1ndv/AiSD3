from adj_lst import *
from adj_mat import *
from adj_tbl import *

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
                    print_adjacency_matrix
                elif rep == 'table':
                    print_table()

            elif state == 'find':
                try:
                    start = int(input('start> '))
                    end = int(input('end> '))

                    if rep == 'list':
                        adjacency_list_find(graph, start, end)
                    elif rep == 'matrix':
                        adjacency_matrix_find()
                    elif rep == 'table':
                        table_find()
                except ValueError:
                    print('Values must be numbers')

            elif state == 'bfs':
                if rep == 'list':
                    adjacency_list_bfs(graph)
                elif rep == 'matrix':
                    adjacency_matrix_bfs()
                elif rep == 'table':
                    table_bfs()

            elif state == 'dfs':
                if rep == 'list':
                    adjacency_list_dfs(graph)
                elif rep == 'matrix':
                    adjacency_matrix_dfs()
                elif rep == 'table':
                    table_dfs()

            elif state == 'kahn':
                print('Topological order using Kahn\' algorithm: ')
                if rep == 'list':
                    print(adjacency_list_kahn(graph))
                elif rep == 'matrix':
                    print(adjacency_matrix_kahn())
                elif rep == 'table':
                    print(table_kahn())

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