import time
import numpy as np
import functools
import math
import copy

NUMBER_OF_CALLS = 0
LOG_FILE = open('logfile.txt', 'w')
DATA_CACHE = dict()
USED = []
STARTSET = set()


def min_coord(front : set, dist : np.full, visited : np.full):
    minv = 2**33
    coord = (0, 0)
    for p in front:
        if not visited[p[0], p[1]] and dist[p[0], p[1]] < minv:
            minv = dist[p[0], p[1]]
            coord = p

    return coord
            

def find_forbidden_path(p : tuple, dist : np.full, visited : np.full):
    pp = p
    bsize = dist.shape
    forbidden = (0, 0)
    back_path = list()
    if p[0] > 0 or p[1] > 0:
        for b in range(3):
            minv = dist[pp[0], pp[1]]
            for cp in [(pp[0]+1, pp[1]),(pp[0]-1, pp[1]),(pp[0], pp[1]+1),(pp[0], pp[1]-1)]:
                if cp[0] >= 0 and cp[0] < bsize[0] and cp[1] >= 0 and cp[1] < bsize[1]:
                    if visited[cp[0], cp[1]] and dist[cp[0], cp[1]] < minv:
                        minv = dist[cp[0], cp[1]]
                        pp = cp
            back_path.append(pp)
        # on straight line?
        if (abs(p[0] - back_path[0][0]) == 1  and abs(p[0] - back_path[1][0]) == 2 and abs(p[0] - back_path[2][0]) == 3):
            forbidden = (p[0] + (back_path[0][0] - back_path[1][0]), p[1])
            #print(p, back_path, forbidden)
        if (abs(p[1] - back_path[0][1]) == 1  and abs(p[1] - back_path[1][1]) == 2 and abs(p[1] - back_path[2][1]) == 3):
            forbidden = (p[0], p[1] + (back_path[0][1] - back_path[1][1]))
            #print(p, back_path, forbidden)
    return forbidden

    
def dijkstra(blocks : np.full, start=(0, 0)):
    bsize = blocks.shape
    visited = np.full(bsize, False, dtype=bool)
    dist = np.full(bsize, 2**10, dtype=int)

    p = start
    dist[p[0], p[1]] = 0
    viset = set()
    while not (visited == True).all():
        visited[p[0], p[1]] = True
        f_path = find_forbidden_path(p, dist, visited)
        for cp in [(p[0]+1, p[1]),(p[0]-1, p[1]),(p[0], p[1]+1),(p[0], p[1]-1)]:
            if cp[0] >= 0 and cp[0] < bsize[0] and cp[1] >= 0 and cp[1] < bsize[1]:
                if cp != f_path:
                    dist[cp[0], cp[1]] = min(dist[cp[0], cp[1]], dist[p[0], p[1]] + blocks[cp[0], cp[1]])
                viset.add(cp)
        #print(viset)
        p = min_coord(viset, dist, visited)
        try:
            viset.remove(p)
        except:
            pass
        #print(visited)

    return dist

        
def advent17_1():
    file = open('input17_example.txt');  c_size = (13, 13)
    #file = open('input17.txt'); c_size = (141, 141)

    blocks = np.full(c_size, 0, dtype=int)

    i = 0
    for line in file:
        line = line.strip('\n')
        for j in range(c_size[1]):
            blocks[i, j] = int(line[j])
        i += 1

    print(blocks)
    dist = dijkstra(blocks, (3,3))
    #print(dist)
    dist = dijkstra(blocks, (6, 6))
    print(dist)

if __name__ == '__main__':

    start_time = time.time()
    print('Advent 17')
    advent17_1()
    #advent17_2()
    end_time_1 = time.time()
    print("time elapsed: {:.2f}s".format(end_time_1 - start_time))
