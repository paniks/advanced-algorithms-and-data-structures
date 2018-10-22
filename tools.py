def read_graph_structure_scheme(graph_structure_scheme_file, splitter):
    with open(graph_structure_scheme_file, 'r') as file:
        structure = file.readlines()

    file.close()

    structure = [line.split(splitter) for line in structure]

    return structure
