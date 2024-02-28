import csv
import networkx as nx

def main(path='../data/Champion.csv', destiny='../data/TFTGraph.gml'):
    nodes = []
    with open(path, newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=",")
        for row in reader:
            traits = row['Origin'].replace(' ', '').split(',') + row['Class'].replace(' ', '').split(',')
            nodes.append((row['Champion'],{'Traits': traits, 'Cost': row['Cost']}))
    
    g = nx.Graph()
    g.add_nodes_from(nodes)
    for start in g.nodes(data=True):
        for end in g.nodes(data=True):
            for trait in start[1]['Traits']:
                if start[0] != end[0] and trait in end[1]['Traits']:
                    g.add_edge(start[0] ,end[0])
    
    nx.write_gml(g, destiny)

main()