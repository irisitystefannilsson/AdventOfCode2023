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


def to_equation(p : list, v : list):
    k = v[1] / v[0]
    m = (p[1] - k*p[0])

    return k, m


def calc_intersect(k0 : float, m0 : float, k1 : float, m1 : float):
    if k0 == k1:
        return float('inf'), float('inf')
    x = (m1 - m0)/(k0 - k1)
    y = k0*x + m0

    return x, y


def within_box(x : float, y : float, box : list):
    if (box[0][0] <= x <= box[0][1]) and (box[1][0] <= y <= box[1][1]):
        return True
    return False


def in_the_future(p : list, v : list, x : float, y : float):
    if x > p[0] and v[0] > 0 and y > p[1] and v[1] > 0:
        return True
    if x > p[0] and v[0] > 0 and y < p[1] and v[1] < 0:
        return True
    if x < p[0] and v[0] < 0 and y > p[1] and v[1] > 0:
        return True
    if x < p[0] and v[0] < 0 and y < p[1] and v[1] < 0:
        return True
    return False

    
def advent24_1():
    #file = open('input24_example.txt'); box = [[7, 27], [7, 27]]
    file = open('input24.txt'); box = [[200000000000000, 400000000000000], [200000000000000, 400000000000000]]

    poss = list()
    vels = list()
    eqs = list()
    for line in file:
        line = line.strip('\n')
        p, v = line.split(' @ ')
        p = [int(e) for e in p.split(', ')]
        v = [int(e) for e in v.split(', ')]
        poss.append(p)
        vels.append(v)
        eqs.append(to_equation(p, v))

    nof_crosses = 0
    for i in range(len(eqs)):
        for j in range(i + 1, len(eqs)):
            k0, m0 = eqs[i][0], eqs[i][1]
            k1, m1 = eqs[j][0], eqs[j][1] 
            x, y= calc_intersect(k0, m0, k1, m1)
            if within_box(x, y, box) and in_the_future(poss[i], vels[i], x, y) and in_the_future(poss[j], vels[j], x, y):
                nof_crosses += 1
    print('Crossing paths in box:', nof_crosses)


def advance_hail(p : tuple, v : tuple, dt : int):
    p = (p[0] + dt*v[0], p[1] + dt*v[1], p[2] + dt*v[2])
    return p


def calc_spread(poss : list):
    xmin = 2**32
    xmax = -2**32
    ymin = 2**32
    ymax = -2**32
    zmin = 2**32
    zmax = -2**32
    for p in poss:
        xmin, xmax = min(xmin, p[0]), max(xmax, p[0])
        ymin, ymax = min(ymin, p[1]), max(ymax, p[1])
        zmin, zmax = min(zmin, p[2]), max(zmax, p[2])
    return [xmin, xmax], [ymin, ymax], [zmin, zmax]

    
def advent24_2():
    file = open('input24_example.txt');
    #file = open('input24.txt');

    poss = list()
    vels = list()
    for line in file:
        line = line.strip('\n')
        p, v = line.split(' @ ')
        p = [int(e) for e in p.split(', ')]
        v = [int(e) for e in v.split(', ')]
        poss.append(p)
        vels.append(v)

    for t in (range(1, 6)):
        for i in range(len(poss)):
            poss[i] = advance_hail(poss[i], vels[i], 1)
        print(poss[0][0], poss[1][0], poss[2][0], poss[3][0], poss[4][0])
        xs, ys, zs = calc_spread(poss)
        #print(xs, ys, zs)

        
if __name__ == '__main__':
    start_time = time.time()
    print('Advent 24')
    advent24_1()
    advent24_2()
    end_time_1 = time.time()
    print("time elapsed: {:.2f}s".format(end_time_1 - start_time))
