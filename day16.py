import time
import numpy as np


STARTSET = set()


class Point:
    def __init__(self, coord : tuple, dir : str):
        self.coord = coord
        self.dir = dir


def inside_contraption(start : Point, arr : np.full):
    i, j = start.coord
    if i >= 0 and i < arr.shape[0] and j >= 0 and j < arr.shape[1]:
        return True
    return False
    

def advance(start : Point, arr : np.full):
    terr = arr[start.coord[0], start.coord[1]]
    if start.dir == '>':
        if terr in ['.', '-']:
            start.coord = (start.coord[0], start.coord[1] + 1)
        elif terr == '/':
            start.coord = (start.coord[0] - 1, start.coord[1])
            start.dir = '^'
        elif terr == '\\':
            start.coord = (start.coord[0] + 1, start.coord[1])
            start.dir = 'v'
        elif terr == '|':
            start.coord = (start.coord[0] - 1, start.coord[1])
            start.dir = '^'
            STARTSET.add(Point((start.coord[0] + 1, start.coord[1]), 'v'))
    elif start.dir == '<':
        if terr in ['.', '-']:
            start.coord = (start.coord[0], start.coord[1] - 1)
        elif terr == '/':
            start.coord = (start.coord[0] + 1, start.coord[1])
            start.dir = 'v'
        elif terr == '\\':
            start.coord = (start.coord[0] - 1, start.coord[1])
            start.dir = '^'
        elif terr == '|':
            start.coord = (start.coord[0] + 1, start.coord[1])
            start.dir = 'v'
            STARTSET.add(Point((start.coord[0] - 1, start.coord[1]), '^'))
    elif start.dir == '^':
        if terr in ['.', '|']:
            start.coord = (start.coord[0] - 1, start.coord[1])
        elif terr == '/':
            start.coord = (start.coord[0], start.coord[1] + 1)
            start.dir = '>'
        elif terr == '\\':
            start.coord = (start.coord[0], start.coord[1] - 1)
            start.dir = '<'
        elif terr == '-':
            start.coord = (start.coord[0], start.coord[1] - 1)
            start.dir = '<'
            STARTSET.add(Point((start.coord[0], start.coord[1] + 1), '>'))
    elif start.dir == 'v':
        if terr in ['.', '|']:
            start.coord = (start.coord[0] + 1, start.coord[1])
        elif terr == '/':
            start.coord = (start.coord[0], start.coord[1] - 1)
            start.dir = '<'
        elif terr == '\\':
            start.coord = (start.coord[0], start.coord[1] + 1)
            start.dir = '>'
        elif terr == '-':
            start.coord = (start.coord[0], start.coord[1] + 1)
            start.dir = '>'
            STARTSET.add(Point((start.coord[0], start.coord[1] - 1), '<'))
    
    return start


def advent16_1():
    #file = open('input16_example.txt');  c_size = (10, 10)
    file = open('input16.txt'); c_size = (110, 110)

    contraption = np.full(c_size, '.', dtype=str)
    visited = np.full(c_size, '.', dtype=object)
    energized = contraption.copy()
    i = 0
    for line in file:
        line = line.strip('\n')
        for j in range(c_size[1]):
            contraption[i, j] = line[j]
        i += 1

    #print(contraption)

    STARTSET.add(Point((0, 0), '>'))

    while True:
        try:
            start = STARTSET.pop()
            #print('Popping Start')
            #print(start.coord, start.dir, visited[start.coord[0], start.coord[1]])
            inside = True
            while inside:
                visited[start.coord[0], start.coord[1]] += start.dir
                energized[start.coord[0], start.coord[1]] = '#'
                start = advance(start, contraption)
                inside = inside_contraption(start, contraption)
                if inside and start.dir in visited[start.coord[0], start.coord[1]]:
                    break
                
        except KeyError:
            print('All done!')
            break
        
    print('Curr. energized (1):', (energized == '#').sum())


def advent16_2():
    #file = open('input16_example.txt');  c_size = (10, 10)
    file = open('input16.txt'); c_size = (110, 110)

    contraptionOrig = np.full(c_size, '.', dtype=str)
    i = 0
    for line in file:
        line = line.strip('\n')
        for j in range(c_size[1]):
            contraptionOrig[i, j] = line[j]
        i += 1

    allstartpoints = set();

    #left/right sides
    for i in range(c_size[0]):
        allstartpoints.add(Point((i, 0), '>'))
        allstartpoints.add(Point((i, c_size[1]-1), '<'))
    #top/bottom sides
    for j in range(c_size[1]):
        allstartpoints.add(Point((0, j), 'v'))
        allstartpoints.add(Point((c_size[0]-1, j), '^'))
    #print(contraption)

    energy = 0
    for p in allstartpoints:
        contraption = contraptionOrig.copy()
        visited = np.full(c_size, '.', dtype=object)
        energized = contraption.copy()
        
        #print('S:', p.coord, p.dir)
        STARTSET.add(p)

        while True:
            try:
                start = STARTSET.pop()
                #print('Popping Start')
                #print(start.coord, start.dir, visited[start.coord[0], start.coord[1]])
                inside = True
                while inside:
                    visited[start.coord[0], start.coord[1]] += start.dir
                    energized[start.coord[0], start.coord[1]] = '#'
                    start = advance(start, contraption)
                    inside = inside_contraption(start, contraption)
                    if inside and start.dir in visited[start.coord[0], start.coord[1]]:
                        break

            except KeyError:
                #print('All done!')
                break

        energy = max((energized == '#').sum(), energy)
        #print(energy)
    print('Emax (2):', energy)


if __name__ == '__main__':

    start_time = time.time()
    print('Advent 16')
    advent16_1()
    advent16_2()
    end_time_1 = time.time()
    print("time elapsed: {:.2f}s".format(end_time_1 - start_time))
