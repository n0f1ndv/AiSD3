import argcomplete
import argparse
import sys
from adj_mat import *
from adj_lst import *
from menu import *

'''
Usage:
python3 main.py --generate
type> list, matrix, table
nodes> Number of vertecies
saturation> How many vertecies are in the graph

python3 main.py --user-provided
!!! DOES NOT CHECK WHETHER GIVEN GRAPH IS ACYCLIC !!!
type> list, matrix, table
nodes>
0>
...
nodes>

Available actions:
print - Prints the graph

find - Search for edge (start, end) in graph
start> Start vertex
end> End vertex

bfs - Breath-first search order

dfs - Depth-first search order

kahn - Topological sort using Kahn algorithm

tarjan - Topological sort using Tarjan algorithm

exit - Exits the program
'''
def main():
    graph = None
    try:
        rep = input('type> ').strip().lower()
        while rep not in ['list', 'matrix', 'table']:
            print('Invalid type. Available options: list, matrix, table.')
            rep = input('type> ').strip().lower()

    except KeyboardInterrupt:
            print('\nKeyboard Interrupt')
            sys.exit(0)

    if sys.argv[1] == '--generate':
        if rep.lower() == 'list':
            graph = adjacency_matrix()
        elif rep.lower() == 'matrix':
            pass
        elif rep.lower() == 'table':
            pass

    if sys.argv[1] == '--user-provided':
        if rep.lower() == 'list':
            graph = adjacency_list()
        elif rep.lower() == 'matrix':
            pass
        elif rep.lower() == 'table':
            pass

    menu(graph, rep)


if __name__ == '__main__':
    main()