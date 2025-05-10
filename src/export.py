import math

def generate_coordinates(nodes,r=2.5):
    coordinates = []
    for i in range(nodes):
        angle = 2 * math.pi * i / nodes  # Kąt w radianach
        x = round(r * math.cos(angle),1)+r      # Współrzędna x
        y = round(r * math.sin(angle),1)+r      # Współrzędna y
        coordinates.append((x, y))
    return coordinates


def adjacency_list_export(graph,nodes):
    coordinates_list=generate_coordinates(nodes)
    for node in range(nodes):
        print(f"\\node[shape=circle,draw=black] ({node}) at {coordinates_list[node]} {{{node}}};")
    print()
    for node in range(nodes):
        for edge in range(nodes):
            if edge in graph[node]:
                print(f"\\path [->]({node}) edge ({edge});")


def adjcacency_matrix_export(graph,nodes):
    coordinates_matrix=generate_coordinates(nodes)
    for node in range(nodes):
        print(f"\\node[shape=circle,draw=black] ({node}) at {coordinates_matrix[node]} {{{node}}};")
    print()
    for node in range(nodes):
        for edge in range(nodes):
            if graph[node][edge]==1:
                print(f"\\path [->]({node}) edge ({edge});")
    

def table_export(graph,nodes):
    coordinates_list=generate_coordinates(nodes)

    for node in range(nodes):
        print(f"\\node[shape=circle,draw=black] ({node}) at {coordinates_list[node]} {{{node}}};")
    print()
    for node in range(nodes):
        for u in range(nodes):
            if (node,u) in graph:
                print(f"\\path [->]({node}) edge ({u});")