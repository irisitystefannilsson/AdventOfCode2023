import time
import numpy as np


SEQUENCE = list()


def tilt(col : np.full):
    cols = col.shape[0]
    tcol = cols*['.']
    ff = 0
    for i in range(col.shape[0]):
        if col[i] == 'O':
            tcol[ff] = 'O'
            ff += 1
        elif col[i] == '#':
            tcol[i] = '#'
            ff = i + 1
            
    return tcol


def calc_load(col : list):
    load = 0
    cols = len(col)
    for i in range(cols):
        if col[i] == 'O':
            load += cols - i
    return load
    

def find_load(in_board : list):
    rows = len(in_board)
    cols = len(in_board[0])
    board = np.full((rows, cols), '.', dtype=str)
    for i in range(rows):
        for j in range(cols):
            board[i, j] = in_board[i][j]

    load = 0
    for j in range(cols):
        tilted = tilt(board[:, j])
        #print(tilted)
        load += calc_load(tilted)
    return load


def advent14_1():
    #file = open('input14_example.txt')
    file = open('input14.txt')

    board = list()
    for line in file:
        line = line.strip('\n')
        board.append(list(line))

    load = find_load(board)
    print('Load (1):', load)


def rotate(in_board : list):
    global SEQUENCE
    rows = len(in_board)
    cols = len(in_board[0])
    board = np.full((rows, cols), '.', dtype=str)
    for i in range(rows):
        for j in range(cols):
            board[i, j] = in_board[i][j]

    for j in range(cols):
        tilted = tilt(board[:, j])
        for i in range(rows):
            board[i, j] = tilted[i]
    for i in range(rows):
        tilted = tilt(board[i, :])
        for j in range(cols):
            board[i, j] = tilted[j]
    for j in range(cols):
        tilted = tilt(np.flip(board[:, j], 0))
        for i in range(rows):
            board[i, j] = tilted[rows - 1 - i]
    for i in range(rows):
        tilted = tilt(np.flip(board[i, :], 0))
        tilted.reverse()
        for j in range(cols):
            board[i, j] = tilted[j]
    load = 0
    for j in range(cols):
        load += calc_load(list(board[:, j]))

    SEQUENCE.append(load)
    return board
                    

def advent14_2():
    #file = open('input14_example.txt')
    file = open('input14.txt')

    board = list()
    for line in file:
        line = line.strip('\n')
        board.append(list(line))

    for r in range(1000):
        board = rotate(board)

    global SEQUENCE
    s, l = find_repeat(SEQUENCE)
    idx = (1000000000 - s) % l
    print('Load (2):', SEQUENCE[s + idx - 1])
    # After 135 rotations the load starts
    # repeating with a cycle length of 11
    # The correct load is then:
    # indx = (1000000000 - 135) % 11
    # cycle_element[indx] === 83516


def check_repeat(sequence : list, start : int, length : int):
    if sequence[start:start + length] == sequence[start + length:start + 2*length]:
        return True
    return False


def find_repeat(seq : list):
    for s in range(len(seq) - 1):
        for l in range(2, (len(seq) - s - 1) // 2):
            if check_repeat(seq, s, l):
                return s, l
    return -1, -1
    
if __name__ == '__main__':

    start_time = time.time()
    print('Advent 14')
    advent14_1()
    advent14_2()
    end_time_1 = time.time()
    print("time elapsed: {:.2f}s".format(end_time_1 - start_time))
