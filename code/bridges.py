import json
import sys
import networkx as nx

def main():
    if len(sys.argv) < 2:
        print("Usage: python myscript.py <gml-path>")
        sys.exit(1)

    path = sys.argv[1]

    g = nx.read_gml(path)
    bridges = list(nx.bridges(g))
    count = len(bridges)

    print(f'Total Bridges Found: {count}\n')
    for bridge in bridges:
        print(f'{bridge}\n')

if __name__ == "__main__":
    main()