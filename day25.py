import time
import networkx as nx


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
    print('Edges to be cut:', cut)
    for e in cut:
        #print(e[0], e[1])
        G.remove_edge(e[0], e[1])

    n1 = nx.node_connected_component(G, e[0])
    n2 = nx.node_connected_component(G, e[1])

    print('Subgraph 1:', len(n1))
    print('Subgraph 2: ',len(n2))
    print('Product:', len(n1)*len(n2))
    
        
if __name__ == '__main__':
    start_time = time.time()
    print('Advent 25')
    advent25_1()
    #advent25_2()
    end_time_1 = time.time()
    print("time elapsed: {:.2f}s".format(end_time_1 - start_time))
