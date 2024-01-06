import time
import numpy as np
import functools
import math
import copy

NUMBER_OF_CALLS = 0
LOG_FILE = open('logfile.txt', 'w')
DATA_CACHE = dict()
USED = []


def ok_conf(conf : list, constr : list):
    for l in range(min(len(conf), len(constr))):
        if conf[l] == '#' and constr[l] not in ['#', '?']:
            return False
        if conf[l] == '.' and constr[l] not in ['.', '?']:
            return False
    return True


def generate(numbers : list, constr : str, start=0):
    ckey = tuple(numbers + list(constr) + [start])
    if ckey in DATA_CACHE:
        return DATA_CACHE[ckey]
    
    lc = len(constr) - start
    ln = sum(numbers) + len(numbers) - 1
    nod = 0
    if lc < ln:
        return 0
    for i in range(lc - ln + 1):
        testarr = i*['.'] + numbers[0]*['#'] + ['.']
        if ok_conf(testarr, constr[start:start+len(testarr)]):
            if len(numbers) > 1:
                nod += generate(numbers[1:], constr, start + i + numbers[0] + 1)
            else:
                endarr = (len(constr) - (start + len(testarr)))*['.']
                if ok_conf(endarr, constr[(start + len(testarr)):]):
                    nod += 1

    DATA_CACHE[ckey] = nod
    return nod

    
def advent12_1():
    #file = open('input12_example.txt')
    file = open('input12.txt')

    sum_parr = 0
    for line in file:
        line = line.strip('\n')
        springs, numbers = line.split(' ')
        numbers = numbers.split(',')
        numbers = [int(e) for e in numbers]
        pbroke = springs.split('.')
        pbroke = [e for e in pbroke if e != '']
        parr = generate(numbers, springs)
        #print('----------- parr : ', parr, '----------')
        sum_parr += parr

    print('Sum of arrs(1):' ,sum_parr)


def advent12_2():
    #file = open('input12_example.txt')
    file = open('input12.txt')

    sum_parr = 0
    for line in file:
        line = line.strip('\n')
        springs, numbers = line.split(' ')
        numbers = numbers.split(',')
        numbers = [int(e) for e in numbers]
        numbers = 5*numbers
        springs = springs + '?' + springs + '?' + springs + '?' + springs + '?' + springs 
        pbroke = springs.split('.')
        pbroke = [e for e in pbroke if e != '']
        parr = generate(numbers, springs)
        #print('----------- parr : ', parr, '----------')
        sum_parr += parr
        #break
    print('Sum of arrs(2):' ,sum_parr)
    
    
if __name__ == '__main__':

    start_time = time.time()
    print('Advent 12')
    advent12_1()
    advent12_2()
    end_time_1 = time.time()
    print("time elapsed: {:.2f}s".format(end_time_1 - start_time))
