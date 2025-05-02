import argcomplete
import argparse
import sys
from adj_mat import *
from adj_lst import *
from menu import *

'''
Usage:
python3 main.py --generate
nodes>
saturation>

python3 main.py --user-provided
nodes>
1>
...
x>

representation:
type> [matrix, list, table]

printing graph in selected representation
searching edges

BFS
DFS

Kahn
Tarjan
'''
def main():
    graph = None

    if sys.argv[1] == '--generate':
        graph = adjacency_matrix()
    if sys.argv[1] == '--user-provided':
        graph = adjacency_list()

    menu(graph, 'list')


if __name__ == '__main__':
    main()