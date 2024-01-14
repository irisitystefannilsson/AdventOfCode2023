import time
import numpy as np


def expand_universe(universe : np.full, galaxies : list):
    empty_rows = list()
    for r in range(universe.shape[0]):
        if np.all(universe[r, :] == '.'):
            empty_rows.append(r)
    empty_cols = list()
    for c in range(universe.shape[1]):
        if np.all(universe[:, c] == '.'):
            empty_cols.append(c)

    new_galaxies = list()
    for g in galaxies:
        i = g[0]
        j = g[1]
        for r in empty_rows:
            if g[0] > r:
                i += 1
        for c in empty_cols:
            if g[1] > c:
                j += 1
        new_galaxies.append((i, j))

    return new_galaxies

    
def advent11_1():
    #file = open('input11_example.txt')
    file = open('input11.txt')

    ex_size = (10, 10)
    real_size = (140, 140)

    universe = np.full(real_size, '.', dtype=str)
    galaxies = list()
    for r in range(universe.shape[0]):
        row = file.readline().strip('\n')
        for c in range(len(row)):
            universe[r, c] = row[c]
            if row[c] == '#':
                galaxies.append((r, c))

    galaxies = expand_universe(universe, galaxies)
    #print(galaxies)
    distsum = 0
    for g1 in range(len(galaxies)):
        for g2 in range(g1 + 1, len(galaxies)):
            dist = abs(galaxies[g1][0] - galaxies[g2][0]) + abs(galaxies[g1][1] - galaxies[g2][1])
            #print(dist)
            distsum += dist

    print('Sum of minlengths (1):', distsum)


def expand_universe_alot(universe : np.full, galaxies : list):
    empty_rows = list()
    for r in range(universe.shape[0]):
        if np.all(universe[r, :] == '.'):
            empty_rows.append(r)
    empty_cols = list()
    for c in range(universe.shape[1]):
        if np.all(universe[:, c] == '.'):
            empty_cols.append(c)

    new_galaxies = list()
    for g in galaxies:
        i = g[0]
        j = g[1]
        for r in empty_rows:
            if g[0] > r:
                i += 1000000 - 1
        for c in empty_cols:
            if g[1] > c:
                j += 1000000 - 1
        new_galaxies.append((i, j))

    return new_galaxies


def advent11_2():
    #file = open('input11_example.txt')
    file = open('input11.txt')

    ex_size = (10, 10)
    real_size = (140, 140)

    universe = np.full(real_size, '.', dtype=str)
    galaxies = list()
    for r in range(universe.shape[0]):
        row = file.readline().strip('\n')
        for c in range(len(row)):
            universe[r, c] = row[c]
            if row[c] == '#':
                galaxies.append((r, c))

    galaxies = expand_universe_alot(universe, galaxies)
    #print(galaxies)
    distsum = 0
    for g1 in range(len(galaxies)):
        for g2 in range(g1 + 1, len(galaxies)):
            dist = abs(galaxies[g1][0] - galaxies[g2][0]) + abs(galaxies[g1][1] - galaxies[g2][1])
            #print(dist)
            distsum += dist

    print('Sum of minlengths (2):', distsum)

    
if __name__ == '__main__':

    start_time = time.time()
    print('Advent 11')
    advent11_1()
    advent11_2()
    end_time_1 = time.time()
    print("time elapsed: {:.2f}s".format(end_time_1 - start_time))
