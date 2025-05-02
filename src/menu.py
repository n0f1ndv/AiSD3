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
                    print_adj_lst(graph)
                elif rep == 'matrix':
                    pass
                elif rep == 'table':
                    pass

            elif state == 'find':
                try:
                    start = int(input('start> '))
                    end = int(input('end> '))

                    if rep == 'list':
                        find(graph, start, end)
                    elif rep == 'matrix':
                        pass
                    elif rep == 'table':
                        pass
                except ValueError:
                    print('Values must be numbers')

            elif state == 'bfs':
                if rep == 'list':
                    adjacency_list_bfs(graph)
                elif rep == 'matrix':
                    pass
                elif rep == 'table':
                    pass

            elif state == 'dfs':
                if rep == 'list':
                    adjacency_list_dfs(graph)
                elif rep == 'matrix':
                    pass
                elif rep == 'table':
                    pass

            elif state == 'kahn':
                print('Topological order using Kahn\' algorithm: ')
                if rep == 'list':
                    print(adjacency_list_kahn(graph))
                elif rep == 'matrix':
                    pass
                elif rep == 'table':
                    pass

            elif state == 'tarjan':
                if rep == 'list':
                    adjacency_list_dfs(graph)
                elif rep == 'matrix':
                    pass
                elif rep == 'table':
                    pass

            else:
                print('This commend doesn\'t exist')

        except KeyboardInterrupt:
            state = 'exit'
            print('\nKeyboard Interrupt')