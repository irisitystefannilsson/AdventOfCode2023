from enum import Enum
import time
import numpy as np
import functools
import math

NUMBER_OF_CALLS = 0
LOG_FILE = open('logfile.txt', 'w')
DATA_CACHE = dict()
USED = []
ALLCONSTR = list()
MODULES = dict()


def add_possibilities(possibilities : set, garden : np.full):
    gs = garden.shape
    new_possibilities = set()
    for p in possibilities:
        #print(p)
        for new_p in [(p[0] + 1, p[1]), (p[0] - 1, p[1]), (p[0], p[1] + 1), (p[0], p[1] - 1)]:
            #print(new_p)
            if new_p[0] >= 0 and new_p[0] < gs[0] and new_p[1] >= 0 and new_p[1] < gs[1]:
                if garden[new_p[0], new_p[1]] != '#':
                    new_possibilities.add(new_p)

    return new_possibilities


def advent21_1():
    #file = open('input21_example.txt'); garden_size = (11, 11)
    file = open('input21.txt'); garden_size = (131, 131)

    garden = np.full(garden_size, '.', dtype=str)
    r = 0
    start = (0, 0)
    for line in file:
        line = line.strip('\n')
        for c in range(garden_size[1]):
            garden[r, c] = line[c]
            if line[c] == 'S':
                start = (r, c)
                garden[r, c] = '.'
        r += 1

    #print(garden)

    possible_plots = set()
    possible_plots.add(start)

    for step in range(64):
        possible_plots = add_possibilities(possible_plots, garden)

    for p in possible_plots:
        garden[p[0], p[1]] = 'O'
    #print(garden)

    print('Total (1):', len(possible_plots))


def add_more_possibilities(possibilities : set, garden : np.full):
    gs = garden.shape
    new_possibilities = set()
    for p in possibilities:
        #print(p)
        for new_p in [(p[0] + 1, p[1]), (p[0] - 1, p[1]), (p[0], p[1] + 1), (p[0], p[1] - 1)]:
            mod_p = (new_p[0] % gs[0], new_p[1] % gs[1])
            if garden[mod_p[0], mod_p[1]] != '#':
                new_possibilities.add(new_p)

    return new_possibilities


def advent21_2():
    #file = open('input21_example.txt'); garden_size = (11, 11); incr = 11
    file = open('input21.txt'); garden_size = (131, 131); incr = 131

    garden = np.full(garden_size, '.', dtype=str)
    r = 0
    start = (0, 0)
    for line in file:
        line = line.strip('\n')
        for c in range(garden_size[1]):
            garden[r, c] = line[c]
            if line[c] == 'S':
                start = (r, c)
                garden[r, c] = '.'
        r += 1

    #print(garden)

    possible_plots = set()
    possible_plots.add(start)

    nof_steps = 26501365
    sim_steps = 400
    ff_mult = (nof_steps - sim_steps) // incr
    sim_steps = nof_steps - ff_mult*incr
    nos = []
    print('Sim_steps:', sim_steps)
    for step in range(sim_steps):
        possible_plots = add_more_possibilities(possible_plots, garden)
        nos.append(len(possible_plots))

    diff55 = []
    for i in range(3):
        diff55.append(nos[sim_steps -1 - i * incr] - nos[sim_steps - 1 - (i+1)*incr])
            
    print(diff55[0] - diff55[1], diff55[1] - diff55[2])
        
    d_diff = diff55[0] - diff55[1]
    st, diff = nos[-1 - incr], nos[-1 - incr] - nos[-1 - 2*incr]

    
    summ = 0
    for i in range(1, ff_mult + 2):
        summ += i

    Total = st + (ff_mult + 1)*diff + summ*d_diff

    print('Total (2):', Total)

    
if __name__ == '__main__':

    start_time = time.time()
    print('Advent 21')
    advent21_1()
    advent21_2()
    end_time_1 = time.time()
    print("time elapsed: {:.2f}s".format(end_time_1 - start_time))
