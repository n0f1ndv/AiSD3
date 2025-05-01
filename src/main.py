import argcomplete
import argparse
import sys
from graph_rep import *
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
    if sys.argv[1] == '--generate':
        adjacency_matrix()

    menu()


if __name__ == '__main__':
    main()