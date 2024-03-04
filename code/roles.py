import networkx as nx
from graphrole import RecursiveFeatureExtractor, RoleExtractor
import sys
import json

N_ROLES =  [None, 2]

def get_role_extractor(g, n):
    feature_extractor = RecursiveFeatureExtractor(g)
    features = feature_extractor.extract_features()

    role_extractor = RoleExtractor(n)
    role_extractor.extract_role_factors(features)
    return role_extractor

def save_role_percentages(role_percentages, save_path):
    print(f'\nNode role membership by percentage saved on {save_path}.')
    role_percentages.to_csv(save_path)

def save_roles(roles, save_path):
    save = {}
    for node, role in roles.items():
        if not role in save:
            save[role] = []
        save[role].append(node)

    with open(save_path, 'w') as json_file:
        json.dump(save, json_file)

    print(f"Dictionary saved to {save_path}")


def main():
    if len(sys.argv) < 2:
        print("Usage: python myscript.py <gml-path>.")
        sys.exit(1)

    load_path = sys.argv[1]
    g = nx.read_gml(load_path)

    for n in N_ROLES:
        role_extractor = get_role_extractor(g, n)

        percentages_save_path = f'../data/roles/{n if n!=None else "automatic"}RolesPercentages.csv'
        save_role_percentages(role_extractor.role_percentage, percentages_save_path)

        roles_save_path = f'../data/roles/{n if n!=None else "automatic"}Roles.json'
        save_roles(role_extractor.roles, roles_save_path)


        with open(f'{n if n!=None else "automatic"}RolesFromExtractor.json', 'w') as json_file:
            json.dump(role_extractor.roles, json_file)

        

        

if __name__ == "__main__":
    main()