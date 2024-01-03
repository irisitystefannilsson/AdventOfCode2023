import time
import networkx as nx

import math
import copy

NUMBER_OF_CALLS = 0
LOG_FILE = open('logfile.txt', 'w')
DATA_CACHE = dict()
USED = []
STARTSET = set()


def advent25_1():
    #file = open('input25_example.txt')
    file = open('input25.txt')

    components = dict()
    for line in file:
        line = line.strip('\n')
        comp, conn = line.split(': ')
        connections = conn.split(' ')
        curr = components.get(comp, [])
        for conn in connections:
            curr.append(conn)
            curr2 = components.get(conn, [])
            curr2.append(comp)
            components[conn] = curr2
        components[comp] = curr

    
    G = nx.Graph()
    for k, el in components.items():
        G.add_node(k)
        #print(k, el)

    for k, el in components.items():
        for n in el:
            G.add_edge(k, n)

    cut = nx.minimum_edge_cut(G)
    print(cut)
    for e in cut:
        #print(e[0], e[1])
        G.remove_edge(e[0], e[1])

    n1 = nx.node_connected_component(G, e[0])
    n2 = nx.node_connected_component(G, e[1])

    print(len(n1))
    print(len(n2))
    print(len(n1)*len(n2))
    
        
if __name__ == '__main__':
    start_time = time.time()
    print('Advent 25')
    advent25_1()
    #advent25_2()
    end_time_1 = time.time()
    print("time elapsed: {:.2f}s".format(end_time_1 - start_time))
