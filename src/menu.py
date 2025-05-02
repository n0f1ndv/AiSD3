from adj_lst import *

def menu(graph, rep):
    state = ''

    while True and state != 'exit':            
        try:
            state = input('action> ').lower()

            if state == 'exit':
                print('Closing the program')
                state = 'exit'

            elif state == 'print':
                if rep.lower() == 'list':
                    print_adj_lst(graph)
                elif rep.lower() == 'matrix':
                    pass
                elif rep.lower() == 'table':
                    pass

            elif state == 'find':
                try:
                    start = int(input('start> '))
                    end = int(input('end> '))

                    if rep.lower() == 'list':
                        find(graph, start, end)
                    elif rep.lower() == 'matrix':
                        pass
                    elif rep.lower() == 'table':
                        pass
                except ValueError:
                    print('Values must be numbers')


            elif state == 'bfs':
                if rep.lower() == 'list':
                    adjacency_list_bfs(graph)
                elif rep.lower() == 'matrix':
                    pass
                elif rep.lower() == 'table':
                    pass

            elif state == 'dfs':
                if rep.lower() == 'list':
                    adjacency_list_dfs(graph)
                elif rep.lower() == 'matrix':
                    pass
                elif rep.lower() == 'table':
                    pass

            elif state == 'kahn':
                pass

            elif state == 'tarjan':
                pass

            else:
                print('This commend doesn\'t exist')

        except KeyboardInterrupt:
            state = 'exit'
            print('\nKeyboard Interrupt')