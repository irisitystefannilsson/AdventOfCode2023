import time
import numpy as np


DATA_CACHE = dict()


def find_symmetry(pattern : list, noc = -1):
    rows = len(pattern)
    cols = len(pattern[0])
    pat = np.full((rows, cols), '.', dtype=str)
    for i in range(rows):
        for j in range(cols):
            pat[i, j] = pattern[i][j]

    #print(pat)
    # check cols
    for j in range(cols - 1):
        sym = True
        for jj in range(1, j + 2):
            if j + jj >= cols:
                continue
            if (pat[:, j + 1 - jj] != pat[:, j + jj]).any():
                sym = False
                break
        if sym:
            if (noc >= 0 and DATA_CACHE[noc] != j + 1) or noc == -1:
                return j + 1


    # check rows
    for i in range(rows - 1):
        sym = True
        for ii in range(1, i + 2):
            if i + ii >= rows:
                continue
            if (pat[i + 1 - ii, :] != pat[i + ii]).any():
                sym = False
                break
        if sym:
            if (noc >= 0 and DATA_CACHE[noc] != (i + 1)*100) or noc == -1:
                return (i + 1)*100

    return 0

    
def advent13_1():
    #file = open('input13_example.txt')
    file = open('input13.txt')

    sym_sum = 0
    lines = list()
    noc = 0
    for line in file:
        line = line.strip('\n')
        if line == '':
            sym = find_symmetry(lines)
            DATA_CACHE[noc] = sym
            #print(DATA_CACHE)
            noc += 1
            sym_sum += sym
            lines = list()
        else:
            lines.append(line)
    # last pattern        
    sym = find_symmetry(lines)
    DATA_CACHE[noc] = sym
    #print(DATA_CACHE)
    noc += 1
    sym_sum += sym
        
    print('Sum of symms (1):' , sym_sum)


def find_new_symmetry(pattern : list, noc : int):
    rows = len(pattern)
    cols = len(pattern[0])
    for i in range(rows):
        for j in range(cols):
            if pattern[i][j] == '.':
                pattern[i][j] = '#'
                sym = find_symmetry(pattern, noc)
                if sym > 0:
                    return sym
                else:
                    pattern[i][j] = '.'
            elif pattern[i][j] == '#':
                pattern[i][j] = '.'
                sym = find_symmetry(pattern, noc)
                if sym > 0:
                    return sym
                else:
                    pattern[i][j] = '#'
            else:
                #print(pattern[i][j])
                raise

                    
def advent13_2():
    #file = open('input13_example.txt')
    file = open('input13.txt')

    sym_sum = 0
    lines = list()
    noc = 0
    for line in file:
        line = line.strip('\n')
        if line == '':
            #print(DATA_CACHE)
            #print(noc)
            sym = find_new_symmetry(lines, noc)
            noc += 1
            #print(sym)
            sym_sum += sym
            lines = list()
        else:
            lines.append(list(line))
    # last pattern        
    sym = find_new_symmetry(lines, noc)
    #print(sym)
    sym_sum += sym
        
    print('Sum of symms (2):' , sym_sum)
    

if __name__ == '__main__':

    start_time = time.time()
    print('Advent 13')
    advent13_1()
    advent13_2()
    end_time_1 = time.time()
    print("time elapsed: {:.2f}s".format(end_time_1 - start_time))
