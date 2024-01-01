import time
import numpy as np
import functools
import math
import copy
import resource, sys

np.set_printoptions(edgeitems=30, linewidth=100000, formatter=dict(float=lambda x: "%.3g" % x))
resource.setrlimit(resource.RLIMIT_STACK, (2**29,-1))
sys.setrecursionlimit(2500)

NUMBER_OF_CALLS = 0
LOG_FILE = open('logfile.txt', 'w')
DATA_CACHE = dict()
SORTED = []
NODES = []
GRAPH = dict()
EDGES = dict()


def top_sort(trails : np.full, visited : np.full, coord : tuple):
    bsize = trails.shape
    global SORTED
    p = coord
    visited[coord[0], coord[1]] = True
    for cp in [(p[0]+1, p[1]),(p[0]-1, p[1]),(p[0], p[1]+1),(p[0], p[1]-1)]:
        if cp[0] >= 0 and cp[0] < bsize[0] and cp[1] >= 0 and cp[1] < bsize[1] and not visited[cp[0], cp[1]]:
            if trails[cp[0], cp[1]] in  ['.', '^', '>', 'v', '<']:
                if cp == (p[0]+1, p[1]) and trails[cp[0], cp[1]] == '^':
                    pass
                elif cp == (p[0]-1, p[1]) and trails[cp[0], cp[1]] == 'v':
                    pass
                elif cp == (p[0], p[1]+1) and trails[cp[0], cp[1]] == '<':
                    pass
                elif cp == (p[0], p[1]-1) and trails[cp[0], cp[1]] == '>':
                    pass
                else:
                    top_sort(trails, visited, cp)

    SORTED.append(coord)


def dijkstra2(trails : np.full, start : tuple):
    global SORTED
    bsize = trails.shape
    visited = np.full(bsize, False, dtype=bool)
    top_sort(trails, visited, start)
    visited = trails == '#'
    dist = np.full(bsize, 0, dtype=int)

    p = start
    dist[p[0], p[1]] = 0
    while not (visited == True).all():
        visited[p[0], p[1]] = True
        for cp in [(p[0]+1, p[1]),(p[0]-1, p[1]),(p[0], p[1]+1),(p[0], p[1]-1)]:
            if cp[0] >= 0 and cp[0] < bsize[0] and cp[1] >= 0 and cp[1] < bsize[1] and not visited[cp[0], cp[1]]:
                if trails[cp[0], cp[1]] in  ['.', '^', '>', 'v', '<']:
                    if cp == (p[0]+1, p[1]) and trails[cp[0], cp[1]] == '^':
                        pass
                    elif cp == (p[0]-1, p[1]) and trails[cp[0], cp[1]] == 'v':
                        pass
                    elif cp == (p[0], p[1]+1) and trails[cp[0], cp[1]] == '<':
                        pass
                    elif cp == (p[0], p[1]-1) and trails[cp[0], cp[1]] == '>':
                        pass
                    else:
                        dist[cp[0], cp[1]] = min(dist[cp[0], cp[1]], dist[p[0], p[1]] - 1)

        try:
            p = SORTED.pop()
        except:
            break
        #print(dist)
        #print(p)
        #time.sleep(1)
    return dist


def find_forks(trails : np.full):
    global NODES
    global GRAPH
    p = (0, 1)
    visited = trails == '#'
    #print('Fork node:', p, 0)
    NODES.append(p)
    GRAPH[p] = []
    visited[p[0], p[1]] = True
    while not (visited == True).all():
        follow_trail(trails, visited, p, (p[0] + 1, p[1]))
        

def follow_trail(trails : np.full, visited : np.full, node : tuple, start : tuple):
    global NODES
    global GRAPH
    dist = 1
    p = start
    bsize = trails.shape
    while True:
        visited[p[0], p[1]] = True
        nofn = 0
        nes = list()
        if p in NODES and dist > 1: # we've been here before
            #print('Fork node:', node, ' - ', p, dist)
            GRAPH[p].append(node)
            GRAPH[node].append(p)
            EDGES[(p, node)] = dist
            EDGES[(node, p)] = dist
            return True
        for cp in [(p[0]+1, p[1]),(p[0]-1, p[1]),(p[0], p[1]+1),(p[0], p[1]-1)]:
            if cp[0] >= 0 and cp[0] < bsize[0] and cp[1] >= 0 and cp[1] < bsize[1] and (not visited[cp[0], cp[1]] or (cp in NODES and dist > 1)):
                if trails[cp[0], cp[1]] in  ['.', '^', '>', 'v', '<']:
                    nofn += 1
                    nes.append(cp)
        if nofn == 0:
            if p == (bsize[0] - 1, bsize[1] - 2):
                #print('Fork node:', node, ' - ', p, dist)
                GRAPH[p] = [node]
                GRAPH[node].append(p)
                EDGES[(p, node)] = dist
                EDGES[(node, p)] = dist
                return True
            return False
        if nofn > 1:
            #print('Fork node:', node, ' - ', p, dist)
            NODES.append(p)
            GRAPH[p] =[node]
            GRAPH[node].append(p)
            EDGES[(p, node)] = dist
            EDGES[(node, p)] = dist
            for s in nes:
                follow_trail(trails, visited, p, s)
            return True
        dist += 1
        p = nes[0]


def calc_length(path : list):
    global EDGES
    length = 0
    for i in range(len(path) - 1):
        length += EDGES[(path[i], path[i + 1])]

    return length
    
    
def find_path(src, dst):
    global GRAPH
    """Finds all possible path for a graph (global var) for `src` and `dst`
    
    Args:
        src (list): the source
        dst (list): the destination
    """

    def dfs(src, dst, path, seen):
        """Recursive generator that yields all paths from `src` to `dst`
        
        Args:
            src (int): source node
            dst (int): destination node
            path (list): path so far
            seen (set): set of visited nodes
        
        Yields:
            list: all paths from `src` to `dst`
        """
        if src in seen:
            return

        if src == dst:
            yield path + [src]
            return

        seen.add(src)

        for i in GRAPH[src]:
            yield from dfs(i, dst, path + [src], seen)
        seen.remove(src)


    # return paths for `src` `dst`
    return list(dfs(src, dst, [], set()))


def advent23_1():
    #file = open('input23_example.txt'); trail_size = (23, 23)
    file = open('input23.txt'); trail_size = (141, 141)
    trails = np.full(trail_size, '.', dtype=str)
    r = 0
    start = (0, 1)
    for line in file:
        line = line.strip('\n')
        for c in range(trail_size[1]):
            trails[r, c] = line[c]
        r += 1

    #print(trails)

    dist = dijkstra2(trails, start)
    print('Longest path:', abs(dist[trail_size[0] - 1, trail_size[1] - 2]))


def advent23_2():
    global GRAPH
    #file = open('input23_example.txt'); trail_size = (23, 23)
    file = open('input23.txt'); trail_size = (141, 141)
    trails = np.full(trail_size, '.', dtype=str)
    r = 0
    for line in file:
        line = line.strip('\n')
        for c in range(trail_size[1]):
            trails[r, c] = line[c]
        r += 1

    find_forks(trails)
    #print(GRAPH)
    paths = find_path((0, 1), (trail_size[0] - 1, trail_size[1] - 2))
    #depthFirst(GRAPH, (0, 1), [])

    max_len = 0
    for path in paths:
        if (trail_size[0] - 1, trail_size[1] - 2) in path:
            max_len = max(calc_length(path), max_len)

    print('Max length:', max_len)
    
    
if __name__ == '__main__':

    start_time = time.time()
    print('Advent 23')
    advent23_1()
    advent23_2()
    end_time_1 = time.time()
    print("time elapsed: {:.2f}s".format(end_time_1 - start_time))
