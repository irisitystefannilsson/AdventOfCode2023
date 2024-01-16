import time
import copy
from enum import Enum


class Dir(Enum):
    XDIR=0
    YDIR=1

    
class Brick:
    def __init__(self, start : tuple, end : tuple, name : str):
        self.start = start
        self.end = end
        self.name = name
        self.zlen = end[2] - start[2]
        self.dir = Dir.XDIR
        if end[1] > start[1]:
            self.dir = Dir.YDIR
        self.supports = list()
        self.supported_by = list()
        
    def interesect(self, other):
        #print(self.name, other.name)
        if self.dir != other.dir:
            #print('Diff dirs')
            if self.dir == Dir.XDIR:
                if self.start[1] >= other.start[1] and self.start[1] <= other.end[1]:
                    if self.start[0] <= other.start[0] and self.end[0] >= other.start[0]:
                        return True
            else:
                if self.start[0] >= other.start[0] and self.start[0] <= other.end[0]:
                    if self.start[1] <= other.start[1] and self.end[1] >= other.start[1]:
                        return True
        else:
            #print('Same dirs')
            if self.dir == Dir.XDIR:
                if self.start[1] == other.start[1]:
                    if other.start[0] <= self.start[0] <= other.end[0]:
                        return True
                    if self.start[0] <= other.start[0] <= self.end[0]:
                        return True
            else:
                if self.start[0] == other.start[0]:
                    if other.start[1] <= self.start[1] <= other.end[1]:
                        return True
                    if self.start[1] <= other.start[1] <= self.end[1]:
                        return True
        #print('No intersect!')
        return False
                    

def find_rest(bricks : list, pos : int):
    h = 1
    best_p = pos
    for p in range(pos - 1, -1, -1):
        if bricks[pos].interesect(bricks[p]):
            if bricks[p].end[2] >= h:
                bricks[pos].start = (bricks[pos].start[0], bricks[pos].start[1], bricks[p].end[2] + 1)
                bricks[pos].end = (bricks[pos].end[0], bricks[pos].end[1], bricks[pos].start[2] + bricks[pos].zlen)
                best_p = p
                h = bricks[pos].start[2]

    if best_p != pos:
        bricks[pos].supported_by.append(best_p)
        bricks[best_p].supports.append(pos)
    else:
        bricks[pos].start = (bricks[pos].start[0], bricks[pos].start[1], 1)
        bricks[pos].end = (bricks[pos].end[0], bricks[pos].end[1], bricks[pos].start[2] + bricks[pos].zlen)


def find_more_support(bricks : list, pos : int):
    #for p in range(len(bricks)):
    for p in range(pos - 1, -1, -1):
        if bricks[pos].interesect(bricks[p]) and bricks[pos].start[2] == (bricks[p].end[2] + 1):
            if p not in bricks[pos].supported_by:
                bricks[pos].supported_by.append(p)
            if pos not in bricks[p].supports:
                bricks[p].supports.append(pos)


def advent22_1():
    #file = open('input22_example.txt')
    file = open('input22.txt')

    bricks = list()
    num = 65
    for line in file:
        line = line.strip('\n')
        start, end = line.split('~')
        start = start.split(',')
        end = end.split(',')
        start = [int(e) for e in start]
        end = [int(e) for e in end]
        bricks.append(Brick(tuple(start), tuple(end), chr(num)))
        num += 1
        
    bricks = sorted(bricks, key=lambda e: e.start[2])
    #for b in bricks:
    #    print(b.name, b.start[2], b.end[2])

    for i in range(len(bricks)):
        find_rest(bricks, i)
    
    for i in range(len(bricks)):
        find_more_support(bricks, i)
        #print(bricks[i].name, bricks[i].start[2], bricks[i].end[2])

    nof_dis = 0
    for b in bricks:
        add = 1
        for s in b.supports:
            if len(bricks[s].supported_by) == 1:
                #print(b.name + ' only support for ' + bricks[s].name)
                add = 0
        nof_dis += add

    print(str(nof_dis) + ' can be disintegrated (1)')

    
def advent22_2():
    #file = open('input22_example.txt')
    file = open('input22.txt')

    bricks = list()
    num = 65
    for line in file:
        line = line.strip('\n')
        start, end = line.split('~')
        start = start.split(',')
        end = end.split(',')
        start = [int(e) for e in start]
        end = [int(e) for e in end]
        bricks.append(Brick(tuple(start), tuple(end), chr(num)))
        num += 1
        
    bricks = sorted(bricks, key=lambda e: e.start[2])
    #for b in bricks:
    #    print(b.name, b.start[2], b.end[2])

    for i in range(len(bricks)):
        find_rest(bricks, i)
    
    for i in range(len(bricks)):
        find_more_support(bricks, i)
        #print(bricks[i].name, bricks[i].start[2], bricks[i].end[2])

    tot_dis = 0
    for i in range(len(bricks)):
        cbricks = copy.deepcopy(bricks)
        nof_dis = 1
        #cbricks.pop(i)
        potdis = dis_brick(cbricks, i)
        while True:
            try:
                j = potdis.pop(0)
                #cbricks.pop(j)
                nof_dis += 1
                potdis += dis_brick(cbricks, j)
            except IndexError:
                break
        if nof_dis > 1:
            tot_dis += (nof_dis - 1)

        #print('Brick:', bricks[i].name, ' nof dis.:', nof_dis)

    print('Tot dis. (2):', tot_dis)
    

def dis_brick(bricks : list, i : int):
    b = bricks[i]
    potdis = list()
    for br in b.supports:
        #print(br, bricks[br].supported_by, bricks[i].supports)
        bricks[br].supported_by.remove(i)
        if len(bricks[br].supported_by) == 0:
            potdis.append(br)

    return potdis


if __name__ == '__main__':

    start_time = time.time()
    print('Advent 22')
    advent22_1()
    advent22_2()
    end_time_1 = time.time()
    print("time elapsed: {:.2f}s".format(end_time_1 - start_time))
