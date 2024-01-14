import time
import numpy as np


def corona_chars(row : int, number : (str, int), schematic : np.full):
    c_start = max(0, number[1] - 1)
    c_stop = min(c_start + len(number[0]) + 2, len(schematic[row]))
    r_start = max(0, row - 1)
    r_stop = min(row + 2, schematic.shape[0])

    #print('lims: ', c_start, c_stop, r_start, r_stop)
    ret_chars = []
    for r in range(r_start, r_stop):
        for c in range(c_start, c_stop):
            if not (c in range(number[1], number[1] + len(number[0])) and r == row):
                ret_chars.append(schematic[r, c])

    return ret_chars

        
def advent3_1():
    #file = open('input03_example.txt')
    file = open('input03.txt')
    ex_size = (10, 10)
    real_size = (140, 140)
    #schematic = np.full(ex_size, '.', dtype=str)
    schematic = np.full(real_size, '.', dtype=str)
    numbers_on_rows = []
    r = 0
    number = ''
    for line in file:
        row = line.strip('\n')
        c = 0
        numbers_on_rows.append([])
        for ch in row:
            schematic[r, c] = ch
            if ch.isdigit(): # or (ch in ['-', '+'] and number == '' and c < len(row) and row[c].isdigit()):
                number += ch
            else:
                if number != '':
                    numbers_on_rows[r].append((number, c - len(number)))
                number = ''
            c += 1
        if number != '':
            numbers_on_rows[r].append((number, c - len(number)))
        number = ''
        r += 1

    #print(schematic)
    sum = 0
    for r in range(len(numbers_on_rows)):
        for num in numbers_on_rows[r]:
            corona = corona_chars(r, num, schematic)
            for ch in corona:
                #print(ch)
                if not ch.isdigit() and ch != '.':
                    sum += int(num[0])
                    break

    print('Sum (1): ', sum)


def check_ratio(numbers_on_rows : list, r : int, c : int, bounds : tuple):
    g = [0, 0]
    c_start = max(0, c - 1)
    c_stop = min(c + 2, bounds[1])
    r_start = max(0, r - 1)
    r_stop = min(r + 2, bounds[0])
    gi = 0
    for i in range(r_start, r_stop):
        for num in numbers_on_rows[i]:
            used_num = (0, (0, 0))
            for j in range(c_start, c_stop):
                if j in num[1] and num != used_num:
                    #print(i,j,num)
                    g[gi] = int(num[0])
                    gi += 1
                    if gi == 2:
                        #print(g)
                        return g[0], g[1]
                    used_num = num
                    break
    
    return g[0], g[1]


def advent3_2():
    #file = open('input03_example.txt')
    file = open('input03.txt')
    ex_size = (10, 10)
    real_size = (140, 140)
    #schematic = np.full(ex_size, '.', dtype=str)
    schematic = np.full(real_size, '.', dtype=str)
    numbers_on_rows = []
    r = 0
    number = ''
    for line in file:
        row = line.strip('\n')
        c = 0
        numbers_on_rows.append([])
        for ch in row:
            schematic[r, c] = ch
            if ch.isdigit(): # or (ch in ['-', '+'] and number == '' and c < len(row) and row[c].isdigit()):
                number += ch
            else:
                if number != '':
                    numbers_on_rows[r].append((number, range(c - len(number), c)))
                number = ''
            c += 1
        if number != '':
            numbers_on_rows[r].append((number, range(c - len(number), c)))
        number = ''
        r += 1

    gear_sum = 0
    for r in range(schematic.shape[0]):
        for c in range(schematic.shape[1]):
            if schematic[r, c] == '*': #gear
                g1, g2 = check_ratio(numbers_on_rows, r, c, real_size)
                gear_sum += g1*g2

    print('Sum (2): ', gear_sum)

    
if __name__ == '__main__':

    start_time = time.time()
    print('Advent 3')
    advent3_1()
    advent3_2()
    end_time_1 = time.time()
    print("time elapsed: {:.2f}s".format(end_time_1 - start_time))
