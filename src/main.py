import argcomplete
import argparse
import sys
from adjacency_list_representation import input_adjacency_list, generate_adjacency_list
from adjacency_matrix_represenation import input_adjacency_matrix, generate_adjacency_matrix
from table_represenation import input_table, generate_table
from menu import menu

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
    if len(sys.argv) !=2 or (sys.argv[1] != "--generate" and sys.argv[1] != "--user-provided"):
        print("Usage: python3 src/main.py --generate/--user-provided.")
        sys.exit(1)
    
    try:
        rep = input('type> ').strip().lower()
        while rep not in ['list', 'matrix', 'table']:
            print('Invalid type. Available options: list, matrix, table.')
            rep = input('type> ').strip().lower()

    except KeyboardInterrupt:
            print('\nKeyboard Interrupt')
            sys.exit(0)

    while True:
        try:
            nodes = int(input('nodes> '))
        except ValueError:
            print('Number of nodes MUST be an integer')
            continue
        except KeyboardInterrupt:
            print("\nKeyboardInterrupt")
            sys.exit(1)
        else:
            break

    if sys.argv[1] == '--generate':
        if rep.lower() == 'list':
            graph = generate_adjacency_list(nodes)
        elif rep.lower() == 'matrix':
            graph = generate_adjacency_matrix(nodes)
        elif rep.lower() == 'table':
            graph = generate_table(nodes)

    elif sys.argv[1] == '--user-provided':
        if rep.lower() == 'list':
            graph = input_adjacency_list(nodes)
        elif rep.lower() == 'matrix':
            graph = input_adjacency_matrix(nodes)
        elif rep.lower() == 'table':
            graph = input_table(nodes)

    menu(graph, rep, nodes-1)


if __name__ == '__main__':
    main()