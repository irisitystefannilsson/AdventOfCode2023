import time
import numpy as np
import functools
import math
import copy

NUMBER_OF_CALLS = 0
LOG_FILE = open('logfile.txt', 'w')
DATA_CACHE = dict()
USED = []


HUGE_DIST = 1000000

class TubeNode:
    def __init__(self, tube : str, coord : tuple):
        self.tube = tube
        self.dist = HUGE_DIST
        self.visited = False
        if tube == '.':
            self.visited = True
        self.neighbours = list()
        self.coord = coord
        i = coord[0]
        j = coord[1]
        if tube == '|':
            self.neighbours.append((i - 1, j))
            self.neighbours.append((i + 1, j))
        elif tube == '-':
            self.neighbours.append((i, j - 1))
            self.neighbours.append((i, j + 1))
        elif tube == 'L':
            self.neighbours.append((i - 1, j))
            self.neighbours.append((i, j + 1))
        elif tube == 'J':
            self.neighbours.append((i - 1, j))
            self.neighbours.append((i, j - 1))
        elif tube == '7':
            self.neighbours.append((i + 1, j))
            self.neighbours.append((i, j - 1))
        elif tube == 'F':
            self.neighbours.append((i + 1, j))
            self.neighbours.append((i, j + 1))

    def init_start(self, near_tubes : list):
        self.dist = 0
        self.visited = True
        i = self.coord[0]
        j = self.coord[1]
        if near_tubes[0] in ['|', '7', 'F']:
            self.neighbours.append((i - 1, j))
        if near_tubes[1] in ['-', '7', 'J']:
            self.neighbours.append((i, j + 1))
        if near_tubes[2] in ['|', 'L', 'J']:
            self.neighbours.append((i + 1, j))
        if near_tubes[3] in ['-', 'L', 'F']:
            self.neighbours.append((i, j - 1))
            

def all_visited(arr : np.full):
    a_vis = True
    for i in range(arr.shape[0]):
        for j in range(arr.shape[1]):
            if not arr[i, j].visited:
                a_vis = False
                #print(i, j)
    return a_vis


def find_next(arr : np.full):
    mind = HUGE_DIST
    next = (-1, -1)
    for i in range(arr.shape[0]):
        for j in range(arr.shape[1]):
            if not arr[i, j].visited and arr[i, j].dist < mind:
                mind = arr[i, j].dist
                next = (i, j)
    return next


def dijkstra(dists : np.full, start):
    finished = False
    while True:
        #print(start, dists[start].neighbours)
        #print(dists[start[0], start[1]])
        dists[start[0], start[1]].visited = True
        for n in dists[start].neighbours:
            if not dists[n[0], n[1]].visited:
                dists[n[0], n[1]].dist = min(dists[n[0], n[1]].dist, dists[start[0], start[1]].dist + 1)

        start = find_next(dists)
        finished = all_visited(dists)
        if finished:
            break
        if start == (-1, -1):
            print(dists[start].neighbours)
            break
        

def find_largest_dist(arr : np.full):
    largest = 0
    for i in range(arr.shape[0]):
        for j in range(arr.shape[1]):
            if arr[i, j].visited and arr[i, j].tube != '.' and arr[i, j].dist > largest:
                largest = arr[i, j].dist
                print(i, j)
    return largest


def advent10_1():
    #file = open('input10_example.txt')
    file = open('input10.txt')
    ex_size = (5, 5)
    real_size = (140, 140)
    tubing = np.full(real_size, '.', dtype=str)

    i = 0
    start = (0, 0)
    for line in file:
        row = line.strip('\n')
        for j in range(len(row)):
            tubing[i, j] = row[j]
            if row[j] == 'S':
                start = (i, j)
        i += 1

    #print(tubing)
    dists = np.full(tubing.shape, TubeNode('.', (-1, -1)), dtype=TubeNode)
    dists[start] = TubeNode('S', start)
    S_close = ['.', '.', '.', '.']
    if start[0] > 0:
        S_close[0] = tubing[(start[0] - 1, start[1])]
    if start[1] < tubing.shape[1] - 1:
        S_close[1] = tubing[(start[0], start[1] + 1)]
    if start[0] < tubing.shape[0] - 1:
        S_close[2] = tubing[(start[0] + 1, start[1])]
    if start[1] > 0:
        S_close[3] = tubing[(start[0], start[1] - 1)]
    
    dists[start].init_start(S_close)
    for i in range(tubing.shape[0]):
        for j in range(tubing.shape[1]):
            if (i, j) != start:
                dists[i, j] = TubeNode(tubing[i, j], (i, j))
                
    dijkstra(dists, start)
    print('Distance:', find_largest_dist(dists))


def fill_unused_tubes(tubing : np.full, dists : np.full):
    for i in range(tubing.shape[0]):
        for j in range(tubing.shape[1]):
            if dists[i, j].dist== HUGE_DIST:
                tubing[i, j] = '.'
    

def remove_start(tubing : np.full, dists : np.full):
    for i in range(tubing.shape[0]):
        for j in range(tubing.shape[1]):
            if tubing[i, j] == 'S':
                n1, n2 = dists[i, j].neighbours
                if n1[0] == n2[0]:
                    tubing[i, j] = '-'
                    print('S => ', tubing[i, j]) 
                    return
                elif n1[1] == n2[1]:
                    tubing[i, j] = '|'
                    print('S => ', tubing[i, j]) 
                    return
                elif (n1 == (i, j-1) or n2 == (i, j-1)) and (n1[0] == i + 1 or n2[0] == i + 1):
                    tubing[i, j] = '7'
                    print('S => ', tubing[i, j]) 
                    return
                elif (n1 == (i, j+1) or n2 == (i, j+1)) and (n1[0] == i + 1 or n2[0] == i + 1):
                    tubing[i, j] = 'F'
                    print('S => ', tubing[i, j]) 
                    return
                elif (n1 == (i-1, j) or n2 == (i-1, j)) and (n1[1] == j + 1 or n2[1] == j + 1):
                    tubing[i, j] = 'L'
                    print('S => ', tubing[i, j]) 
                    return
                elif (n1 == (i-1, j) or n2 == (i-1, j)) and (n1[1] == j - 1 or n2[1] == j - 1):
                    tubing[i, j] = 'J'
                    print('S => ', tubing[i, j]) 
                    return


def check_if_inside(coord : tuple, tubing : np.full):
    i = coord[0]
    j = coord[1]
    crossings = 0
    for c in range(j + 1, tubing.shape[1]):
        if tubing[i, c] in ['|', 'F', '7']:
            crossings += 1
            #print(tubing[i, c])

    #print(crossings)
    return crossings % 2 != 0


def advent10_2():
    #file = open('input10_example2.txt')
    file = open('input10.txt')
    ex_size = (10, 20)
    real_size = (140, 140)
    tubing = np.full(real_size, '.', dtype=str)

    i = 0
    start = (0, 0)
    for line in file:
        row = line.strip('\n')
        for j in range(len(row)):
            tubing[i, j] = row[j]
            if row[j] == 'S':
                start = (i, j)
        i += 1

    #print(tubing)
    dists = np.full(tubing.shape, TubeNode('.', (-1, -1)), dtype=TubeNode)
    dists[start] = TubeNode('S', start)
    S_close = ['.', '.', '.', '.']
    if start[0] > 0:
        S_close[0] = tubing[(start[0] - 1, start[1])]
    if start[1] < tubing.shape[1] - 1:
        S_close[1] = tubing[(start[0], start[1] + 1)]
    if start[0] < tubing.shape[0] - 1:
        S_close[2] = tubing[(start[0] + 1, start[1])]
    if start[1] > 0:
        S_close[3] = tubing[(start[0], start[1] - 1)]
    
    dists[start].init_start(S_close)
    for i in range(tubing.shape[0]):
        for j in range(tubing.shape[1]):
            if (i, j) != start:
                dists[i, j] = TubeNode(tubing[i, j], (i, j))
                
    dijkstra(dists, start)
    fill_unused_tubes(tubing, dists)
    remove_start(tubing, dists)
    #print(tubing)
    nof_inside = 0
    for i in range(tubing.shape[0]):
        for j in range(tubing.shape[1]):
            if tubing[i, j] == '.' and check_if_inside((i, j), tubing):
                nof_inside += 1
                tubing[i, j] = 'O'

    #print(tubing)
    print('No. inside: ', nof_inside)

    
if __name__ == '__main__':

    start_time = time.time()
    print('Advent 10')
    #advent10_1()
    advent10_2()
    end_time_1 = time.time()
    print("time elapsed: {:.2f}s".format(end_time_1 - start_time))
