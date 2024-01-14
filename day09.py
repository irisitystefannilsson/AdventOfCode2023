import time


def next_seq(seq: list):
    nseq = list()
    for i in range(1, len(seq)):
        nseq.append(seq[i] - seq[i-1])
    if all(e == 0 for e in nseq):
        nseq.append(0)
        return nseq
    else:
        nnseq = next_seq(nseq)
        nseq.append(nseq[-1] + nnseq[-1])
        return nseq


def prev_seq(seq: list):
    pseq = list()
    for i in range(1, len(seq)):
        pseq.append(seq[i] - seq[i-1])
    if all(e == 0 for e in pseq):
        pseq.insert(0, 0)
        return pseq
    else:
        ppseq = prev_seq(pseq)
        pseq.insert(0, pseq[0] - ppseq[0])
        return pseq

        
def advent9_1():
    #file = open('input09_example.txt')
    file = open('input09.txt')

    sum = 0
    for line in file:
        row = line.strip('\n')
        sequence = row.split()
        sequence = [int(e) for e in sequence]
        #print(sequence)
        nseq = next_seq(sequence)
        #print(nseq)
        sequence.append(sequence[-1] + nseq[-1])
        #print(sequence)
        #print('------------')
        sum += sequence[-1]

    print('Sum (1): ', sum)
    

def advent9_2():
    #file = open('input09_example.txt')
    file = open('input09.txt')

    sum = 0
    for line in file:
        row = line.strip('\n')
        sequence = row.split()
        sequence = [int(e) for e in sequence]
        #print(sequence)
        pseq = prev_seq(sequence)
        #print(nseq)
        sequence.insert(0, sequence[0] - pseq[0])
        #print(sequence)
        #print('------------')
        sum += sequence[0]

    print('Sum (2): ', sum)



if __name__ == '__main__':

    start_time = time.time()
    print('Advent 9')
    advent9_1()
    advent9_2()
    end_time_1 = time.time()
    print("time elapsed: {:.2f}s".format(end_time_1 - start_time))
