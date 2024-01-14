import time
import math


def tp_roots(d, T):
    root1 = math.floor(T/2 + math.sqrt(T*T/4 - d))
    root2 = math.ceil(T/2 - math.sqrt(T*T/4 - d))
    if root1*(T - root1) <= d:
        root1 -= 1
    if root2*(T - root2) <= d:
        root2 += 1
    return root2, root1
        
def advent6_1():
    #file = open('input06_example.txt')
    file = open('input06.txt')
    time_line = file.readline().strip('\n');
    times = time_line.split(':')[1].split()
    dist_line = file.readline().strip('\n');
    dists = dist_line.split(':')[1].split()
    #print(times)
    #print(dists)
    nofways = 1
    for d, T in zip(dists, times):
        r1, r2 = tp_roots(int(d), int(T))
        #print(r1, r2)
        nofways *= (r2 - r1 + 1)

    print('Nof ways (1):', nofways)
    
    
def advent6_2():
    #file = open('input06_example.txt')
    file = open('input06.txt')
    time_line = file.readline().strip('\n');
    time = int(time_line.split(':')[1].replace(' ', ''))
    dist_line = file.readline().strip('\n');
    dist = int(dist_line.split(':')[1].replace(' ', ''))
    #print(time, dist)
    r1, r2 = tp_roots(dist, time)
    #print(r1, r2)
    nofways = (r2 - r1 + 1)

    print('Nof ways (2):', nofways)
    

    
if __name__ == '__main__':

    start_time = time.time()
    print('Advent 6')
    advent6_1()
    advent6_2()
    end_time_1 = time.time()
    print("time elapsed: {:.2f}s".format(end_time_1 - start_time))
