import json
import sys
import networkx as nx

def main():
    if len(sys.argv) < 2:
        print("Usage: python myscript.py <json-source>")
        sys.exit(1)

    source = sys.argv[1]

    g = nx.Graph()
    di_g = nx.DiGraph()

    with open(source) as f:
        characters = json.load(f)
        for character in characters:
            rows = character['rows']
            for row in rows:
                start_name = row['name2']
                end_name = row['name']
                relation = row['relation']
                if not start_name in g:
                    g.add_node(start_name)
                    di_g.add_node(start_name)
                if not end_name in g:
                    g.add_node(end_name)
                    di_g.add_node(end_name)
                g.add_edge(start_name, end_name)
                di_g.add_edge(start_name, end_name, relationship=relation)

    nx.write_gml(g, '../data/NarutoGraph.gml')
    nx.write_gml(di_g, '../data/NarutoDiGraph.gml')

if __name__ == "__main__":
    main()