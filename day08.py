import time
import math


def advent8_1():
    #file = open('input08_example.txt')
    file = open('input08.txt')

    instructions = file.readline().strip('\n')
    file.readline()
    nodes = dict()
    for line in file:
        row = line.strip('\n')
        nkey, elem = row.split(' = ')
        ln, rn = elem.lstrip('(').rstrip(')').split(', ')
        nodes[nkey] = {'L' : ln, 'R' : rn}

    steps = 0
    nofs = len(instructions)
    node = 'AAA'
    while node != 'ZZZ':
        node = nodes[node][instructions[steps % nofs]]
        steps += 1
        #print(node)

    print('Nof steps:', steps)

def primeFactors(n): 
    factors = list()
    # Print the number of two's that divide n 
    while n % 2 == 0: 
        factors.append(2)
        n = n / 2
          
    # n must be odd at this point 
    # so a skip of 2 ( i = i + 2) can be used 
    for i in range(3,int(math.sqrt(n))+1,2): 
          
        # while i divides n , print i and divide n 
        while n % i== 0: 
            factors.append(int(i)) 
            n = n / i 
              
    # Condition if n is a prime 
    # number greater than 2 
    if n > 2: 
        factors.append(int(n))

    return factors;

        
def advent8_2():
    #file = open('input08_example2.txt')
    file = open('input08.txt')

    instructions = file.readline().strip('\n')
    file.readline()
    nodes = dict()
    for line in file:
        row = line.strip('\n')
        nkey, elem = row.split(' = ')
        ln, rn = elem.lstrip('(').rstrip(')').split(', ')
        nodes[nkey] = {'L' : ln, 'R' : rn}

    startnodes = list()
    for k in nodes.keys():
        if k[2] == 'A':
            startnodes.append(k)
            
    nofs = len(instructions)
    print(startnodes)
    total_steps = list()
    for node in startnodes:
        not_there = True
        steps = 0
        #print(node)
        while not_there:
            next_node = nodes[node][instructions[steps % nofs]]
            steps += 1
            if next_node[2] == 'Z':
                not_there = False
                print(steps)
                total_steps.append(steps)
            node = next_node

    all_factors = list()
    for s in total_steps:
        f = primeFactors(s)
        for fact in f:
            all_factors.append(fact)
        print('Factors :', s, ' : ', f)

    set_of_factors = set(all_factors)
    necessary_steps = 1
    for f in set_of_factors:
        necessary_steps *= f
        
    print('Nof steps:', necessary_steps)


if __name__ == '__main__':

    start_time = time.time()
    print('Advent 8')
    advent8_1()
    advent8_2()
    end_time_1 = time.time()
    print("time elapsed: {:.2f}s".format(end_time_1 - start_time))
