from adjacency_list import *
from adjacency_matrix import *
from table import *
from export import *
from backend import display_avaialable_actions
import sys

def menu(graph, rep, nodes):
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
                while True:
                    try:
                        start = int(input('start> '))
                        while start > nodes or start < 0:
                            print(f'Start must be between 0 and {nodes}')
                            start = int(input('start> '))
                        end = int(input('end> '))

                        while end > nodes or end < 0:
                            print(f'End must be between 0 and {nodes}')
                            end = int(input('end> '))

                        if rep == 'list':
                            exists = adjacency_list_find(graph, start, end)
                        elif rep == 'matrix':
                            exists = adjacency_matrix_find(graph, start, end)
                        elif rep == 'table':
                            exists = table_find(graph, start, end)

                        if exists == True:
                            print(f'True: Edge {(start, end)} exists in the Graph.')
                        else:
                            print(f'False: Edge {(start, end)} doesn\'t exist in the Graph.')

                        break

                    except ValueError:
                        print('Values must be numbers')
                    except KeyboardInterrupt:
                        print('\nKeyboardInterrupt')
                        sys.exit(1)

            elif state == 'bfs':
                print('Breath-first search order:')
                if rep == 'list':
                    adjacency_list_bfs(graph)
                elif rep == 'matrix':
                    adjacency_matrix_bfs(graph)
                elif rep == 'table':
                    table_bfs(graph)

            elif state == 'dfs':
                print('Depth-first search order:')
                if rep == 'list':
                    adjacency_list_dfs(graph)
                elif rep == 'matrix':
                    adjacency_matrix_dfs(graph)
                elif rep == 'table':
                    table_dfs(graph)

            elif state == 'kahn':
                print('Topological order using Kahn\' algorithm: ')
                if rep == 'list':
                    print(*adjacency_list_kahn(graph))
                elif rep == 'matrix':
                    print(*adjacency_matrix_kahn(graph))
                elif rep == 'table':
                    print(*table_kahn(graph))

            elif state == 'tarjan':
                print('Topological order using Tarjan\' algorithm: ')
                if rep == 'list':
                    print(*adjacency_list_tarjan(graph))
                elif rep == 'matrix':
                    print(*adjcacency_matrix_tarjan(graph))
                elif rep == 'table':
                    print(*table_tarjan(graph))
                    
            elif state == 'export':
                if rep == 'list':
                    adjacency_list_export(graph, nodes+1)
                elif rep == 'matrix':
                    adjcacency_matrix_export(graph, nodes+1)
                elif rep == 'table':
                    table_export(graph, nodes+1)

            elif state == 'help':
                display_avaialable_actions()

            else:
                print('This commend doesn\'t exist')

        except KeyboardInterrupt:
            state = 'exit'
            print('\nKeyboard Interrupt')