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
                pass

            elif state == 'find':
                pass

            elif state == 'bfs':
                if rep.lower() == 'list':
                    adjacency_list_bfs(graph)

            elif state == 'dfs':
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