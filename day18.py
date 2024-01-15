import time


class Bem:
    def __init__(self, coord : tuple, color : str, symbol : str, dir : str):
        self.coord = coord
        self.color = color
        self.symbol = symbol
        self.dir = dir


def count_insides(bems : list):
    coord = bems[0].coord[1]

    c = 0
    i = 0
    for b in bems:
        if b.coord[1] - coord > 1:
            if check_if_inside(bems[:i]):
                c += b.coord[1] - coord - 1
        coord = b.coord[1]
        i += 1
    return c


def check_if_inside(bems : list):
    nc = 0
    for b in bems:
        if b.symbol in ['|', 'F', '7']:
            nc += 1
    return nc % 2 != 0


def advent18_1():
    #file = open('input18_example.txt')
    file = open('input18.txt')

    boundary = list()
    start = (0, 0)

    coord = start
    for line in file:
        line = line.strip('\n')
        dir, length, color = line.split(' ')
        length = int(length)
        color = color.rstrip(')').lstrip('(')
        #print(dir, length, color)
        for b in range(length):
            if dir == 'U':
                coord = (coord[0] - 1, coord[1])
                sym = '|'
            elif dir == 'R':
                coord = (coord[0], coord[1] + 1)
                sym = '-'
            elif dir == 'D':
                coord = (coord[0] + 1, coord[1])
                sym = '|'
            elif dir == 'L':
                coord = (coord[0], coord[1] - 1)
                sym = '-'
            boundary.append(Bem(coord, color, sym, dir))

    for b in range(len(boundary)):
        if boundary[b].symbol != boundary[b-1].symbol: #corner
            if boundary[b].dir == 'U' and  boundary[b-1].dir == 'L':
                boundary[b-1].symbol = 'L'
            elif boundary[b].dir == 'U' and  boundary[b-1].dir == 'R':
                boundary[b-1].symbol = 'J'
            elif boundary[b].dir == 'D' and  boundary[b-1].dir == 'L':
                boundary[b-1].symbol = 'F'
            elif boundary[b].dir == 'D' and  boundary[b-1].dir == 'R':
                boundary[b-1].symbol = '7'
            elif boundary[b].dir == 'R' and  boundary[b-1].dir == 'U':
                boundary[b-1].symbol = 'F'
            elif boundary[b].dir == 'R' and  boundary[b-1].dir == 'D':
                boundary[b-1].symbol = 'L'
            elif boundary[b].dir == 'L' and  boundary[b-1].dir == 'U':
                boundary[b-1].symbol = '7'
            elif boundary[b].dir == 'L' and  boundary[b-1].dir == 'D':
                boundary[b-1].symbol = 'J'


    minH = min(boundary, key=lambda b: b.coord[0])
    maxH = max(boundary, key=lambda b: b.coord[0])

    h_sorted_b = list()
    idx = 0
    for i in range(minH.coord[0], maxH.coord[0] + 1):
        #print(i, idx)
        h_sorted_b.append([])
        for b in boundary:
            if b.coord[0] == i:
                h_sorted_b[idx].append(b)
        idx += 1

    incount = 0
    for l in h_sorted_b:
        l = sorted(l, key=lambda b: b.coord[1])
        #for b in l:
        #    print(b.coord)
        #print('--')
        incount += count_insides(l)

    print('Lava vol. (1):', int(incount + len(boundary)))

    
def advent18_2():
    #file = open('input18_example.txt')
    file = open('input18.txt')

    corners = list()
    start = (0, 0)
    coord = start
    trenchlen = 0
    for line in file:
        line = line.strip('\n')
        dir, length, color = line.split(' ')
        #length = int(length)
        color = color.rstrip(')').lstrip('(')
        length = int(color[1:6], 16)
        trenchlen += length
        if color[6] == '0':
            dir = 'R'
        elif color[6] == '1':
            dir = 'D'
        elif color[6] == '2':
            dir = 'L'
        elif color[6] == '3':
            dir = 'U'
        if dir == 'U':
            coord = (coord[0] - length, coord[1])
            sym = '|'
        elif dir == 'R':
            coord = (coord[0], coord[1] + length)
            sym = '-'
        elif dir == 'D':
            coord = (coord[0] + length, coord[1])
            sym = '|'
        elif dir == 'L':
            coord = (coord[0], coord[1] - length)
            sym = '-'
        corners.append(Bem(coord, color, sym, dir))

    for b in range(len(corners)):
        if corners[b].symbol != corners[b-1].symbol: #corner
            if corners[b].dir == 'U' and  corners[b-1].dir == 'L':
                corners[b-1].symbol = 'L'
                #corners[b-1].coord = (corners[b-1].coord[0]-1, corners[b-1].coord[1]+1)
            elif corners[b].dir == 'U' and  corners[b-1].dir == 'R':
                corners[b-1].symbol = 'J'
                #corners[b-1].coord = (corners[b-1].coord[0]-1, corners[b-1].coord[1])
            elif corners[b].dir == 'D' and  corners[b-1].dir == 'L':
                corners[b-1].symbol = 'F'
                #corners[b-1].coord = (corners[b-1].coord[0], corners[b-1].coord[1]+1)
            elif corners[b].dir == 'D' and  corners[b-1].dir == 'R':
                corners[b-1].symbol = '7'
                #corners[b-1].coord = (corners[b-1].coord[0], corners[b-1].coord[1]) 
            elif corners[b].dir == 'R' and  corners[b-1].dir == 'U':
                corners[b-1].symbol = 'F'
                #corners[b-1].coord = (corners[b-1].coord[0], corners[b-1].coord[1]+1)
            elif corners[b].dir == 'R' and  corners[b-1].dir == 'D':
                corners[b-1].symbol = 'L'
                #corners[b-1].coord = (corners[b-1].coord[0]-1, corners[b-1].coord[1]+1)
            elif corners[b].dir == 'L' and  corners[b-1].dir == 'U':
                corners[b-1].symbol = '7'
                #corners[b-1].coord = (corners[b-1].coord[0], corners[b-1].coord[1])
            elif corners[b].dir == 'L' and  corners[b-1].dir == 'D':
                corners[b-1].symbol = 'J'
                #corners[b-1].coord = (corners[b-1].coord[0]-1, corners[b-1].coord[1])

    #for b in corners:
    #    print(b.symbol, b.coord)
    
    #print('Trench len.:', trenchlen)
    iarea = shoelace(corners)
    #print('Inner area:', iarea)
    print('Lava vol. (2):', int(0.5*trenchlen + iarea + 1)) # +1 due to 4 corners with only 1/4 inside border 


def shoelace(corners : list):
    sum = 0
    for i in range(len(corners)):
        c = i % len(corners)
        cp1 = (i + 1) % len(corners)
        sum += corners[c].coord[0]*corners[cp1].coord[1] - corners[c].coord[1]*corners[cp1].coord[0]

    return 0.5*abs(sum)

    
if __name__ == '__main__':

    start_time = time.time()
    print('Advent 18')
    advent18_1()
    advent18_2()
    end_time_1 = time.time()
    print("time elapsed: {:.2f}s".format(end_time_1 - start_time))
