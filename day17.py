import time
import numpy as np
import networkx as nx


NUMBER_OF_CALLS = 0
LOG_FILE = open('logfile.txt', 'w')

"""
The idea of building a graph with vertical & horizontal connections of 
different lengths(*) comes from the reddit discussion board user 'thblt'. 
(https://www.reddit.com/r/adventofcode/comments/18zx149/2023_day_17_part_1_wheres_my_mistake/)

(*) the length of the edges is the same as the possible moving intervals
"""

def build_graph(blocks : np.full):
    G = nx.DiGraph()
    bsize = blocks.shape
    for r in range(bsize[0]):
        for c in range(bsize[1]):
            G.add_node((r, c, 'h'))
            G.add_node((r, c, 'v'))

    for r in range(bsize[0]):
        for c in range(bsize[1]):
            if c > 0:
                G.add_edge((r, c, 'h'), (r, c - 1, 'v'), weight=blocks[r, c - 1])
            if c > 1:
                G.add_edge((r, c, 'h'), (r, c - 2, 'v'), weight=blocks[r, c - 1] + blocks[r, c - 2])
            if c > 2:
                G.add_edge((r, c, 'h'), (r, c - 3, 'v'), weight=blocks[r, c - 1] + blocks[r, c - 2] + blocks[r, c - 3])
            if c < bsize[1] - 1:
                G.add_edge((r, c, 'h'), (r, c + 1, 'v'), weight=blocks[r, c + 1])
            if c < bsize[1] - 2 :
                G.add_edge((r, c, 'h'), (r, c + 2, 'v'), weight=blocks[r, c + 1] + blocks[r, c + 2])
            if c < bsize[1] - 3:
                G.add_edge((r, c, 'h'), (r, c + 3, 'v'), weight=blocks[r, c + 1] + blocks[r, c + 2] + blocks[r, c + 3])
            #
            if r > 0:
                G.add_edge((r, c, 'v'), (r - 1, c, 'h'), weight=blocks[r - 1, c])
            if r > 1:
                G.add_edge((r, c, 'v'), (r - 2, c, 'h'), weight=blocks[r - 1, c] + blocks[r - 2, c])
            if r > 2:
                G.add_edge((r, c, 'v'), (r - 3, c, 'h'), weight=blocks[r - 1, c] + blocks[r - 2, c] + blocks[r - 3, c])
            if r < bsize[0] - 1:
                G.add_edge((r, c, 'v'), (r + 1, c, 'h'), weight=blocks[r + 1, c])
            if r < bsize[0] - 2:
                G.add_edge((r, c, 'v'), (r + 2, c, 'h'), weight=blocks[r + 1, c] + blocks[r + 2, c])
            if r < bsize[0] - 3:
                G.add_edge((r, c, 'v'), (r + 3, c, 'h'), weight=blocks[r + 1, c] + blocks[r + 2, c] + blocks[r + 3, c])

    return G


def build_graph_2(blocks : np.full):
    G = nx.DiGraph()
    bsize = blocks.shape
    for r in range(bsize[0]):
        for c in range(bsize[1]):
            G.add_node((r, c, 'h'))
            G.add_node((r, c, 'v'))

    for r in range(bsize[0]):
        for c in range(bsize[1]):
            if c > 3:
                G.add_edge((r, c, 'h'), (r, c - 4, 'v'), weight=blocks[r, c - 1] + blocks[r, c - 2] + blocks[r, c - 3] + blocks[r, c - 4])
            if c > 4:
                G.add_edge((r, c, 'h'), (r, c - 5, 'v'), weight=blocks[r, c - 1] + blocks[r, c - 2] + blocks[r, c - 3] + blocks[r, c - 4] + blocks[r, c - 5])
            if c > 5:
                G.add_edge((r, c, 'h'), (r, c - 6, 'v'), weight=blocks[r, c - 1] + blocks[r, c - 2] + blocks[r, c - 3] + blocks[r, c - 4] + blocks[r, c - 5] + blocks[r, c - 6])
            if c > 6:
                G.add_edge((r, c, 'h'), (r, c - 7, 'v'), weight=blocks[r, c - 1] + blocks[r, c - 2] + blocks[r, c - 3] + blocks[r, c - 4] + blocks[r, c - 5] + blocks[r, c - 6] + blocks[r, c - 7])
            if c > 7:
                G.add_edge((r, c, 'h'), (r, c - 8, 'v'), weight=blocks[r, c - 1] + blocks[r, c - 2] + blocks[r, c - 3] + blocks[r, c - 4] + blocks[r, c - 5] + blocks[r, c - 6] + blocks[r, c - 7] + blocks[r, c - 8])
            if c > 8:
                G.add_edge((r, c, 'h'), (r, c - 9, 'v'), weight=blocks[r, c - 1] + blocks[r, c - 2] + blocks[r, c - 3] + blocks[r, c - 4] + blocks[r, c - 5] + blocks[r, c - 6] + blocks[r, c - 7] + blocks[r, c - 8] + blocks[r, c - 9])
            if c > 9:
                G.add_edge((r, c, 'h'), (r, c - 10, 'v'), weight=blocks[r, c - 1] + blocks[r, c - 2] + blocks[r, c - 3] + blocks[r, c - 4] + blocks[r, c - 5] + blocks[r, c - 6] + blocks[r, c - 7] + blocks[r, c - 8] + blocks[r, c - 9] + blocks[r, c - 10])
            if c < bsize[1] - 4:
                G.add_edge((r, c, 'h'), (r, c + 4, 'v'), weight=blocks[r, c + 1] + blocks[r, c + 2] + blocks[r, c + 3] + blocks[r, c + 4])
            if c < bsize[1] - 5:
                G.add_edge((r, c, 'h'), (r, c + 5, 'v'), weight=blocks[r, c + 1] + blocks[r, c + 2] + blocks[r, c + 3] + blocks[r, c + 4] + blocks[r, c + 5])
            if c < bsize[1] - 6:
                G.add_edge((r, c, 'h'), (r, c + 6, 'v'), weight=blocks[r, c + 1] + blocks[r, c + 2] + blocks[r, c + 3] + blocks[r, c + 4] + blocks[r, c + 5] + blocks[r, c + 6])
            if c < bsize[1] - 7:
                G.add_edge((r, c, 'h'), (r, c + 7, 'v'), weight=blocks[r, c + 1] + blocks[r, c + 2] + blocks[r, c + 3] + blocks[r, c + 4] + blocks[r, c + 5] + blocks[r, c + 6] + blocks[r, c + 7])
            if c < bsize[1] - 8:
                G.add_edge((r, c, 'h'), (r, c + 8, 'v'), weight=blocks[r, c + 1] + blocks[r, c + 2] + blocks[r, c + 3] + blocks[r, c + 4] + blocks[r, c + 5] + blocks[r, c + 6] + blocks[r, c + 7] + blocks[r, c + 8])
            if c < bsize[1] - 9:
                G.add_edge((r, c, 'h'), (r, c + 9, 'v'), weight=blocks[r, c + 1] + blocks[r, c + 2] + blocks[r, c + 3] + blocks[r, c + 4] + blocks[r, c + 5] + blocks[r, c + 6] + blocks[r, c + 7] + blocks[r, c + 8] + blocks[r, c + 9])
            if c < bsize[1] - 10:
                G.add_edge((r, c, 'h'), (r, c + 10, 'v'), weight=blocks[r, c + 1] + blocks[r, c + 2] + blocks[r, c + 3] + blocks[r, c + 4] + blocks[r, c + 5] + blocks[r, c + 6] + blocks[r, c + 7] + blocks[r, c + 8] + blocks[r, c + 9] + blocks[r, c + 10])
            #
            if r > 3:
                G.add_edge((r, c, 'v'), (r - 4, c, 'h'), weight=blocks[r - 1, c] + blocks[r - 2, c] + blocks[r - 3, c] + blocks[r - 4, c])
            if r > 4:
                G.add_edge((r, c, 'v'), (r - 5, c, 'h'), weight=blocks[r - 1, c] + blocks[r - 2, c] + blocks[r - 3, c] + blocks[r - 4, c] + blocks[r - 5, c])
            if r > 5:
                G.add_edge((r, c, 'v'), (r - 6, c, 'h'), weight=blocks[r - 1, c] + blocks[r - 2, c] + blocks[r - 3, c] + blocks[r - 4, c] + blocks[r - 5, c] + blocks[r - 6, c])
            if r > 6:
                G.add_edge((r, c, 'v'), (r - 7, c, 'h'), weight=blocks[r - 1, c] + blocks[r - 2, c] + blocks[r - 3, c] + blocks[r - 4, c] + blocks[r - 5, c] + blocks[r - 6, c] + blocks[r - 7, c])
            if r > 7:
                G.add_edge((r, c, 'v'), (r - 8, c, 'h'), weight=blocks[r - 1, c] + blocks[r - 2, c] + blocks[r - 3, c] + blocks[r - 4, c] + blocks[r - 5, c] + blocks[r - 6, c] + blocks[r - 7, c] + blocks[r - 8, c])
            if r > 8:
                G.add_edge((r, c, 'v'), (r - 9, c, 'h'), weight=blocks[r - 1, c] + blocks[r - 2, c] + blocks[r - 3, c] + blocks[r - 4, c] + blocks[r - 5, c] + blocks[r - 6, c] + blocks[r - 7, c] + blocks[r - 8, c] + blocks[r - 9, c])
            if r > 9:
                G.add_edge((r, c, 'v'), (r - 10, c, 'h'), weight=blocks[r - 1, c] + blocks[r - 2, c] + blocks[r - 3, c] + blocks[r - 4, c] + blocks[r - 5, c] + blocks[r - 6, c] + blocks[r - 7, c] + blocks[r - 8, c] + blocks[r - 9, c] + blocks[r - 10, c])
            if r < bsize[0] - 4:
                G.add_edge((r, c, 'v'), (r + 4, c, 'h'), weight=blocks[r + 1, c] + blocks[r + 2, c] + blocks[r + 3, c] + blocks[r + 4, c])
            if r < bsize[0] - 5:
                G.add_edge((r, c, 'v'), (r + 5, c, 'h'), weight=blocks[r + 1, c] + blocks[r + 2, c] + blocks[r + 3, c] + blocks[r + 4, c] + blocks[r + 5, c])
            if r < bsize[0] - 6:
                G.add_edge((r, c, 'v'), (r + 6, c, 'h'), weight=blocks[r + 1, c] + blocks[r + 2, c] + blocks[r + 3, c] + blocks[r + 4, c] + blocks[r + 5, c] + blocks[r + 6, c])
            if r < bsize[0] - 7:
                G.add_edge((r, c, 'v'), (r + 7, c, 'h'), weight=blocks[r + 1, c] + blocks[r + 2, c] + blocks[r + 3, c] + blocks[r + 4, c] + blocks[r + 5, c] + blocks[r + 6, c] + blocks[r + 7, c])
            if r < bsize[0] - 8:
                G.add_edge((r, c, 'v'), (r + 8, c, 'h'), weight=blocks[r + 1, c] + blocks[r + 2, c] + blocks[r + 3, c] + blocks[r + 4, c] + blocks[r + 5, c] + blocks[r + 6, c] + blocks[r + 7, c] + blocks[r + 8, c])
            if r < bsize[0] - 9:
                G.add_edge((r, c, 'v'), (r + 9, c, 'h'), weight=blocks[r + 1, c] + blocks[r + 2, c] + blocks[r + 3, c] + blocks[r + 4, c] + blocks[r + 5, c] + blocks[r + 6, c] + blocks[r + 7, c] + blocks[r + 8, c] + blocks[r + 9, c])
            if r < bsize[0] - 10:
                G.add_edge((r, c, 'v'), (r + 10, c, 'h'), weight=blocks[r + 1, c] + blocks[r + 2, c] + blocks[r + 3, c] + blocks[r + 4, c] + blocks[r + 5, c] + blocks[r + 6, c] + blocks[r + 7, c] + blocks[r + 8, c] + blocks[r + 9, c] + blocks[r + 10, c])

    return G

    
def advent17_1():
    #file = open('input17_example.txt');  c_size = (13, 13)
    file = open('input17.txt'); c_size = (141, 141)

    blocks = np.full(c_size, 0, dtype=int)

    i = 0
    for line in file:
        line = line.strip('\n')
        for j in range(c_size[1]):
            blocks[i, j] = int(line[j])
        i += 1

    bsize = blocks.shape
    gb = build_graph(blocks)
    print('gb:', gb)

    p1 = nx.shortest_path(gb, (0, 0, 'v'), (bsize[0] - 1, bsize[1] - 1, 'v'), weight='weight')
    p2 = nx.shortest_path(gb, (0, 0, 'v'), (bsize[0] - 1, bsize[1] - 1, 'h'), weight='weight')
    p3 = nx.shortest_path(gb, (0, 0, 'h'), (bsize[0] - 1, bsize[1] - 1, 'v'), weight='weight')
    p4 = nx.shortest_path(gb, (0, 0, 'h'), (bsize[0] - 1, bsize[1] - 1, 'h'), weight='weight') 

    shortest = min([
        nx.path_weight(gb, p1, weight='weight'),
        nx.path_weight(gb, p2, weight='weight'),
        nx.path_weight(gb, p3, weight='weight'),
        nx.path_weight(gb, p4, weight='weight')
    ])
    print('Min. loss is (1):', shortest)


def advent17_2():
    #file = open('input17_example.txt');  c_size = (13, 13)
    file = open('input17.txt'); c_size = (141, 141)

    blocks = np.full(c_size, 0, dtype=int)

    i = 0
    for line in file:
        line = line.strip('\n')
        for j in range(c_size[1]):
            blocks[i, j] = int(line[j])
        i += 1

    bsize = blocks.shape
    gb = build_graph_2(blocks)
    print('gb:', gb)

    p1 = nx.shortest_path(gb, (0, 0, 'v'), (bsize[0] - 1, bsize[1] - 1, 'v'), weight='weight')
    p2 = nx.shortest_path(gb, (0, 0, 'v'), (bsize[0] - 1, bsize[1] - 1, 'h'), weight='weight')
    p3 = nx.shortest_path(gb, (0, 0, 'h'), (bsize[0] - 1, bsize[1] - 1, 'v'), weight='weight')
    p4 = nx.shortest_path(gb, (0, 0, 'h'), (bsize[0] - 1, bsize[1] - 1, 'h'), weight='weight') 

    shortest = min([
        nx.path_weight(gb, p1, weight='weight'),
        nx.path_weight(gb, p2, weight='weight'),
        nx.path_weight(gb, p3, weight='weight'),
        nx.path_weight(gb, p4, weight='weight')
    ])
    print('Min. loss is (2):', shortest)

    
if __name__ == '__main__':

    start_time = time.time()
    print('Advent 17')
    advent17_1()
    advent17_2()
    end_time_1 = time.time()
    print("time elapsed: {:.2f}s".format(end_time_1 - start_time))
